from setuptools import setup, find_packages

setup(
    name='RL-MANUFACTURING',
    version='0.1.0',
    author="Wenqing Hu",
    description='Joint Control of Manufacturing and Onsite Microgrid System via Novel Neural-Network Integrated Reinforcement Learning Algorithms',
    python_requires='=3.7',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=[
        'requests',
        'numpy',
    ],
)