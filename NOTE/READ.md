export CMAKE_PREFIX_PATH=~/jwt/rc/work1_relocation/relies/_install:$CMAKE_PREFIX_PATH -->>rcenv



rcenv
<!-- source /opt/ros/humble/setup.sh -->
source install/setup.bash


bash ./build.sh humble

配置有线ip
sudo nmcli connection add type ethernet ifname enp4s0 con-name enp4s0-static \
  ipv4.method manual \
  ipv4.addresses 192.168.1.5/24 \
  ipv4.gateway 192.168.1.1

sudo nmcli connection modify enp4s0-static \
  ipv4.dns "192.168.1.1 8.8.8.8" \
  ipv4.ignore-auto-dns yes

**判断是否成功**
nmcli device status

**重定位全流程**
1. 启动基础节点
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 launch livox_ros_driver2 msg_MID360_launch.py

2. 建图节点（只有建图时候需要）
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 launch pgo pgo_launch.py

- 调用建图服务保存，注意路径必须存在 
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /pgo/save_maps interface/srv/SaveMaps "{file_path: '/home/rc2/jwt/rc/work1_relocation/sources/map6', save_patches: true}"

3. 重定位，启动重定位节点
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 launch localizer localizer_launch.py

**- 调用重定位服务(remember to confirm pcd file !!!!)**

conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize interface/srv/Relocalize \
"{pcd_path: '/home/rc2/jwt/rc/work1_relocation/sources/map6/map.pcd', x: 0.0, y: 0.0, z: 0.0, yaw: 0.0, pitch: 0.0, roll: 0.0}"
ros2 service call /localizer/relocalize_check interface/srv/IsValid "{code: 0}"

conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize interface/srv/Relocalize \
"{pcd_path: '/home/rc2/jwt/rc/work1_relocation/sources/map2/map.pcd', x: 0, y: 0, z: 0.0, yaw: 180, pitch: 0.0, roll: 0.0}"




- 检查重定位是否成功
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize_check interface/srv/IsValid "{code: 0}"

4. debug 
ros2 launch fastlio2 lio_launch.py


pcl_viewer map.pcd
ros2 topic info -v /tf_static
ros2 topic info -v /tf

ros2 topic echo /tf  
 - best way to read tf directly

ros2 run tf2_tools view_frames
 - equal to rqt tf-tree but with HZ,so why not rqt

conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 run tf2_ros tf2_echo map lidar 
 - can directly read two tf ,good good good

fazuobiao
conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 run tf2_ros tf2_echo init base_link


5. static_tf
conda activate ros2
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
source install/setup.bash
ros2 launch my_static_tf lidar_to_base.launch.py

ros2 launch my_static_tf map_to_init.launch.py



cd /home/rc2/jwt/rc/autostart
./start_all_terminals.sh

conda activate ros2
cd /home/rc2/jwt/rc/work1_relocation/sources/scripts
python monitor_map_body.py


conda activate ros2
cd /home/rc2/jwt/rc/work1_relocation/sources/scripts
python monitor_tf.py

ros2 run plotjuggler plotjuggler

<!-- conda activate ros2
colcon build --packages-select my_static_tf -->

删除wifi
nmcli connection show
sudo nmcli connection delete "Robocon_5G"
sudo nmcli connection delete "Robocon_Wi-Fi5"
sudo nmcli connection delete "XJTU_STU"
sudo nmcli connection modify "Redmi Note 12 Turbo" connection.permissions ""

sudo nmcli connection modify "Robocon_5G" connection.autoconnect yes
sudo nmcli connection modify "Robocon_5G" connection.autoconnect-priority 50

测速：
curl -L http://speed.cloudflare.com/__down?bytes=100000000 -o /dev/null

CloudCompare:
https://github.com/CloudCompare/CloudCompare/releases/tag/v2.13.2




(base) rc2@rc-2:~/jwt/rc/work1_relocation/r1_lio_ws$ conda activate ros2
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/jwt/rc/work1_relocation/relies/_install/lib:$LD_LIBRARY_PATH
cd /home/rc2/jwt/rc/work1_relocation/r1_lio_ws
. ./install/setup.bash
ros2 service call /localizer/relocalize_check interface/srv/IsValid "{code: 0}"
requester: making request: interface.srv.IsValid_Request(code=0)

response:
interface.srv.IsValid_Response(valid=False)


/home/rc2/jwt/rc/autostart/serial_driver.sh