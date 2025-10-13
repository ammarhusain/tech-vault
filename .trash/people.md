Bedroom:CrashReporter root# cat peopleawarenessd-2023-06-29-210342.ips

{"app_name":"peopleawarenessd","timestamp":"2023-06-29 21:03:42.00 -0700","app_version":"","slice_uuid":"5200896b-753f-302f-9997-166cba74d7b1","build_version":"","platform":3,"share_with_app_devs":0,"is_first_party":1,"bug_type":"309","os_version":"Apple TVOS 18.0 (22V19)","roots_installed":0,"incident_id":"2DF31036-F678-446B-990E-A0E9098B7FF4","name":"peopleawarenessd"}

{

  "uptime" : 95,

  "procRole" : "Unspecified",

  "version" : 2,

  "userID" : 501,

  "deployVersion" : 210,

  "modelCode" : "AppleTV14,4",

  "coalitionID" : 317,

  "osVersion" : {

    "isEmbedded" : true,

    "train" : "Apple TVOS 18.0",

    "releaseType" : "Internal",

    "build" : "22V19"

  },

  "captureTime" : "2023-06-29 21:03:42.2717 -0700",

  "codeSigningMonitor" : 1,

  "incident" : "2DF31036-F678-446B-990E-A0E9098B7FF4",

  "pid" : 322,

  "cpuType" : "ARM-64",

  "roots_installed" : 0,

  "bug_type" : "309",

  "procLaunch" : "2023-06-29 21:03:42.1960 -0700",

  "procStartAbsTime" : 2294990827,

  "procExitAbsTime" : 2296798527,

  "procName" : "peopleawarenessd",

  "procPath" : "\/System\/Library\/PrivateFrameworks\/Motif.framework\/peopleawarenessd",

  "parentProc" : "launchd.development",

  "parentPid" : 1,

  "coalitionName" : "com.apple.peopleawarenessd",

  "crashReporterKey" : "5958dbc4615a922fc36eb61f57fa9fce2b2512cf",

  "systemID" : "00008110-001A68203A40011E",

  "codeName" : "J310AP",

  "consecutiveCrashCount" : 1,

  "throttleTimeout" : 10,

  "codeSigningID" : "com.apple.peopleawarenessd",

  "codeSigningTeamID" : "",

  "codeSigningFlags" : 570434049,

  "codeSigningValidationCategory" : 1,

  "codeSigningTrustLevel" : 10,

  "instructionByteStream" : {"beforePC":"fyMD1f17v6n9AwCRtB4AlL8DAJH9e8Go\/w9f1sADX9YQKYDSARAA1A==","atPC":"AwEAVH8jA9X9e7+p\/QMAkakeAJS\/AwCR\/XvBqP8PX9bAA1\/WkCmA0g=="},

  "exception" : {"codes":"0x0000000000000000, 0x0000000000000000","rawCodes":[0,0],"type":"EXC_CRASH","signal":"SIGABRT"},

  "termination" : {"flags":0,"code":6,"namespace":"SIGNAL","indicator":"Abort trap: 6","byProc":"peopleawarenessd","byPid":322},

  "asi" : {"libswiftCore.dylib":["generic witness table at 0x1cf939a7c contains out-of-bounds requirement descriptor 0xbad4007"],"libsystem_c.dylib":["abort() called"]},

  "faultingThread" : 0,

  "threads" : [{"triggered":true,"id":3812,"threadState":{"x":[{"value":0},{"value":0},{"value":0},{"value":0},{"value":18446744073709550432},{"value":16},{"value":26458647880073539},{"value":0},{"value":5368470618104359144},{"value":5383530625160791784},{"value":170401860},{"value":170401860},{"value":170401860},{"value":170401860},{"value":4294967295},{"value":144115188344291568},{"value":328},{"value":8273206384},{"value":0},{"value":6},{"value":259},{"value":8138927840,"symbolLocation":224,"symbol":"_main_thread"},{"value":24445996146903248,"symbolLocation":24445991776157696,"symbol":"protocol descriptor for ChannelDescriptor"},{"value":28579610111527120,"symbolLocation":28579605740781568,"symbol":"protocol descriptor for ChannelDescriptor"},{"value":7777524280,"symbolLocation":36208,"symbol":"__unnamed_7"},{"value":4370745588,"symbolLocation":0,"symbol":"associated conformance descriptor for ChannelDescriptor.ChannelDescriptor.Message: SignalMessage"},{"value":7777524284,"symbolLocation":36212,"symbol":"__unnamed_7"},{"value":8139284856,"symbolLocation":38712,"symbol":"InitialAllocationPool"},{"value":8261941376,"symbolLocation":9400,"symbol":"block_descriptor.78"}],"flavor":"ARM_THREAD_STATE64","lr":{"value":6675005920},"cpsr":{"value":1073745920},"fp":{"value":6103783136},"sp":{"value":6103783104},"esr":{"value":1442840704,"description":" Address size fault"},"pc":{"value":6675208204,"matchesCrashFrame":1},"far":{"value":8116519864}},"queue":"com.apple.main-thread","frames":[{"imageOffset":14348,"symbol":"__pthread_kill","symbolLocation":8,"imageIndex":5},{"imageOffset":8672,"symbol":"pthread_kill","symbolLocation":268,"imageIndex":6},{"imageOffset":474060,"symbol":"abort","symbolLocation":176,"imageIndex":7},{"imageOffset":3695556,"symbol":"swift::fatalErrorv(unsigned int, char const*, char*)","symbolLocation":128,"imageIndex":8},{"imageOffset":3695588,"symbol":"swift::fatalError(unsigned int, char const*, ...)","symbolLocation":32,"imageIndex":8},{"imageOffset":3850372,"symbol":"instantiateWitnessTable(swift::TargetMetadata<swift::InProcess> const*, swift::TargetProtocolConformanceDescriptor<swift::InProcess> const*, void const* const*, void**)","symbolLocation":1772,"imageIndex":8},{"imageOffset":3802424,"symbol":"swift::_getWitnessTable(swift::TargetProtocolConformanceDescriptor<swift::InProcess> const*, swift::TargetMetadata<swift::InProcess> const*, void const* const*)","symbolLocation":5348,"imageIndex":8},{"imageOffset":151572,"imageIndex":9},{"imageOffset":1046200,"imageIndex":9},{"imageOffset":3850312,"symbol":"instantiateWitnessTable(swift::TargetMetadata<swift::InProcess> const*, swift::TargetProtocolConformanceDescriptor<swift::InProcess> const*, void const* const*, void**)","symbolLocation":1712,"imageIndex":8},{"imageOffset":3802424,"symbol":"swift::_getWitnessTable(swift::TargetProtocolConformanceDescriptor<swift::InProcess> const*, swift::TargetMetadata<swift::InProcess> const*, void const* const*)","symbolLocation":5348,"imageIndex":8},{"imageOffset":3998932,"symbol":"swift::TargetProtocolConformanceDescriptor<swift::InProcess>::getWitnessTable(swift::TargetMetadata<swift::InProcess> const*) const","symbolLocation":484,"imageIndex":8},{"imageOffset":4017532,"symbol":"swift_conformsToProtocolMaybeInstantiateSuperclasses(swift::TargetMetadata<swift::InProcess> const*, swift::TargetProtocolDescriptor<swift::InProcess> const*, bool)","symbolLocation":3336,"imageIndex":8},{"imageOffset":4010696,"symbol":"swift_conformsToProtocolCommon","symbolLocation":136,"imageIndex":8},{"imageOffset":3646460,"symbol":"swift::_conformsToProtocol(swift::OpaqueValue const*, swift::TargetMetadata<swift::InProcess> const*, swift::TargetProtocolDescriptorRef<swift::InProcess>, swift::TargetWitnessTable<swift::InProcess> const**)","symbolLocation":60,"imageIndex":8},{"imageOffset":4006036,"symbol":"swift::_checkGenericRequirements(__swift::__runtime::llvm::ArrayRef<swift::TargetGenericRequirementDescriptor<swift::InProcess>>, __swift::__runtime::llvm::SmallVectorImpl<void const*>&, std::__1::function<void const* (unsigned int, unsigned int)>, std::__1::function<swift::TargetWitnessTable<swift::InProcess> const* (swift::TargetMetadata<swift::InProcess> const*, unsigned int)>)","symbolLocation":7056,"imageIndex":8},{"imageOffset":3975280,"symbol":"_gatherGenericParameters(swift::TargetContextDescriptor<swift::InProcess> const*, __swift::__runtime::llvm::ArrayRef<swift::MetadataOrPack>, swift::TargetMetadata<swift::InProcess> const*, __swift::__runtime::llvm::SmallVectorImpl<unsigned int>&, __swift::__runtime::llvm::SmallVectorImpl<void const*>&, swift::Demangle::__runtime::Demangler&)","symbolLocation":2612,"imageIndex":8},{"imageOffset":3956492,"symbol":"(anonymous namespace)::DecodedMetadataBuilder::createBoundGenericType(swift::TargetContextDescriptor<swift::InProcess> const*, __swift::__runtime::llvm::ArrayRef<swift::MetadataOrPack>, swift::MetadataOrPack) const","symbolLocation":248,"imageIndex":8},{"imageOffset":3950680,"symbol":"swift::Demangle::__runtime::TypeDecoder<(anonymous namespace)::DecodedMetadataBuilder>::decodeMangledType(swift::Demangle::__runtime::Node*, unsigned int, bool)","symbolLocation":11008,"imageIndex":8},{"imageOffset":3934944,"symbol":"swift_getTypeByMangledNodeImpl(swift::MetadataRequest, swift::Demangle::__runtime::Demangler&, swift::Demangle::__runtime::Node*, void const* const*, std::__1::function<void const* (unsigned int, unsigned int)>, std::__1::function<swift::TargetWitnessTable<swift::InProcess> const* (swift::TargetMetadata<swift::InProcess> const*, unsigned int)>)","symbolLocation":876,"imageIndex":8},{"imageOffset":3933844,"symbol":"swift_getTypeByMangledNode","symbolLocation":836,"imageIndex":8},{"imageOffset":3936548,"symbol":"swift_getTypeByMangledNameImpl(swift::MetadataRequest, __swift::__runtime::llvm::StringRef, void const* const*, std::__1::function<void const* (unsigned int, unsigned int)>, std::__1::function<swift::TargetWitnessTable<swift::InProcess> const* (swift::TargetMetadata<swift::InProcess> const*, unsigned int)>)","symbolLocation":1172,"imageIndex":8},{"imageOffset":3917176,"symbol":"swift_getTypeByMangledName","symbolLocation":836,"imageIndex":8},{"imageOffset":3918992,"symbol":"swift_getTypeByMangledNameInContextInMetadataStateImpl(unsigned long, char const*, unsigned long, swift::TargetContextDescriptor<swift::InProcess> const*, void const* const*)","symbolLocation":172,"imageIndex":8},{"imageOffset":144196,"symbol":"__swift_instantiateConcreteTypeFromMangledNameAbstract","symbolLocation":64,"imageIndex":9},{"imageOffset":444300,"imageIndex":9},{"imageOffset":443324,"imageIndex":9},{"imageOffset":3860124,"symbol":"swift::MetadataCacheEntryBase<(anonymous namespace)::SingletonMetadataCacheEntry, int>::doInitialization(swift::MetadataWaitQueue::Worker&, swift::MetadataRequest)","symbolLocation":184,"imageIndex":8},{"imageOffset":3760960,"symbol":"swift_getSingletonMetadata","symbolLocation":416,"imageIndex":8},{"imageOffset":442960,"imageIndex":9},{"imageOffset":18892,"imageIndex":4},{"imageOffset":11036,"imageIndex":4},{"imageOffset":6200,"symbol":"start","symbolLocation":2076,"imageIndex":10}]},{"id":3814,"frames":[{"imageOffset":42408,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}],"threadState":{"x":[{"value":6104346624},{"value":6659},{"value":6103810048},{"value":0},{"value":409604},{"value":18446744073709551615},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0}],"flavor":"ARM_THREAD_STATE64","lr":{"value":0},"cpsr":{"value":4096},"fp":{"value":0},"sp":{"value":6104346624},"esr":{"value":1442840704,"description":" Address size fault"},"pc":{"value":6675039656},"far":{"value":8139292752}}},{"id":3815,"frames":[{"imageOffset":42408,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}],"threadState":{"x":[{"value":6104920064},{"value":4867},{"value":6104383488},{"value":0},{"value":409604},{"value":18446744073709551615},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0}],"flavor":"ARM_THREAD_STATE64","lr":{"value":0},"cpsr":{"value":4096},"fp":{"value":0},"sp":{"value":6104920064},"esr":{"value":1442840704,"description":" Address size fault"},"pc":{"value":6675039656},"far":{"value":4381999112}}},{"id":3816,"frames":[{"imageOffset":42408,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}],"threadState":{"x":[{"value":6105493504},{"value":0},{"value":6104956928},{"value":0},{"value":278532},{"value":18446744073709551615},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0}],"flavor":"ARM_THREAD_STATE64","lr":{"value":0},"cpsr":{"value":4096},"fp":{"value":0},"sp":{"value":6105493504},"esr":{"value":0,"description":" Address size fault"},"pc":{"value":6675039656},"far":{"value":0}}},{"id":3817,"frames":[{"imageOffset":42408,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}],"threadState":{"x":[{"value":6106066944},{"value":0},{"value":6105530368},{"value":0},{"value":278532},{"value":18446744073709551615},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0},{"value":0}],"flavor":"ARM_THREAD_STATE64","lr":{"value":0},"cpsr":{"value":4096},"fp":{"value":0},"sp":{"value":6106066944},"esr":{"value":0,"description":" Address size fault"},"pc":{"value":6675039656},"far":{"value":0}}}],

  "usedImages" : [

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 4368334848,

    "size" : 2555904,

    "uuid" : "88a37db3-f143-3e23-92f5-77b5ed076089",

    "path" : "\/System\/Library\/PrivateFrameworks\/SignalTransmissionKit.framework\/SignalTransmissionKit",

    "name" : "SignalTransmissionKit"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 4377657344,

    "size" : 1261568,

    "uuid" : "81b33bb0-1d74-36e8-b91f-c2e21b1ff2af",

    "path" : "\/System\/Library\/PrivateFrameworks\/Kinematics.framework\/Kinematics",

    "name" : "Kinematics"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 4379361280,

    "size" : 147456,

    "uuid" : "ad33bc06-20f2-395e-8f67-02c6d2580013",

    "path" : "\/System\/Library\/PrivateFrameworks\/KinematicsGeometryTypes.framework\/KinematicsGeometryTypes",

    "name" : "KinematicsGeometryTypes"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 4379656192,

    "size" : 98304,

    "uuid" : "32af86c0-f3c2-326a-b903-e6d1ec471177",

    "path" : "\/System\/Library\/PrivateFrameworks\/SignalTransmissionKitFlatBuffers.framework\/SignalTransmissionKitFlatBuffers",

    "name" : "SignalTransmissionKitFlatBuffers"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 4363091968,

    "size" : 49152,

    "uuid" : "5200896b-753f-302f-9997-166cba74d7b1",

    "path" : "\/System\/Library\/PrivateFrameworks\/Motif.framework\/peopleawarenessd",

    "name" : "peopleawarenessd"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 6675193856,

    "size" : 229352,

    "uuid" : "70d87587-2079-3e13-9d82-021bbdd12073",

    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",

    "name" : "libsystem_kernel.dylib"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 6674997248,

    "size" : 49144,

    "uuid" : "502b9ad8-ca7c-329b-bd98-e18e1c91cd3b",

    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",

    "name" : "libsystem_pthread.dylib"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 6677815296,

    "size" : 507892,

    "uuid" : "b8ecae9f-fe7c-3592-a612-092f02bb9cb9",

    "path" : "\/usr\/lib\/system\/libsystem_c.dylib",

    "name" : "libsystem_c.dylib"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 6694952960,

    "size" : 5472256,

    "uuid" : "6ebde0d1-53d4-3ed8-878e-a2406fc10e89",

    "path" : "\/usr\/lib\/swift\/libswiftCore.dylib",

    "name" : "libswiftCore.dylib"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 7775977472,

    "size" : 1736704,

    "uuid" : "76c1d77b-5c1e-3cf2-a186-a9436537d324",

    "path" : "\/System\/Library\/PrivateFrameworks\/Motif.framework\/Motif",

    "name" : "Motif"

  },

  {

    "source" : "P",

    "arch" : "arm64e",

    "base" : 6673596416,

    "size" : 516028,

    "uuid" : "74aabb1c-0b06-34c2-8115-36c02a76fed3",

    "path" : "\/usr\/lib\/dyld",

    "name" : "dyld"

  },

  {

    "size" : 0,

    "source" : "A",

    "base" : 0,

    "uuid" : "00000000-0000-0000-0000-000000000000"

  }

],

  "sharedCache" : {

  "base" : 6672760832,

  "size" : 2263433216,

  "uuid" : "2d08b045-fe1e-3bd8-b3d6-7f4507eb01c9"

},

  "vmSummary" : "ReadOnly portion of Libraries: Total=695.5M resident=0K(0%) swapped_out_or_unallocated=695.5M(100%)\nWritable regions: Total=45.6M written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=45.6M(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nActivity Tracing                   256K        1 \nDispatch continuations            6144K        1 \nKernel Alloc Once                   32K        1 \nMALLOC                            36.1M       13 \nMALLOC guard page                   64K        4 \nSTACK GUARD                         80K        5 \nStack                             3184K        5 \n__AUTH                            1522K      176 \n__AUTH_CONST                      18.6M      457 \n__CTF                               824        1 \n__DATA                            7754K      451 \n__DATA_CONST                      21.2M      463 \n__DATA_DIRTY                      4408K      415 \n__FONT_DATA                        2352        1 \n__INFO_FILTER                         8        1 \n__LINKEDIT                       238.0M        6 \n__OBJC_RO                         51.6M        1 \n__OBJC_RW                         1531K        1 \n__TEXT                           457.5M      470 \ndyld private memory                272K        1 \nmapped file                         64K        1 \nshared memory                       96K        4 \n===========                     =======  ======= \nTOTAL                            847.9M     2479 \n",

  "legacyInfo" : {

  "threadTriggered" : {

    "queue" : "com.apple.main-thread"

  }

},

  "logWritingSignature" : "09b9e072c493543ff5a10c9734dc7a615b3d4c8b",

  "trialInfo" : {

  "rollouts" : [

  

  ],

  "experiments" : [

  

  ]

},

  "filteredLog" : [

  "Timestamp                         Type Thread  Act Process[pid] (Sender)",

  "2023-06-29 21:02:30.7769 -0700 default 0x005fd 0x0 sandboxd[102] (sandboxd): Telemetry is enabled.",

  "2023-06-29 21:02:33.4459 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): HTPrefs initialization",

  "2023-06-29 21:02:33.4486 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): HTPrefs: Refreshing preferences",

  "2023-06-29 21:02:33.4598 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): memoryLoggingInterval changed 0 -> 3600",

  "2023-06-29 21:02:33.4657 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Posting notification com.apple.hangtracer.htprefs.refreshed",

  "2023-06-29 21:02:33.4660 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Handling notification: com.apple.hangtracer.htprefs.refreshed",

  "2023-06-29 21:02:33.4666 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Memory Logging Enabled",

  "2023-06-29 21:02:33.4667 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Hang Tracer Daemon Enabled",

  "2023-06-29 21:02:33.4697 -0700 default 0x00aa9 0x0 hangtracerd[197] (hangtracerd): hangtracerd compiled without App Activation Logging",

  "2023-06-29 21:02:33.4697 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): EPL is not enabled by PLDE, and not enabled by profile, attempting to restore os_log state",

  "2023-06-29 21:02:33.4744 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Successfully validated profile payload",

  "2023-06-29 21:02:33.4757 -0700    info 0x00aa9 0x0 hangtracerd[197] (hangtracerd): Successfully removed profile payload",

  "2023-06-29 21:02:33.4759 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): XPC: Client started new connection: pid 39",

  "2023-06-29 21:02:33.4771 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): New proc: \/Applications\/PineBoard.app\/PineBoard(39)",

  "2023-06-29 21:02:33.4771 -0700 default 0x00b10 0x0 hangtracerd[197] (hangtracerd): Initialization complete now watching hangs for PineBoard(39) | UIKit-runloop",

  "2023-06-29 21:02:33.4772 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): XPC: Client started new connection: pid 204",

  "2023-06-29 21:02:33.4772 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): New proc: \/Applications\/BreadBoard.app\/BreadBoard(204)",

  "2023-06-29 21:02:33.4772 -0700 default 0x00b10 0x0 hangtracerd[197] (hangtracerd): Initialization complete now watching hangs for BreadBoard(204) | UIKit-runloop",

  "2023-06-29 21:02:33.4772 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): XPC: Client started new connection: pid 203",

  "2023-06-29 21:02:33.4773 -0700    info 0x00b10 0x0 hangtracerd[197] (hangtracerd): New proc: \/Applications\/TVSystemUIService.app\/TVSystemUIService(203)",

  "2023-06-29 21:02:33.4773 -0700 default 0x00b10 0x0 hangtracerd[197] (hangtracerd): Initialization complete now watching hangs for TVSystemUIService(203) | UIKit-runloop",

  "2023-06-29 21:02:34.4363 -0700 default 0x006e7 0x0 sandboxd[102] (sandboxd): Taking telemetry transaction.",

  "2023-06-29 21:02:36.7106 -0700   error 0x00649 0x0 sandboxd[102] (sandboxd): Sandbox: distnoted(91) deny(1) file-read-data \/private\/var\/empty...",

  "2023-06-29 21:02:36.7596 -0700   error 0x00649 0x0 sandboxd[102] (sandboxd): Sandbox: wifiFirmwareLoader(117) deny(1) iokit-set-properties iokit-class:AppleBCMWLANCore property:WiFiMSFSource...",

  "2023-06-29 21:02:36.8194 -0700   error 0x00649 0x0 sandboxd[102] (sandboxd): Sandbox: WirelessRadioManagerd(55) deny(1) file-write-create \/private\/var\/mobile\/tmp\/com.apple.WirelessRadioManager...",

  "2023-06-29 21:03:37.6801 -0700 default 0x00cfa 0x0 sandboxd[102] (sandboxd): telemetry_submit_events: 5",

  "2023-06-29 21:03:37.6817 -0700 default 0x00cfa 0x0 sandboxd[102] (sandboxd): Releasing telemetry transaction.",

  "2023-06-29 21:03:42.2649 -0700 default 0x00ee4 0x0 peopleawarenessd[322] (libxpc.dylib): [0xce2a06630] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon",

  "2023-06-29 21:03:42.2690 -0700 default 0x00ee4 0x0 peopleawarenessd[322] (SignalTransmissionKit): Connecting to remote switchboard",

  "2023-06-29 21:03:42.2695 -0700 default 0x00ee4 0x0 peopleawarenessd[322] (libxpc.dylib): [0xce2806380] activating connection: mach=true listener=false peer=false name=com.apple.sigmond",

  "2023-06-29 21:03:42.2711 -0700 default 0x00ee4 0x0 peopleawarenessd[322] (libswiftCore.dylib): generic witness table at 0x1cf939a7c contains out-of-bounds requirement descriptor 0xbad4007"

]

}