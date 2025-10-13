---
aliases: 
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
tags: []
---


---

Related: [[archive/edr/google3 storage]]

Can inspect individual sstable entries, header etc by pointing it to [[archive/edr/gqui]], [example](https://gqui.corp.google.com/?q=from%20%2Fcns%2Fix-d%2Fhome%2Fx-proxy-ml%2Ffelixgeyer%2Flogs%2Fl_shape_rotation%2Fblue.hilo.StereoAndRobotStateProto-00000000.sstable%20limit%2010).

Sample query:
`from /cns/ix-d/home/x-proxy-ml/felixgeyer/logs/l_shape_rotation/blue.hilo.StereoAndRobotStateProto-00000000.sstable limit 10`

To get subsets of the message:
`from /placer/prod/home/x-proxy-logs/robot_logs/ipc/data/2020/09/02/meta035/f0ec3152-bb61-42f7-8b93-5c8ead58d886/2020-09-02T13h31m17.890368594-0700_mma_meta035_meta/derived_best_effort/stereo_output/blue.hilo.StereoAndRobotStateProto-00000000.sstable print header limit 10`
