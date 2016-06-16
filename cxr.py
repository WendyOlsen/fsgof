#!/usr/bin/python

# Print all combins of 1 from 6.
# Copy of cx.py with read of csv file added.
# JM 2016/06/07

from datetime import datetime
import itertools
import matplotlib.pyplot as plt
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

def plot_graph( xlist = [], ylist = [], pltitle = 'XY', Csuff = 0.0, fname = 'XY.png' ):
	MinXaxis =  float( min( xlist ) ) - 1.0
	MaxXaxis =  float( max( xlist ) ) + 1.0

	MinYaxis =  float( min( ylist ) ) - 1.00
	MaxYaxis =  float( max( ylist ) ) + 1.00
	'''
	Xmin = min ( MinXaxis , MinYaxis  )
	Ymin = Xmin
	Xmax = max( MaxXaxis , MaxYaxis  )
	Ymax = Xmax
	'''
	Xmin = 0.0
	Ymin = 0.0
	Xmax = 1.5
	Ymax = 1.5
	plt.title( pltitle )
	plt.xlabel( 'X' )
	plt.ylabel('Y1')

	#plt.axis( [ MinXaxis, MaxXaxis, MinYaxis, MaxYaxis ] )
	print 'XL:', xlist
	print 'YL:', ylist
	#print 'MXY:', MinXaxis, MaxXaxis, MinYaxis, MaxYaxis 
	#print 'XMin:', Xmin, 'Xmax:', Xmax, 'Ymin:', Ymin, 'Ymax:', Ymax

	#plt.plot( [ Ymin, Ymax ], 'k-', lw=2 )
	plt.plot( [ xlist ], [ ylist ], 'rD')
	#plt.plot( [ 0.0, 1.0 ], [ 0.0, 1.0 ], 'k-', lw=2 )
	plt.plot( [ Xmin, Xmax ], [ Ymin, Ymax ], 'k-', lw=2 )
	#plt.plot( [ MinXaxis, MaxXaxis ], [ MinYaxis, MaxYaxis ], 'k-', lw=2 )
	#plt.show( )
	print 'Fname:', fname
	plt.savefig( fname )
	plt.close()
	# Need to close to free up memory. Stops next slide being overwritten with previous slide data.


def proc_cons6(  XvalListn = [ ] ):
	print 'PC6:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5,x6 = XvalListn
	#print 'A,B,C,X,Y,Z:', x1,x2,x3,x4,x5,x6
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 ) + str( x6 ) + 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'LCD:', LCD
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		#print 'ForX5:', column_dict[ x5 ][ LCD ] 
		#print 'ForX6:', column_dict[ x6 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				   column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ], 
				   column_dict[ y1 ][ LCD ] ) )
	print
	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + ',X' + str( x5 ) + ',X' + str( x6 ) + ' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )

def proc_cons5(  XvalListn = [ ] ):
	print 'PC5:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5 = XvalListn
	#print 'A,B,X,Y,Z:', x1,x2,x3,x4,x5
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 )+ 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		#print 'ForX5:', column_dict[ x5 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ y1 ][ LCD ] ) )
	print
	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) +',X' + str( x5 ) + ' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )

def proc_cons4(  XvalListn = [ ] ):
	print 'PC4:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4 = XvalListn
	#print 'A,X,Y,Z:', x1,x2,x3,x4
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				   column_dict[ x4 ][ LCD ], column_dict[ y1 ][ LCD ] ) )
	print
	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + ' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )



def proc_cons3(  XvalListn = [ ] ):
	print 'PC3:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3 = XvalListn
	#print 'X,Y,Z:', x1,x2,x3
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:', column_dict[ x1 ][ LCD ] 
		#print 'ForY:', column_dict[ x2 ][ LCD ] 
		#print 'ForZ:', column_dict[ x3 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
		                   column_dict[ y1 ][ LCD ] ) )
	print
	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 ) +' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )


def proc_cons2(  XvalListn = [ ] ):
	print 'PC2List:', XvalListn, 'LX:', len( XvalListn )
	x1,x2 = XvalListn
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:', column_dict[ x1 ][ LCD ] 
		#print 'ForY:', column_dict[ x2 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ y1 ][ LCD ] ) )
	print
	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Minimum of X' + str( x1 ) + ',X' + str( x2 ) +' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )


def proc_cons1(  XvalListn = [ ] ):
	print 'PC1:', XvalListn, 'LX:', len( XvalListn )
	## Setting x to XvalListn doesn't work. Cos it's a tuple ???
	## Must set x, = XvalListn as XvalListn is a tuple. Feature !!
	x1, = XvalListn
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + 'Y1.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:',  column_dict[ x1 ][ LCD ] 
		#print 'ForY:',  column_dict[ y1 ][ LCD ] 
		#print 'MIN:', min( column_dict[ x1 ][ LCD ], column_dict[ y1 ][ LCD ] )
		#print 'ForX:',  column_dict[ XvalListn[ 0 ] ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ y1 ][ LCD ] ) 
		CsuffDen +=  column_dict[ x1 ][ LCD ]
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ y1 ][ LCD ] ) )
	print
	#print 'xlist_plot:', xlist_plot 
	#print 'ylist_plot:', column_dict[ y1 ]
	pltitle = 'Minimum of X' + str( x1 ) +' &Y1; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ y1 ], pltitle, Csuff, fname )
	
def proc_cons(  XvalList = [ ] ):
	#print 'List:', XvalList, 'LX:', len( XvalList)
	for n in range( len( XvalList) ):
		#print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )
		if ( len( XvalList[ n ] ) == 1 ):
			print 'Call ONE'
			proc_cons1(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 2 ):
			print 'Call TWO'
			proc_cons2(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 3 ):
			print 'Call THREE'
			proc_cons3(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 4 ):
			print 'Call FOUR'
			proc_cons4(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 5 ):
			print 'Call FIVE'
			proc_cons5(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 6 ):
			print 'Call SIX'
			proc_cons6(  XvalList[ n ] )						
	print
		

#***************************************************************
print 'Start:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')

read_file()
#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3,4,5,6 ]

y1 = 7
y2 = 8
y3 = 9
y4 = 10

for Xindex in range( 1, len(varlist) + 1 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
