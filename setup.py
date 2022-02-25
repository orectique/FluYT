from setuptools import setup

setup(
    name='fluyt',
    version='0.0.1',
    packages=['fluyt'],
    install_requires=[
        'requests',
        'importlib; python_version > "3.5"',
        'PySide6',
        'youtube_dl',
        'shutil'
    ],
)