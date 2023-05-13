from setuptools import setup
from glob import glob


package_name = 'teleopkeys_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch/", glob("launch/*launch*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='filipe',
    maintainer_email='filipe.almeida.18@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleopkeys_publisher = teleopkeys_publisher.__init__:main'
        ],
    },
)
