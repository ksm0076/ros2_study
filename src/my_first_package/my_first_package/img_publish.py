import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.bridge = CvBridge()
        self.image_path = "/home/ksm/ros2_study/test.jpg"  # 전달할 이미지 파일 경로
        self.image = cv2.imread(self.image_path)  # OpenCV로 이미지 로드
        
        if self.image is None:
            self.get_logger().error(f"Failed to load image at path: {self.image_path}")
        else:
            self.get_logger().info(f"Successfully loaded image at path: {self.image_path}")

    def timer_callback(self):
        # OpenCV 이미지를 ROS 이미지 메시지로 변환
        ros_image = self.bridge.cv2_to_imgmsg(self.image, "bgr8")
        self.publisher_.publish(ros_image) # 이미지 발행
        self.get_logger().info('Publishing image')

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
