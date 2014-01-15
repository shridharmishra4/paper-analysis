#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  predictor.py
#  
#  Copyright 2014 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
"""the,
a,
an,
another,
no,
some,
any,
my,
our,
their,
her,
his,
its,
each,
every,
certain,
its,
this,
that
"""
def Black_list(word):#string has to be passed
	black_list=['the','a','an','another','no','some','any','my','our',
			  'their','her','his','its','each','every','certain','it',
			  'this','that','that', 'which','who', 'whom', 'whose',
			  'whichever', 'whoever', 'whomever','anybody', 'anyone', 
			  'anything', 'each', 'either', 'everybody', 'everyone',
			  'everything', 'neither', 'nobody', 'no one', 'nothing', 
			  'one', 'somebody', 'someone', 'something','both', 'few', 
			  'many','several','all', 'most', 'none', 'some','what']
	black_list.sort()
	if str(word) in black_list:
		return True
	else:
	    return False
				  
			
##print Black_list()	

def main():
	
	return 0

if __name__ == '__main__':
	main()

