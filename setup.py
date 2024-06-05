from setuptools import setup

setup(
    name='parameterization',
    version='0.1.0',
    py_modules=['calculate_volume', 'main'],
    entry_points={
        'console_scripts': [
            'parameterization=main:main',
        ],
    },
    install_requires=[],
    tests_require=['unittest'],
)
