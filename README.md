# ROS2 기본

## 1. 노드
ros에서 다루는 프로세스
```
ros2 run <package_name> <node_name>
```

## 전체적인 명령 형식(절차)
1. 리스트 확인
2. 전달 인자 확인
3. 명령

## 2. 토픽
* 발행(Publish) - 구독(Subscribe)
* msg를 이용한 통신
* 비동기적
```
ros2 topic list -t
```
**출력**
```
<topic_name> <type_name>
```
**전달 인자 확인**
```
ros2 interface show <type_name>
```
**명령**
```
ros2 topic pub <topic_name> <type_name> <argument>
```

## 3. 서비스
* 요청(Request) - 응답(Response)
* srv를 이용한 통신
* 동기적 통신

1. 리스트 확인
```
ros2 service list -t
```
**출력**
```
<service_naeme> <type_name>
```
**명령**
```
rosw service call <service_name> <type_name> <argument>
```

## 4. 액션
* 상태 업데이트, 긴 시간이 걸리는 작업
* action을 이용한 통신

**명령**
```
ros action send_goal <action_name> <type_name> <argument>
```


## 5. colcon
> 기존 환경(underlay) 위에 overlay를 얹음 (python venv처럼 가상환경 느낌)

**colcon 설치**
```
sudo apt install python3-colcon-common-extensions
```
> 변경이 있을 시 build (워크스페이스의 홈에서)
```
colcon build
source install/local_setup.bash
```

## 6. 패키지 생성
**토픽, 서비스, 액션 등을 위한 패키지**
```
ros2 pkg create --build-type ament_python --node-name my_node <user_defined_package_name>
```
**메시지 정의를 위한 패키지**
```
ros2 pkg create --build-type ament_cmake <user_defined_package_name>
```

## 6.1 사용자 정의 토픽, 서비스, 액션 작성 방법 (파이썬 코드)
> 기초적인 import
```
import rclpy as rp
from rclpy.node import Node
```

## (Service)Client Example
service list -t 의 결과
```
/turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]
```

> client_test.py

> 메시지 타입을 사용하기 위한 import
```
form turtlesim.srv import TeleportAbsolute
```

```
class ClientTest(Node):
    def __init__(self):
        super().__init__('client_test') # node name
        self.teleport = self.create_client(
            TeleportAbsolute,
            '/turtle1/teleport_absolute'
        )
        self.req_teleport = TeleportAbsolute.Request()
        self.create_timer(1, self.callback_service)
        
    def callback_service(self):        
        self.req_teleport.x = float(random.randrange(1,8))
        self.teleport.call_async(self.req_teleport)
        print("Client Test GOGO!")
    
def main():
    rp.init()
    client_node = ClientTest()
    
    rp.spin(client_node)
    rp.shutdown()

if __name__ == 'main':
    main()
```

> setup.py 수정
```
entry_points={
        'console_scripts': [
            'user_defined_cmd = my_package_name.client_test:main',
        ],
    },
```

> 서비스 요청
```
ros2 run my_package user_defined_cmd
```



<details>
<summary>사용자 정의 서비스 작성 요령</summary>


> 파일명.py
```
def __init__(self):
    super().__init__('노드명')
    self.server = self.create_service(
        import한 메시지타입,
        '서비스명',
        self.콜백함수
    )
```

> setup.py
```
entry_points={
    'console_scripts': [
        '실행명' = 패키지명.파일명:main',
    ],
```

> 서비스 서버 실행
```
ros2 run <패키지명> <실행명>
```
> 서비스 콜
```
ros2 service call <서비스명> <메시지타입> <인자>
```
</details>


## 7. 메시지 정의
> ament_cmake로 생성한 my_first_package_msgs 패키지

msg 폴더 생성 -> 소스코드 만들기 -> package.xml, CMakeList.txt 파일 수정
> ros2_study/src/my_first_package_msgs/msg/CmdAndPoseVel.msg
```
float32 cmd_vel_linear
float32 cmd_vel_angular

float32 pose_x
float32 pose_y
float32 linear_vel
float32 angular_vel
```
> CMakeList.txt
```
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CmdAndPoseVel.msg"
)
```
> package.xml
```
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
명령어로 확인 (변화 있으면 colcon build 잊지 않기)
```
ros2 interface show my_first_package_msgs/msg/CmdAndPoseVel
```

내가 정의한 메시지 사용해보기 : msg 파일, [turtle_cmd_and_pose.py](https://github.com/ksm0076/ros2_study/blob/main/src/my_first_package/my_first_package/turtle_cmd_and_pose.py)

내가 정의한 서비스 메시지 사용해보기: srv파일, [n_spawn.py](https://github.com/ksm0076/ros2_study/blob/main/src/my_first_package/my_first_package/n_spawn.py)
