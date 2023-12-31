from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'test_docking'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marzan',
    maintainer_email='marzanalam3@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           # 'apriltag_port = test_docking.apriltag_port:main',
            'apriltag_port_server = test_docking.docking_server:main',
            'apriltag_port_client = test_docking.docking_client:send_docking_goal',
            'apriltag_port = test_docking.docking_main:main',
        ],
    },
)
