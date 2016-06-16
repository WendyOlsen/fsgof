#!/usr/bin/python

import itertools


def proc_cons(  XvalList = [ ] ):
	for XVL in ( XvalList):
		#print 'List:', XvalList, 'LX:', len( XvalList)
		print 'XVL:', XVL

varlist = [ 1,2,3,4,5,6 ]

for Xindex in range( 1, len(varlist) + 1 ):
        XvalList = list( itertools.combinations( varlist, Xindex ) )
        #print 'List:', XvalList, 'LX:', len( XvalList)
        proc_cons( XvalList ) 

