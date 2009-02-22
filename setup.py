"""
Copyright (C) 2008 Aaron Diep <ahkdiep@gmail.com>

This file is part of Python-Ctags.

Python-Ctags is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Python-Ctags is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Python-Ctags.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup
from distutils.command import build, clean
from distutils.extension import Extension
import os, sys, shutil

setup(
	name='python-ctags',
	version='1.0.2',
	description='python ctags bindings',
	author='Aaron H. K. Diep',
	author_email='ahkdiep@gmail.com',
	url='http://code.google.com/p/python-ctags/',
	packages = ['ctags'],
	ext_package='ctags',
	ext_modules=[Extension(
						'_readtags', ['src/readtags.c', 'src/_readtags.c'],
						 include_dirs=['src/include']
						)],
	package_dir = {'ctags' : 'src/ctags'}
	
	)
