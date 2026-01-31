(base) rc2@rc-2:~/jwt$ conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize interface/srv/Relocalize \
"{pcd_path: '/home/rc2/jwt/rc/work1_relocation/sources/map2/map.pcd', x: -6, y: 0, z: 0.0, yaw: 0.0, pitch: 0.0, roll: 0.0}"
requester: making request: interface.srv.Relocalize_Request(pcd_path='/home/rc2/jwt/rc/work1_relocation/sources/map2/map.pcd', x=-6.0, y=0.0, z=0.0, yaw=0.0, pitch=0.0, roll=0.0)

response:
interface.srv.Relocalize_Response(success=True, message='relocalize success')

(ros2) rc2@rc-2:~/jwt/rc/work1_relocation/r1_lio_ws$ conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize interface/srv/Relocalize \
"{pcd_path: '/home/rc2/jwt/rc/work1_relocation/sources/map2/map.pcd', x: 0.0, y: 0.0, z: 0.0, yaw: 0.0, pitch: 0.0, roll: 0.0}"
requester: making request: interface.srv.Relocalize_Request(pcd_path='/home/rc2/jwt/rc/work1_relocation/sources/map2/map.pcd', x=0.0, y=0.0, z=0.0, yaw=0.0, pitch=0.0, roll=0.0)

response:
interface.srv.Relocalize_Response(success=True, message='relocalize success')

/home/rc2/jwt/rc/work1_relocation/NOTE/log.md


- Matrix:
 -0.043  0.999 -0.013 -0.095
 -0.999 -0.044 -0.004 -5.388
 -0.005  0.013  1.000 -0.046
  0.000  0.000  0.000  1.000
At time 1769086205.81234931
- Translation: [-0.095, -5.388, -0.046]
- Rotation: in Quaternion (xyzw) [0.006, -0.003, -0.722, 0.692]
- Rotation: in RPY (radian) [0.013, 0.005, -1.614]
- Rotation: in RPY (degree) [0.730, 0.275, -92.493]
- Matrix:
 -0.043  0.999 -0.013 -0.095
 -0.999 -0.044 -0.004 -5.388
 -0.005  0.013  1.000 -0.046
  0.000  0.000  0.000  1.000
At time 1769086205.81234931
- Translation: [-0.095, -5.388, -0.046]
- Rotation: in Quaternion (xyzw) [0.006, -0.003, -0.722, 0.692]
- Rotation: in RPY (radian) [0.013, 0.005, -1.614]
- Rotation: in RPY (degree) [0.730, 0.275, -92.493]
- Matrix:
 -0.043  0.999 -0.013 -0.095
 -0.999 -0.044 -0.004 -5.388
 -0.005  0.013  1.000 -0.046
  0.000  0.000  0.000  1.000


At time 1769157380.545486450
- Translation: [-0.068, -0.465, 0.021]
- Rotation: in Quaternion (xyzw) [0.004, -0.005, 0.008, 1.000]
- Rotation: in RPY (radian) [0.009, -0.010, 0.016]
- Rotation: in RPY (degree) [0.510, -0.591, 0.929]
- Matrix:
  1.000 -0.016 -0.010 -0.068
  0.016  1.000 -0.009 -0.465
  0.010  0.009  1.000  0.021
  0.000  0.000  0.000  1.000
At time 1769157381.545330762
- Translation: [-0.066, -0.449, 0.024]
- Rotation: in Quaternion (xyzw) [0.004, -0.005, 0.007, 1.000]
- Rotation: in RPY (radian) [0.009, -0.011, 0.013]
- Rotation: in RPY (degree) [0.502, -0.608, 0.757]
- Matrix:
  1.000 -0.013 -0.010 -0.066
  0.013  1.000 -0.009 -0.449
  0.011  0.009  1.000  0.024
  0.000  0.000  0.000  1.000