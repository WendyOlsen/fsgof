#!/usr/bin/python

# Print all combins of 1 from 6.
# Copy of cx.py with read of csv file added.
# JM 2016/06/07

import itertools
import csv
import sys


if ( len( sys.argv ) != 2 ):
        fname = 'cs2k.csv'
else:
	fname = sys.argv[ 1 ]
'''
X1list = [ 'a', 'b', 'c' ] 
X2list = [ 'd', 'e', 'f' ] 
X3list = [ 'g', 'h', 'j' ] 
X4list = [ 'k', 'l', 'm' ] 
X5list = [ 'n', 'o', 'p' ] 
X6list = [ 'q', 'r', 's' ] 
'''
X0list = []
X1list = []
X2list = []
X3list = []
X4list = []
X5list = []
X6list = []
Y1list = []

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list ,
4 : X4list ,
5 : X5list ,
6 : X6list ,
7 : Y1list
}

def read_file():
	# XvalMax is number of X columns to read.

	with open( fname, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			linelist = list( row )			
			#for Xlocal in range ( 1, XvalMax ):
			try:
				X0list.append( linelist[ 0 ] )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 0 ]
				pass
			try:
				X1list.append( float( linelist[ 1 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 1 ]
				pass
			try:
				X2list.append( float( linelist[ 2 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 2 ]
				pass
			try:
				X3list.append( float( linelist[ 3 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 3 ]
				pass
			try:
				X4list.append( float( linelist[ 4 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 4 ]
				pass
			try:
				X5list.append( float( linelist[ 5 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 5 ]
				pass
			try:
				X6list.append( float( linelist[ 6 ] ) )
				#print 'Xlist:', Xlist
			except:
				print 'XErr:',  linelist[ 6 ]
				pass			
			try:
				Y1list.append( float( linelist[ 7 ] ) )
			except:
				print 'Yerr:', linelist[ 7 ]
				pass



def proc_cons6(  XvalListn = [ ] ):
	print 'PC6:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5,x6 = XvalListn
	print 'A,B,C,X,Y,Z:', x1,x2,x3,x4,x5,x6
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'LCD:', LCD
		print 'ForX1:', column_dict[ x1 ][ LCD ] 
		print 'ForX2:', column_dict[ x2 ][ LCD ] 
		print 'ForX3:', column_dict[ x3 ][ LCD ] 
		print 'ForX4:', column_dict[ x4 ][ LCD ] 
		print 'ForX5:', column_dict[ x5 ][ LCD ] 
		print 'ForX6:', column_dict[ x6 ][ LCD ] 
	print

def proc_cons5(  XvalListn = [ ] ):
	print 'PC5:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5 = XvalListn
	print 'A,B,X,Y,Z:', x1,x2,x3,x4,x5
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'ForX1:', column_dict[ x1 ][ LCD ] 
		print 'ForX2:', column_dict[ x2 ][ LCD ] 
		print 'ForX3:', column_dict[ x3 ][ LCD ] 
		print 'ForX4:', column_dict[ x4 ][ LCD ] 
		print 'ForX5:', column_dict[ x5 ][ LCD ] 
	print

def proc_cons4(  XvalListn = [ ] ):
	print 'PC4:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4 = XvalListn
	print 'A,X,Y,Z:', x1,x2,x3,x4
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'ForX1:', column_dict[ x1 ][ LCD ] 
		print 'ForX2:', column_dict[ x2 ][ LCD ] 
		print 'ForX3:', column_dict[ x3 ][ LCD ] 
		print 'ForX4:', column_dict[ x4 ][ LCD ] 
	print



def proc_cons3(  XvalListn = [ ] ):
	print 'PC3:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3 = XvalListn
	print 'X,Y,Z:', x1,x2,x3
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'ForX:', column_dict[ x1 ][ LCD ] 
		print 'ForY:', column_dict[ x2 ][ LCD ] 
		print 'ForZ:', column_dict[ x3 ][ LCD ] 
	print


def proc_cons2(  XvalListn = [ ] ):
	print 'PC2List:', XvalListn, 'LX:', len( XvalListn )
	x1,x2 = XvalListn
	print
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'ForX:', column_dict[ x1 ][ LCD ] 
		print 'ForY:', column_dict[ x2 ][ LCD ] 
	print


def proc_cons1(  XvalListn = [ ] ):
	print 'PC1:', XvalListn, 'LX:', len( XvalListn )
	## Setting x to XvalListn doesn't work. Cos it's a tuple ???
	## Must set x, = XvalListn as XvalListn is a tuple. Feature !!
	x1, = XvalListn
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print 'ForX:',  column_dict[ x1 ][ LCD ] 
		#print 'ForX:',  column_dict[ XvalListn[ 0 ] ] 
	print
	
def proc_cons(  XvalList = [ ] ):
	#print 'List:', XvalList, 'LX:', len( XvalList)
	for n in range( len( XvalList) ):
		print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )
		if ( len( XvalList[ n ] ) == 1 ):
			proc_cons1(  XvalList[ n ] )
			print 'Call ONE'
		elif ( len( XvalList[ n ] ) == 2 ):
			proc_cons2(  XvalList[ n ] )
			print 'Call TWO'
		elif ( len( XvalList[ n ] ) == 3 ):
			proc_cons3(  XvalList[ n ] )			
			print 'Call THREE'
		elif ( len( XvalList[ n ] ) == 4 ):
			proc_cons4(  XvalList[ n ] )			
			print 'Call FOUR'
		elif ( len( XvalList[ n ] ) == 5 ):
			proc_cons5(  XvalList[ n ] )			
			print 'Call FIVE'
		elif ( len( XvalList[ n ] ) == 6 ):
			proc_cons6(  XvalList[ n ] )						
			print 'Call SIX'
	print
		


read_file()
#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3,4,5,6 ]


for Xindex in range( 1, len(varlist) + 1 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
