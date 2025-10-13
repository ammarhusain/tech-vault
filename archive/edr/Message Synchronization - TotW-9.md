---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

# Tip of the Week #9: Message Synchronization

[go/proxy-totw/9](https://g3doc.corp.google.com/googlex/proxy/g3doc/totw/9.md?cl=head)

*by Ammar Husain (who/ammarh)*

When developing algorithms to add to the robot’s capabilities it is common to
fuse knowledge over multiple streams of data. This could be through raw sensor
measurements or with processed primitives that are produced by upstream
subsystems. Our algorithms are mostly composed inside of IPC modules and the
streams of data are received through IPC channel subscribers. Since parallel
data streams can rarely be processed independent of each other, some level of
synchronization becomes necessary. Traditionally this synchronization is handled
by the module authors by setting multiple independent channel subscriptions,
buffering each stream of data and then triggering the algorithm to start
processing when a certain synchronization condition has been met.

For example, say you want to write a simple module `ColorizeCBrModule` that
colorizes the CBr point cloud using the RGB image. You would nominally need to
write two IPC subscribers: one for the CBr point cloud and the other for the RGB
image.
([live-snippets](http://google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr.h))

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr.h snippet:block content:Register.*SetPrefix
```

The RGB images would then need to be stored locally in a container until a CBr
message arrives.

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr.h snippet:comment,block content:CameraHandler\(.*camera_buffer_
```

When a CBr message comes through, the `camera_buffer_` would then be queried for
a corresponding camera message that is synchronized in time. For simplicity,
let's say we just use the newest message in the buffer as long as it is within
an acceptable time bound from when the CBr message was generated. We would then
need to query the `transform_tree_` for an interpolated transform that spatially
aligns the two messages. The synchronization logic would look as follows:

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr.h snippet:comment,block function:CBrHandler
```

Note that the logic above is for the simplest case. The synchronization logic
gets more complicated and stateful for more intricate queries into the
`camera_buffer_`, such as `GetNearestSample`, `GetExactSample` etc, where the
closest aligned camera message might arrive after its best aligned CBr message.

This approach has the following drawbacks:

- Synchronization logic is reimplemented in every module in slightly different
	 ways.
- There is a higher risk of subtle synchronization bugs.
- Every module is responsible for maintaining memory hygiene through correct
	 usage and storage of `ActiveMsgPtr` and `WeakMsgPtr`.
- Lot of boilerplate code obscures away the core algorithmic code that
	 actually processes data.

If you write code that needs to synchronize over multiple IPC channels, consider
using the [[message_sync]] library.

# MESSAGE_SYNC

The [[message_sync]] library
implements two main primitives: [`Collector`](http://cs/class:blue::Collector)
and [`MessageSynchronizer`](http://cs/class:blue::MessageSynchronizer). These
primitives when used in conjunction provide an abstraction that wraps over the
individual message handlers, stateful message containers as well as any queries
for time aligned message retrievals. Additional it adds some basic sanity
checking on the messages. This TotW provides practical code examples for using
the library through
[live-snippets](http://google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync.h).

To learn more about the design internals please check out the
go/proxy-msg-sync-sw-review presentation or the go/proxy-msg-sync design doc.

Let's walk through an example of writing the same module as above, using the
[[message_sync]] library. Rather
than registering individual subscribers and writing their corresponding
`Handler` functions, we would build `Collector` objects.

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync.h snippet:comment,block content:cbr_collector.*child_frame_id
```

`Collector` objects are created using the
[`MakeCollector`](http://cs/MakeCollector\( f:message_sync.h) factory functions
and can be of the following two types:

## [`CollectorIpc`](http://cs/class:blue::CollectorIpc)

`CollectorIpc` can be thought of as syntactic sugar that replaces the callback
handler as well as the corresponding `HistoryBuffer` to temporarily store
incoming messages. `cbr_collector` and `camera_collector` in the example above
are of this type. Notice that these are instantiated with a
[`CollectorReturn`](http://cs/"enum class CollectorReturn") enum. This
determines how the messages for the given `Collector` should be aligned with
respect to the trigger timestamp. The trigger timestamp is populated by the
primary `Collector` and is used to synchronize all incoming messages. This is
discussed in more detail in the subsequent section.

## [`CollectorTf`](http://cs/class:blue::CollectorTf)

`CollectorTf` is a wrapper over the `TransformTree` and queries for the time
interpolated transform between two user specified frames given a trigger
timestamp that is determined by the primary `Collector`.

Next we define how far in timestamp can the camera message be from its
corresponding CBr message.

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync.h snippet:comment,block content:Set\san.*SetTimestampTolerance
```

And finally we build the `MessageSynchronizer` object passing it a callback
pointer as well as all the collectors we created above.

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync.h snippet:comment,block content:MakeMessageSynchronizer.*cbr_pose_camera_collector
```

# [`MessageSynchronizer`](http://cs/class:blue::MessageSynchronizer)

`MessageSynchronizer` implements the core synchronization logic that we had
manually handled earlier. Additionally it packages the messages from all its
associated collectors and dispatches them to the user defined callback when
ready to do so. Similar to `MakeCollector`, the library provides
[`MakeMessageSynchronizer`](http://cs/"std::unique_ptr<MessageSynchronizer> MakeMessageSynchronizer")
factory functions to build these objects. However unlike the collectors, the
`MessageSynchronizer` must remain in scope for the lifetime of the class and
should therefore be a member variable.

The first two arguments in the builder bind the provided class member function
as the aggregated callback for `message_sync`. This is followed by a variable
number of `Collector` objects that the `MessageSynchronizer` needs to
synchronize the incoming messages over. The first `Collector` argument serves as
the primary collector and will populate the trigger timestamp. All other
collectors will then be synchronized with respect to this trigger timestamp.
Therefore, by definition, the primary must be a `CollectorIpc` instantiated with
the `CollectorReturn::kExact` as its return value. In the example above, the
`cbr_collector` has been made primary.

**NOTE: By default the collectors read the user populated
[`timestamp`](http://cs/"int64 timestamp" f:message_header.proto) field set in
the `MessageHeaderProto` for synchronization. For non-custom IPC message this
can be overwritten. See Advanced Features below**

Based on the order of collectors passed to the `MessageSynchronizer` and their
corresponding `CollectorReturn` instantiations, the bound callback must accept
the corresponding types as its arguments and in that specific order. So for this
example:

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync.h snippet:comment,block function:CBrCameraHandler
```

Here is a handy guide for the available `CollectorReturn` options and their
argument types:

CollectorReturn                                                                  | Arg Type
-------------------------------------------------------------------------------- | --------
[`kExact`](http://google3/googlex/robotics/message_sync/message_sync.h;l=268)    | [`MessageSynchronizer::ActivePtr<T>`](http://google3/googlex/robotics/message_sync/message_sync.h;l=195)
[`kNewest`](http://google3/googlex/robotics/message_sync/message_sync.h;l=273)   | [`MessageSynchronizer::ActivePtr<T>`](http://google3/googlex/robotics/message_sync/message_sync.h;l=195)
[`kNearest`](http://google3/googlex/robotics/message_sync/message_sync.h;l=277)  | [`MessageSynchronizer::ActivePtr<T>`](http://google3/googlex/robotics/message_sync/message_sync.h;l=195)
[`kBefore`](http://google3/googlex/robotics/message_sync/message_sync.h;l=279)   | [`MessageSynchronizer::ActivePtr<T>`](http://google3/googlex/robotics/message_sync/message_sync.h;l=195)
[`kAfter`](http://google3/googlex/robotics/message_sync/message_sync.h;l=283)    | [`MessageSynchronizer::ActivePtr<T>`](http://google3/googlex/robotics/message_sync/message_sync.h;l=195)
[`kInterval`](http://google3/googlex/robotics/message_sync/message_sync.h;l=287) | [`MessageSynchronizer::Interval`](http://google3/googlex/robotics/message_sync/message_sync.h;l=202)
[`kBuffer`](http://google3/googlex/robotics/message_sync/message_sync.h;l=292)   | [`WeakMsgPtrHistoryBuffer<T>`](http://google3/googlex/proxy/module_system/core/message_pointer.h;l=649;rcl=322064470)
[`CollectorTf`](http://cs/class:blue::CollectorTf)                               | [`eigenmath::Pose3d`](http://cs/Pose3d f:eigenmath/pose3.h)

This is all that is needed to get up and running with using the
[`message_sync`](http://google3/googlex/robotics/message_sync/) library!

## Advanced Features

### Watchdog Timer

Given system latency or the order of publishing for different channels, it might
not be uncommon for the primary channel message, that triggers the
synchronization event, to arrive before any of the other channels. In this case
one or more collectors will request the `MessageSynchronizer` to wait. By
default the wait time is 10 seconds, though this can be custom set using
[`SetWatchdogTimeout`](http://cs/MessageSynchronizer::SetWatchDogTimeout).

**NOTE: The MessageSynchronizer does not have an internal clock and therefore
relies on the
[`publish_timestamp`](http://cs/"int64 publish_timestamp" f:message_header.proto)
as a proxy. The `publish_timestamp` is auto-populated by the IPC system and
represents the time when the message was actually published. The time elapsed is
the difference in the `publish_timestamp` between the most recently received
message on any of the bound collectors and the trigger message on the primary
collector. Please note that this is different from the user populated
[`timestamp`](http://cs/"int64 timestamp" f:message_header.proto) in the message
that is used for synchronization by the various `CollectorReturn` types.**

### Binding Arguments as Optional

When synchronizing over multiple incoming channels, it is not always necessary
to require all the messages in order to meaningfully process. It also helps in
better introspection if the module prints debug information on what channels it
is failing to receive data on. The `message_sync` library facilitates this by
allowing users to bind the optional callback arguments with a `util::StatusOr`.
So following the example above, if the user would like to receive a callback
even if `camera_proto` and/or the `camera_pose_cbr` transform are not available,
the callback function would be:

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync_advanced.h snippet:comment,block function:CBrCameraHandlerOptional
```

**NOTE: If the messages are delayed on any of the bound collector channels, the
MessageSynchronizer will still wait for the duration of the watchdog timeout
before dispatching the callback with a not OK status for the corresponding
message. Other than changing the argument type in the callback function
signature no other change is necessary, on how the `Collector` or
`MessageSynchronizer` objects are created, for optional arguments to work.**

### Buffering the Primary Channel

During execution it might frequently be the case that multiple newer messages on
the primary channel arrive while the current synchronization trigger event is
still waiting on one or more of the other collectors. By default the
`MessageSynchronizer` will buffer these messages on the primary channel and
service them in FIFO order. Therefore the newest message on the primary channel
will not be synchronized and dispatched until all the pending primary messages
(aka trigger events) in the buffer have been serviced. This buffering can be
turned off with
[`SetBufferTriggerEvents`](http://cs/MessageSynchronizer::SetBufferTriggerEvents),
in which case the user can pick whether the `MessageSynchronizer` should drop
the newest primary message in favor of the currently synchronization pending
message or vice versa, via
[`SetPickNewestTriggerEvent`](http://cs/MessageSynchronizer::SetPickNewestTriggerEvent)

### Defining a Custom Timestamp Extractor

As mentioned previously the `message_sync` library defaults to using the
[`timestamp`](http://cs/"int64 timestamp" f:message_header.proto) and
[`publish_timestamp`](http://cs/"int64 publish_timestamp" f:message_header.proto)
fields from the `MessageHeaderProto` for synchronization and watchdog timestamps
respectively. If the message on the incoming IPC channel does not contain this
header, a custom `TimestampExtractor` can easily be used to override the default
one in [`MakeCollector`](http://cs/MakeCollector\( f:message_sync.h) by passing
it in as the third template argument.

This custom `TimestampExtractor` class must continue to maintain the
synchronization and watchdog timestamp semantics by providing both timestamps.
Though these two timestamps may be the same as long as they are aligned with
messages coming in from the other bound collector channels.

### Writing a Synchronizedpublisher

With go/proxy-reliable-ipc the IPC system provides the concept of
[reliable channels](https://docs.google.com/document/d/1s0vrUVZ4Xmzt6y53P2TrJV8dWBVU75Jx9pF7fT0AZ54/edit#)
where any messages sent by a reliable publisher are guaranteed to be received by
a reliable subscriber. In order to create a reliable publisher the module must
register a publisher callback, similar to the subscriber callback, which gets
called when the reliable channel is ready to publish data out.

A common workflow for a module publishing over Reliable IPC would be to:

- subscribe to several reliable/unrealiable channels,
- synchronize them to process data,
- notify the module manager of an intent to publish,
- wait for the module's publisher callback to get triggered and then
- finally publish the processed message out over the reliable channel.

The `message_sync` library provides a way to wrap this two stage synchronization
paradigm into a single unified callback with the `SynchronizedPublisher`.
Following the example from earlier, say you want to publish an
`EchoMessageProto` over a reliable publisher everytime the CBr points have been
successfully colorized. In addition to the collectors as before, you would now
create a reliable publisher channel and pass it to
[`MakeSynchronizedReliablePublisher`](http://cs/MakeSynchronizedReliablePublisher f:message_sync_publisher.h):

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync_advanced.h snippet:comment,block content:MakeSynchronizedReliablePublisher.*camera_collector
```

The synchronized callback in this case would need to accept an output pointer to
`EchoMessageProto` followed by the collector return arguments as before.

```live-snippet
cs/file://depot/google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_sync_advanced.h snippet:comment,block function:PublishSynchronizedCbrCamera
```

Once the processing has been completed and results written to the provided
`EchoMessageProto*`, call `Publish()` for the IPC system to reliably publish
that message out. Please refer to the
[live-snippets](http://google3/googlex/proxy/g3doc/totw/live_snippets/message_sync/colorize_cbr_advanced.h)
for a minimal example.

### Debugging Faqs

#### Why Do I Get a Compilation Error when I Hook Everything Up?

The `message_sync` library leverages compile time sanity checking to ensure that
that the collectors, synchronizer and the bound aggregate callback are
compatible with each other. The most common reasons for compilation failures
are:

- The synchronized callback function that is being bound to the
	 `MessageSynchronizer` is incompatible with the `Collector` types that are
	 being associated in `MakeMessageSynchronizer`. This could be either:
	 - The number of callback arguments are not the same as the number of
		  collectors.
	 - The argument type in the callback function is not the expected return
		  type for that collector. Please refer to the table above for
		  `CollectorReturn` argument types.
- The primary collector must be a `CollectorIpc` and instantiated with
	 `CollectorReturn::kExact`. This is because this collector serves as the
	 trigger timestamp for synchronizing the other collector channels.

#### What Do I Do if I Am not Getting Any Synchronized Callbacks?

There could be multiple different reasons why an aggregate callback might not be
getting called ranging from channel latency to synchronization requirements over
a host of collectors. The `message_sync` library logs some helpful state
introspection information at the `MODULE_DEBUG` log level. Step 0 for any
debugging should be to enable this log level by setting the appropriate `-vtag`.
Here are a few useful debugging tips that require minimal effort and ranked in
that order:

- Check the logs to make sure that all the collectors are
	 [receiving data](http://google3/googlex/robotics/message_sync/message_sync.h;l=850).
	 If it is hard to disambiguate the collectors from each other in the logs, a
	 unique name can be set for each using
	 [`SetCollectorName`](http://cs/blue::Collector::SetCollectorName).
- Check the logs to see if any of the collectors are constantly in a failed or
	 waiting state.
- Ensure that the watchdog timeout is not too short. This might not give the
	 `MessageSynchronizer` enough time to package up if any of the collectors are
	 tardy.
- Bind all the collectors as optional by wrapping the arguments in a
	 `util::StatusOr`. This is guaranteed to trigger a callback as long as a
	 message was received on the primary collector channel. The status for each
	 collector can then be read to figure out the point of failure. Please refer
	 to the table below.

#### Why Are Some of My Messages Getting Dropped? what Do the Failed Status Messages for a Collector Argument Mean?

Here is a handy table of status codes with their associated failure reasons:

absl::StatusCode   | Reason
------------------ | ------
`kUnavailable`     | Either the collector doesn't have any messages or doesn't yet contain a message that would satisfy its `CollectorReturn` type. It is still waiting to receive newer messages that may or may not meet the synchronization criteria. For `CollectorTf`, it is still waiting on receiving a transform that can be interpolated to the synchronization timestamp. If this status was returned it either means that (a) the synchronizer watchdog timeout was up or that (b) the `TriggerBuffer` has been disabled so a new primary collector message preempted this one.
`kOutOfRange`      | The messages currently in the collectors storage buffer do not satisfy the acceptable timestamp tolerance that the user desires. Given monotonically increasing time, this synchronization condition will not be met, hence it is safe to just give up.
`kDataLoss`        | Collectors internally store all messages as [`WeakMsgPtr`](http://cs/class:WeakMsgPtr) types. In this case it received the relevant message but lost access to it while waiting for the synchronization to finish. In most cases this can be resolved by setting a higher number for [`SetMaxRestoredActiveMsgPtrs`](http://cs/IpcModuleChannel::SetMaxRestoredActiveMsgPtrs) in this collectors `IpcModuleChannel` option.
`kInvalidArgument` | The frame ids specified in the `CollectorTf` are invalid.
`kInternal`        | Lookup for the transform failed within the TransformTree either due to the tree being in an invalid state or invalid arguments.
