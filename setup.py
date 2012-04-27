import os

from distutils.core import setup


repodir = os.path.dirname(os.path.realpath(__file__))
readme = open(os.path.join(repodir, 'README.rst'))

version = '1.0.a1'
longdesc = readme.read()
classifiers=['Environment :: Console',
             'Operating System :: OS Independent',
             'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
             'Programming Language :: Python :: 2.4',
             'Programming Language :: Python :: 2.5',
             'Programming Language :: Python :: 2.6',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.0',
             'Programming Language :: Python :: 3.1',
             'Programming Language :: Python :: 3.2',
             'Intended Audience :: End Users/Desktop',
             'Intended Audience :: Developers',
             'Intended Audience :: System Administrators']
readme.close()

setup(name='awake',
      version=version,
      author='Joel Rivera',
      author_email='rivera@joel.mx',
      maintainer='Joel Rivera',
      maintainer_email='rivera@joel.mx',
      url='http://github.com/cyraxjoe/awake',
      download_url='http://github.com/cyraxjoe/awake/tarball/v%s' % version,
      license='GPLv3',
      package_dir={'': 'src'},
      scripts=['bin/awake.py',],
      packages=['awakelib',],
      provides=['awake',],
      classifiers=classifiers,
      platforms=['linux2', 'win32', 'cygwin', 'darwin'],
      description='Command line program/library to wake-on-lan a remote host.',
      long_description=longdesc)
