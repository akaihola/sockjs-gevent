import os
from setuptools import setup, find_packages

version='0.1dev'

install_requires = [
    'greenlet==0.3.4',
    'setuptools',
    'gevent==0.13.6',
    'gevent-websocket==0.3.0',
]

tests_require = install_requires + ['nose==1.1.2',
                                    'unittest2==0.5.1',
                                    # ws4py from GitHub
                                    # Websocket-for-Python from GitHub
                                    ]

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

setup(name='gevent-sockjs',
      version=version,
      description=('gevent base sockjs server'),
      long_description='\n\n'.join((read('README.md'), read('CHANGES.txt'))),
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Internet :: WWW/HTTP",
          'Topic :: Internet :: WWW/HTTP :: WSGI'],
      author='Stephen Diehl',
      author_email='stephen.m.diehl@gmail.com',
      url='https://github.com/sdiehl/sockjs-gevent',
      license='MIT',
      packages=find_packages(),
      install_requires = install_requires,
      tests_require = tests_require,
      test_suite = 'nose.collector',
      include_package_data = True,
      zip_safe = False,
      entry_points = {
          'console_scripts': [
              'sockjs-server = gevent_sockjs.server:main',
              ],
          },
      )
