from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name = 'somebar',
    scripts = ['somebar'],
    version = '0.0.2',
    license = 'MIT License',
    description = 'Simple taskbar widget that displays color dot or custom icon',
    author = 'Ivan',
    author_email = 'ivan.vershigora@gmail.com',
    url = 'https://github.com/limpbrains/somebar',
    download_url  ='https://github.com/limpbrains/somebar/tarball/0.0.2',
    keywords = ['AnyBar', 'somebar', 'taskbar', 'indicator'],
    packages = find_packages(),
    long_description = open(join(dirname(__file__), 'README.md')).read(),
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
    ],
    package_data = {'somebar_icons' : ['*.png']},
    install_requires = [
        # 'gi'
    ],
)
