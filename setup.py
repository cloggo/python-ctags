from distutils.core import setup
from distutils.command import build, clean
from distutils.extension import Extension
import os, sys, shutil

setup(
	name='ctags',
	version='1.0',
	description='python ctags bindings',
	author='Aaron H. K. Diep',
	author_email='hkdiep@gmail.com',
	packages = ['ctags'],
	ext_package='ctags',
	ext_modules=[Extension(
						'_readtags', ['src/readtags.c', 'src/_readtags.c'],
						 include_dirs=['src/include']
						)],
	package_dir = {'ctags' : 'src/ctags'}
	
	)