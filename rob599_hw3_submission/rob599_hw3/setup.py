from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rob599_hw3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'resource'), glob('resource/*[.yaml,.pgm]')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aliclara',
    maintainer_email='jonesal9@oregonstate.edu',
    description='TODO: Package description',
    license='GPT-3.0-only',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'places = rob599_hw3.places:main'
        ],
    },
)