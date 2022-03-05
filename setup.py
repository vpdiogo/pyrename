from setuptools import setup


setup(
    name = 'pyrename',
    version = '0.1.0',
    packages = ['main'],
    entry_points = {
        'console_scripts': [
            'pyren = main.__main__:main'
        ]
    })
