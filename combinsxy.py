#!/usr/bin/python

# Show all combins of X1-6 & Y1-4.

import itertools

def proc_consxy( XvalList = [ ], YvalList = [ ] ):
	print 'YL:',XvalList  
	print 'XL:', YvalList 
	'''
	for XVL in ( XvalList):
		#print 'List:', XvalList, 'LX:', len( XvalList)
		print 'XVL:', XVL
	'''


def proc_cons(  XvalList = [ ] ):
	for XVL in ( XvalList):
		#print 'List:', XvalList, 'LX:', len( XvalList)
		print 'XVL:', XVL

Xvarlist = [ 1,2,3,4,5,6 ]
Yvarlist = [ 1,2,3,4 ]
'''
for Xindex in range( 1, len(Xvarlist) + 1 ):
        XvalList = list( itertools.combinations( Xvarlist, Xindex ) )
        #print 'List:', XvalList, 'LX:', len( XvalList)
        proc_cons( XvalList ) 

for Yindex in range( 1, len(Yvarlist) + 1 ):
        YvalList = list( itertools.combinations( Yvarlist, Yindex ) )
        #print 'List:', YvalList, 'LY:', len( YvalList)
        proc_cons( YvalList ) 
'''	
for Yindex in range( 1, len(Yvarlist) + 1 ):
        YvalList = list( itertools.combinations( Yvarlist, Yindex ) )
	for Xindex in range( 1, len(Xvarlist) + 1 ):
		XvalList = list( itertools.combinations( Xvarlist, Xindex ) )
		proc_consxy( XvalList, YvalList )
