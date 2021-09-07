import os
from glob import glob
from setuptools import setup

package_name = 'ros2-foxy-wearable-biosensors'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='purdue-ucsc',
    maintainer_email='wonsu0513@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #'Emotiv_Insight_Node = ros2-foxy-wearable-biosensors.emotiv_insight_node:main',
            'Empatica_E4_Node = ros2-foxy-wearable-biosensors.empatica_e4.empatica_e4_node:main',
        ],
    },
)
