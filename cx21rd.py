#!/usr/bin/python

# Print all combins of Xn from 1 to 6.
# Add all values to be minimised to a list and then take min of list.
# JM Wed  8 Jun 2016 11:33:35 BST
# Finally ! Iterate by taking length of Xnlist, then list of keys.
# Now add read of file into dictionary.
## C-sufficient is sum( min(X1 to X6, Y1 ) ) / sum( min X1 to X6 )
# JM Thu  9 Jun 2016 13:17:15 BST

import itertools
import csv
import sys


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
1 : X1list ,
2 : X2list ,
3 : X3list ,
4 : X4list ,
5 : X5list ,
6 : X6list ,
7 : Y1list
}


def read_file():
	with open( fname, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			linelist = list( row )			
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



def proc_cons(  XvalList = [ ] ):
	print 'List:', XvalList, 'LX:', len( XvalList)
	# XVL is the list of combins from XvalList
	# XVLCD is the individual combin from XVL 
	for XVL in XvalList:
		#print 'XVL:', XVL
		for n in range( 0, len( column_dict[ 1 ] ), 1 ):
			Xlist_to_be_minimised = [ ]
			for XVLCD in ( XVL ):
				#print 'N:', n, 'XVLCD:', XVLCD
				#print 'Letter:',  column_dict[ XVLCD ][ n ] ,
				Xlist_to_be_minimised.append(  column_dict[ XVLCD ][ n ] )
			print
			print 'List:', Xlist_to_be_minimised 
		print 'New Xvl:', XVL, 'XVLCD:', XVLCD 


read_file()
#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3,4,5,6 ]


for Xindex in range( 1, len( varlist ) + 1, 1 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
