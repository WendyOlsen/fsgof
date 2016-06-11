#!/usr/bin/env python

## Read in data from CSV file.
## Use Cress & Snow 2000 Data only.
## Set value of X from 1 to 6.
## C-sufficient is sum( min(X1 to X6, Y1 ) ) / sum( min X1 to X6 )
## JM Mon  2 May 2016 19:36:38 BST
## Read column lists into a dictionary in prep for iteration.
## JM 2016/06/03

import csv
import sys
import itertools

if ( len( sys.argv ) != 2 ):
        fname = 'cs2k.csv'
else:
	fname = sys.argv[ 1 ]

X0list = []
X1list = []
X2list = []
X3list = []
X4list = []
X5list = []
X6list = []
Y1list = []

column_dict = {
1 : X1list,
2 : X2list,
3 : X3list,
4 : X4list,
5 : X5list,
6 : X6list,
7 : Y1list
}

def read_file( ):

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
				#print 'Yerr:', linelist[ 7 ]
				pass

read_file()				
				
print 'CD1:', column_dict[ 1 ]
print 'LCD Tot:', len( column_dict )
print 'LCD1:', len( column_dict[ 1 ] )

LEN_CD = len( column_dict )
varlist = [ 1,2,3,4,5,6 ]

print 'V:', varlist, 'LV:', len( varlist )

## Range goes from 1 to n-1, so need to set our range to length + 1. Feature !!

for Xindex in range( 1, len( varlist ) + 1 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	print 'List:', XvalList, 'LX:', len( XvalList)
	print
	#proc_cons( XvalList ) 
	
	
	





