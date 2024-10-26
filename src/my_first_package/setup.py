from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ksm',
    maintainer_email='ksm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_first_package.my_first_node:main',
            'my_subscriber = my_first_package.my_subscriber:main',
            'my_publisher = my_first_package.my_publisher:main',
            'turtle_cmd_and_pose = my_first_package.turtle_cmd_and_pose:main',
            'my_service_server = my_first_package.my_service_server:main',
            'n_spawn_server = my_first_package.n_spawn:main',
            'my_action_server = my_first_package.my_action_server:main',
            'move_turtle_action_server = my_first_package.move_turtle:main',
            'user_defined_cmd = my_first_package.client_test:main',
            'test_action_server = my_first_package.test_action_server:main',
            'img_publish = my_first_package.img_publish:main',
            'img_subscribe = my_first_package.img_subscribe:main',
        ],
    },
)
