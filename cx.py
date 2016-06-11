#!/usr/bin/python

# Print all combins of 2 from 6.

import itertools

X1list = [ 'a', 'b', 'c' ] 
X2list = [ 'd', 'e', 'f' ] 
X3list = [ 'g', 'h', 'j' ] 

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list 
}


#'L:', len( column_dict[ I ] ),

def proc_cons3(  XvalListn = [ ] ):
	print 'PC3:', XvalListn, 'LX:', len( XvalListn )
	x,y,z = XvalListn
	print 'X,Y,Z:', x,y,z
	for LCD in range( 0, len( column_dict[ x ] ), 1 ):
		print 'ForX:', column_dict[ x ][ LCD ] 
		print 'ForY:', column_dict[ y ][ LCD ] 
		print 'ForZ:', column_dict[ z ][ LCD ] 
	print


def proc_cons2(  XvalListn = [ ] ):
	print 'PC2List:', XvalListn, 'LX:', len( XvalListn )
	x,y = XvalListn
	print
	for LCD in range( 0, len( column_dict[ x ] ), 1 ):
		print 'ForX:', column_dict[ x ][ LCD ] 
		print 'ForY:', column_dict[ y ][ LCD ] 
	print


def proc_cons1(  XvalListn = [ ] ):
	print 'PC1:', XvalListn, 'LX:', len( XvalListn )
	## Setting x to XvalListn doesn't work. Cos it's a tuple ???
	## Must set x, = XvalListn as XvalListn is a tuple. Feature !!
	x, = XvalListn
	for LCD in range( 0, len( column_dict[ x ] ), 1 ):
		print 'ForX:',  column_dict[ x ][ LCD ] 
		#print 'ForX:',  column_dict[ XvalListn[ 0 ] ] 
	print
	
def proc_cons(  XvalList = [ ] ):
	#print 'List:', XvalList, 'LX:', len( XvalList)
	for n in range( len( XvalList) ):
		print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )
		if ( len( XvalList[ n ] ) == 1 ):
			proc_cons1(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 2 ):
			proc_cons2(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 3 ):
			proc_cons3(  XvalList[ n ] )			
	print
		

#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3 ]


for Xindex in range( 1, 4 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
