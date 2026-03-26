from setuptools import find_packages, setup

package_name = 'my_turtle_package'

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
    maintainer='anas',
    maintainer_email='anas-gulzar-dev@users.noreply.github.com',
    description='Turtlesim control nodes for lab patterns and goal navigation',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_node = my_turtle_package.my_node:main',
            'move_turtle = my_turtle_package.move_turtle:main',
            'multi_turtle_patterns = my_turtle_package.multi_turtle_patterns:main',
            'move_to_goal = my_turtle_package.move_to_goal:main',
        ],
    },
)
