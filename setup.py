import os
import sys
import platform
from setuptools import setup, find_packages
from os.path import join, dirname

# copied from electrum project
data_files = []
if platform.system() == 'Linux':
    usr_share = os.path.join(sys.prefix, 'share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['somebar.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['somebar.xpm']),
    ]


setup(
    name = 'somebar',
    scripts = ['somebar'],
    version = '0.0.7',
    license = 'MIT License',
    description = 'Simple taskbar widget that displays color dot or custom icon',
    author = 'Ivan',
    author_email = 'ivan.vershigora@gmail.com',
    url = 'https://github.com/limpbrains/somebar',
    download_url  ='https://github.com/limpbrains/somebar/tarball/0.0.7',
    keywords = ['AnyBar', 'somebar', 'taskbar', 'indicator'],
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
    ],
    package_data = {'somebar_icons' : ['*.png']},
    data_files = data_files,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires = [
        # 'gi'
    ],
)
