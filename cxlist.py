#!/usr/bin/python

# Print all combins of Xn from 1 to 6.
# Add all values to be minimised to a list and then take min of list.
# JM Wed  8 Jun 2016 11:33:35 BST

import itertools

X1list = [ 'a', 'b', 'c' ] 
X2list = [ 'd', 'e', 'f' ] 
X3list = [ 'g', 'h', 'j' ] 

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list 
}

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
	print 'List:', XvalList, 'LX:', len( XvalList)
	'''
	for n in range( len( XvalList) ):
		print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )

	'''
	# XVL is the list of combins from XvalList
	# XVLCD is the individual combin from XVL 
	for XVL in XvalList:
		print 'XVL:', XVL
		for XVLCD in ( XVL ):
			#print 'XVLCD :', XVLCD 
			#print 'CD:', column_dict[ XVLCD ], 'Len CD:', len( column_dict[ XVLCD ] ) 
			#print 'Letter:', column_dict[ XVLCD ][ 0 ]
			# need to process for elements 1 & 2 as well, in turn.

			Xlist_to_be_minimised = [ ]
			for n in range( 0, len( column_dict[ XVLCD ] ), 1 ):
				print 'XVLCD :', XVLCD , 'N:', n
				print 'Letter:',  column_dict[ XVLCD ][ n ] 
				#Xlist_to_be_minimised.append( column_dict[ XVLCD ][ n ] )
			#print 'CD Xlist:', Xlist_to_be_minimised
	print
		

#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3 ]


for Xindex in range( 1, 4 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
