#!/usr/bin/python

# Print all combins of 2 from 6.
# Now include Y combins as well.
# JM Sat 11 Jun 2016 15:06:27 BST

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

	
def proc_cons(  XvalList = [ ] ):
	#print 'List:', XvalList, 'LX:', len( XvalList)
	for n in range( len( XvalList) ):
		print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )
	print
		

#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
xvarlist = [ 1,2,3 ]
yvarlist = [ 1,2,3 ]


for Xindex in range( 1, 4 ):
	XvalList = list( itertools.combinations( xvarlist, Xindex ) )
	print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
for Yindex in range( 1, len( yvarlist ) + 1, 1 ):
	YvalList = list( itertools.combinations( yvarlist, Yindex ) )
	print 'List:', YvalList, 'LY:', len( YvalList)
	print



