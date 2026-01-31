import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
from geometry_msgs.msg import PointStamped

class TFMonitor(Node):
    def __init__(self):
        super().__init__('tf_monitor_plotter')
        
        # --- 配置区域 ---
        # 你想看 谁 相对于 谁 的抖动？
        self.target_frame = 'init'      # 世界坐标系（参考系/父）
        self.source_frame = 'base_link' # 机器人坐标系（移动物体/子）
        # ----------------
        
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # 发布一个话题给 PlotJuggler 看
        self.pub = self.create_publisher(PointStamped, '/monitor/position', 10)
        
        # 50Hz 的频率，捕捉高频抖动
        self.timer = self.create_timer(0.02, self.timer_callback)
        
        self.get_logger().info(f"开始监听 TF: {self.target_frame} <--- {self.source_frame}")

    def timer_callback(self):
        try:
            # 核心：让 ROS 帮我们计算复杂的变换关系
            t = self.tf_buffer.lookup_transform(
                self.target_frame,
                self.source_frame,
                rclpy.time.Time()) # 获取最新时刻
            
            # 把结果打包发出去
            msg = PointStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.point.x = t.transform.translation.x
            msg.point.y = t.transform.translation.y
            msg.point.z = t.transform.translation.z
            
            self.pub.publish(msg)
            
        except Exception as e:
            # 刚启动时可能没连上，这是正常的，不报错
            pass

def main():
    rclpy.init()
    node = TFMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()