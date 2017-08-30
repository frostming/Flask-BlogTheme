from setuptools import setup
import re

with open('flask_ymlconf.py', 'r') as f:
    version = re.search(r'__version__\s*=\s*[\'"](.+)[\'"]', f.read()).group(1)

setup(
    name='Flask-YmlConf',
    version=version,
    description='Flask extension to read _config.yml files like Jekyll',
    author='Frost Ming',
    author_email='mianghong@gmail.com',
    url='https://github.com/frostming/Flask-YmlConf',
    module=['flask_ymlconf'],
    install_requires=['pyyaml'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
