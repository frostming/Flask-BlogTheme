from setuptools import setup
import re

with open('flask_blogtheme.py', 'r') as f:
    version = re.search(r'__version__\s*=\s*[\'"](.+)[\'"]', f.read()).group(1)

setup(
    name='Flask-BlogTheme',
    version=version,
    description='Flask extension to read switch theme easily',
    author='Frost Ming',
    author_email='mianghong@gmail.com',
    url='https://github.com/frostming/Flask-BlogTheme',
    module=['flask_blogtheme'],
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
