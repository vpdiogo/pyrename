from setuptools import setup


setup(
    name = 'pyrename',
    version = '0.1.0',
    packages = ['app'],
    entry_points = {
        'console_scripts': [
            'pyren = app.__main__:main'
        ]
    })
