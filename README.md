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
**명령**
```
ros2 topic pub <topic_name> <type_name> <argument>

<topic_name> <type_name> <argument>
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
**전달 인자 확인**
```
ros2 interface show <type_name>
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
> python venv처럼 가상환경 느낌 (ros에서의 오버레이)

**colcon 설치**
```
sudo apt install python3-colcon-common-extensions
```
