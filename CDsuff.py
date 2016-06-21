#!/usr/bin/python

# Print all combins of 1 from 6.
# Copy of cx.py with read of csv file added.
# JM 2016/06/07
# Copy of cxr.py.  
# JM 2016/06/16
## Add diff value of Y to be input. Y1 to Y4.
# Add in Dsuff calcs.
# JM Mon 20 Jun 2016 09:04:46 BST
# Add output table.
# JM Mon 20 Jun 2016 18:52:44 BST


from datetime import datetime
from scipy.stats import norm, f
import itertools
import matplotlib.pyplot as plt
import csv
import sys
import os

if ( len( sys.argv ) == 1 ):
	fname = 'cs2k.csv'
	Yval = 1
elif ( len( sys.argv ) == 2 ):
	fname = sys.argv[ 1 ]
	Yval = 1
elif ( len( sys.argv ) == 3 ):
	fname = sys.argv[ 1 ]
	Yval = int( sys.argv[ 2 ] )
else:
	fname = 'cs2k.csv'
	Yval = 1

if ( Yval > 4 ):
	# Can't allow Y to be more than four. Only four Y vals allowed.
	Yval = 1


# Add 6 to get correct offset. Y1 is column 7, etc. CD is short for column_dict. 
CDYval = Yval + 6

X0list = []
X1list = []
X2list = []
X3list = []
X4list = []
X5list = []
X6list = []
YNlist = []

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list ,
4 : X4list ,
5 : X5list ,
6 : X6list ,
CDYval  : YNlist
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
				YNlist.append( float( linelist[ CDYval ] ) )
			except:
				print 'Yerr:', linelist[ CDYval ]
				pass

#************** Dsuff Processing ************** 

def plot_zt_graph( xlist = [], ylist = [], pltitle = 'DXY', fname = 'DXY.png' ):
	Xmin = -3.0
	Ymin = -3.0
	Xmax =  3.0
	Ymax =  3.0

	#plt.figure( figsize=( 2, 2 ) ) 
	plt.title( pltitle )
	plt.xlabel( 'ZX' )
	plt.ylabel( 'ZY' + str( Yval ) )

	#print 'XL:', xlist
	#print 'YL:', ylist
	plt.plot( [ Xmin, Xmax ], [ Ymin, Ymax ], '--', lw=2 )
	plt.plot( [ xlist ], [ ylist ], 'rD', markersize=5 )
	
	#plt.plot( [ Xmin, Xmax ], [ Ymin, Ymax ], 'k-', lw=2 )

	#plt.show( )
	#print 'Fname:', fname
	#print 'Dsuff:', Dsuff
	plt.savefig( fname )
	plt.close()
	# Need to close to free up memory. Stops next slide being overwritten with previous slide data.

def Ztransform( zlist =[] ):
	for ZL in range(0, len( zlist ), 1 ):
		if   ( zlist[ ZL ] < damping_factor ):
			zlist[ ZL ] = damping_factor
		elif ( zlist[ ZL ] > 1 - damping_factor ):
			zlist[ ZL ] = 1 - damping_factor
		#print 'ZT - ZL:', zlist[ ZL ] 
	qzxlist = norm.ppf( zlist )
	return qzxlist

def calc_df1(  xlist, ylist ):
	df1 = 0.0
	for XL in range(0, len( xlist ), 1 ):
		#print 'DF1 - XL:', XL, 'Y:', ylist[ XL ], 'X:', xlist[ XL ]
		if ( ylist[ XL ] < xlist[ XL ] ):
			df1 += 1
			#print 'DF1 - YL:', ylist[ XL ], 'XL:', xlist[ XL ]
	return df1 		
		
def calc_ssd(  xlist, ylist, pltitle = 'DXY', fname = 'DXY.png' ):
	ssd = 0.0
	zxlist = Ztransform( xlist )
	zylist = Ztransform( ylist )
	plot_zt_graph( zxlist, zylist, pltitle, fname )
	#print 'SSD - ZX:', zxlist
	#print 'SSD - ZY:', zylist
	#print 'SSD - LZX:', len( zxlist )
	#print 'SSD - LZY:', len( zylist )
	for XL in range(0, len( xlist ), 1 ):
		#print 'SSD - XL:', XL
		if ( ylist[ XL ] > xlist[ XL ] ):
			d = 1
		else:
			d = 0
		
		ssd += ( 1 - d ) *  ( zylist[ XL ] - zxlist[ XL ] )**2 
		#print 'SSD - D:', d, 'YL:', zylist[ XL ], 'XL:', zxlist[ XL ], 'ssd:', ssd
	return ssd 

def calc_nullsd( xlist, ylist, error_value ):
	nullsd = 0.0
	for XL in range(0, len( xlist ), 1 ):
		#print 'SSD - XL:', XL
		if ( ylist[ XL ] > xlist[ XL ] ):
			S = 1
		else:
			S = 0
		nullsd = S *( 2 * error_value - 2 * error_value * xlist[ XL ] ) + ( 1 - S ) * ( 2 * error_value * xlist[ XL ] )
	return nullsd
	
def proc_Dsuff(  xlist, ylist, pltitle = 'DXY', Csuff = 0.0, fname = 'DXY.png' ):
	ssd = 0.0
	msd = 0.0
	df1 = 0.0
	F   = 0.0
	nullsd = 0.0
	ssd = calc_ssd(  xlist, ylist, pltitle, fname )
	df1 = calc_df1(  xlist, ylist )
	
	df2 = len( ylist )

	nullsd = calc_nullsd( xlist, ylist, error_value )
	emsd = nullsd / df2
	if ( df1 > 0 ):
		msd = ssd/df1
		F = msd/emsd 
	else:
		print 'ERR - DF1 Div by Zero. F error.'


	PVAL = f.sf ( F, df1, df2, loc=0, scale=1 ) 

	'''
	print 'Fname:', os.path.splitext( fname )[0]
	print 'SSD:', ssd
	print 'DF1:', df1
	print 'DF2:', df2
	print 'NULLSD:', nullsd
	print 'MSD:', msd
	print 'EMSD:', emsd
	print 'F:', F 
	print 'PVAL - SF:', PVAL
	print 'Csuff:', Csuff
	'''
	#print 
	print '{:>10s}'.format( os.path.splitext( fname )[0] ),
	print '{:>2d}'.format( Yval ),
	print '{:>4.3f}'.format( Csuff ),
	print '{:>6.3f}'.format( ssd ),
	print '{:>11.3f}'.format( F ),
	print '{:>3.2f}'.format( PVAL ),
	print '{:>3d}'.format( df2 )
	#print

#************** Csuff Processing ************** 
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
	Xmax = 1.0
	Ymax = 1.0
	#plt.figure( figsize=( 2, 2 ) ) 

	plt.title( pltitle )
	plt.xlabel( 'X' )
	plt.ylabel( 'Y' + str( Yval ) )

	#plt.axis( [ MinXaxis, MaxXaxis, MinYaxis, MaxYaxis ] )
	#print 'XL:', xlist
	#print 'YL:', ylist
	#print 'MXY:', MinXaxis, MaxXaxis, MinYaxis, MaxYaxis 
	#print 'XMin:', Xmin, 'Xmax:', Xmax, 'Ymin:', Ymin, 'Ymax:', Ymax

	#plt.plot( [ Ymin, Ymax ], 'k-', lw=2 )
	plt.plot( [ xlist ], [ ylist ], 'rD', markersize=15 )
	#plt.plot( [ 0.0, 1.0 ], [ 0.0, 1.0 ], 'k-', lw=2 )
	plt.plot( [ Xmin, Xmax ], [ Ymin, Ymax ], 'k-', lw=2 )
	#plt.plot( [ MinXaxis, MaxXaxis ], [ MinYaxis, MaxYaxis ], 'k-', lw=2 )
	#plt.show( )
	#print 'Fname:', fname
	#print 'Csuff:', Csuff
	plt.savefig( fname )
	plt.close()
	# Need to close to free up memory. Stops next slide being overwritten with previous slide data.


def proc_cons6(  XvalListn = [ ] ):
	#print 'PC6:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5,x6 = XvalListn
	#print 'A,B,C,X,Y,Z:', x1,x2,x3,x4,x5,x6
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 ) + str( x6 ) + 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'LCD:', LCD
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		#print 'ForX5:', column_dict[ x5 ][ LCD ] 
		#print 'ForX6:', column_dict[ x6 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				   column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ x6 ][ LCD ] ) )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Plot of Y' + str( Yval ) + '& Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + ',X' + str( x5 ) + ',X' + str( x6 ) + '; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + ',X' + str( x5 ) + ',X' + str( x6 ) + ')'  
	fname = 'DX' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 ) + str( x6 ) + 'Y' + str( Yval ) + '.png'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

def proc_cons5(  XvalListn = [ ] ):
#	print 'PC5:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4,x5 = XvalListn
	#print 'A,B,X,Y,Z:', x1,x2,x3,x4,x5
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 )+ 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		#print 'ForX5:', column_dict[ x5 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ x5 ][ LCD ] ) )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Plot of Y' + str( Yval ) + ' & Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) +',X' + str( x5 ) + '; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) +',X' + str( x5 ) + ')'
	fname = 'DX' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + str( x5 )+ 'Y' + str( Yval ) + '.png'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

def proc_cons4(  XvalListn = [ ] ):
	#print 'PC4:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3,x4 = XvalListn
	#print 'A,X,Y,Z:', x1,x2,x3,x4
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX1:', column_dict[ x1 ][ LCD ] 
		#print 'ForX2:', column_dict[ x2 ][ LCD ] 
		#print 'ForX3:', column_dict[ x3 ][ LCD ] 
		#print 'ForX4:', column_dict[ x4 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				  column_dict[ x4 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
				  column_dict[ x4 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
				   column_dict[ x4 ][ LCD ] ) )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Plot of Y' + str( Yval ) + ' & Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + '; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )
	
	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 )  + ',X' + str( x4 ) + ')'
	fname = 'DX' + str( x1 ) + str( x2 ) + str( x3 ) + str( x4 ) + 'Y' + str( Yval ) + '.png'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )



def proc_cons3(  XvalListn = [ ] ):
	#print 'PC3:', XvalListn, 'LX:', len( XvalListn )
	x1,x2,x3 = XvalListn
	#print 'X,Y,Z:', x1,x2,x3
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:', column_dict[ x1 ][ LCD ] 
		#print 'ForY:', column_dict[ x2 ][ LCD ] 
		#print 'ForZ:', column_dict[ x3 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ] ) )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Plot of Y' + str( Yval ) + ' & Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 ) +'; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ',X' + str( x3 ) + ')'
	fname = 'DX' + str( x1 ) + str( x2 ) + str( x3 ) + 'Y' + str( Yval ) + '.png'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )


def proc_cons2(  XvalListn = [ ] ):
	#print 'PC2List:', XvalListn, 'LX:', len( XvalListn )
	x1,x2 = XvalListn
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:', column_dict[ x1 ][ LCD ] 
		#print 'ForY:', column_dict[ x2 ][ LCD ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	pltitle = 'Plot of Y' + str( Yval ) + ' & Minimum of X' + str( x1 ) + ',X' + str( x2 ) + '; Csuff = ' + str( Csuff )
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )

	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ',X' + str( x2 ) + ')'
	fname = 'DX' + str( x1 ) + str( x2 ) + 'Y' + str( Yval ) + '.png'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )


def proc_cons1(  XvalListn = [ ] ):
	#print 'PC1:', XvalListn, 'LX:', len( XvalListn )
	## Setting x to XvalListn doesn't work. Cos it's a tuple ???
	## Must set x, = XvalListn as XvalListn is a tuple. Feature !!
	x1, = XvalListn
	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + 'Y' + str( Yval ) + '.png'
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		#print 'ForX:',  column_dict[ x1 ][ LCD ] 
		#print 'ForY:',  column_dict[ CDYval ][ LCD ] 
		#print 'MIN:', min( column_dict[ x1 ][ LCD ], column_dict[ CDYval ][ LCD ] )
		#print 'ForX:',  column_dict[ XvalListn[ 0 ] ] 
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ CDYval ][ LCD ] )
		CsuffDen +=  column_dict[ x1 ][ LCD ]
		xlist_plot.append( column_dict[ x1 ][ LCD ] )

	if ( CsuffDen != 0 ):
		Csuff = CsuffNum / CsuffDen
	#print 'xlist_plot:', xlist_plot 
	#print 'ylist_plot:', column_dict[ CDYval ]
	pltitle = 'Plot of Y' + str( Yval ) + ' & Minimum of X' + str( x1 ) + '; Csuff = ' + str( Csuff )

	fname = 'X' + str( x1 ) + 'Y' + str( Yval ) + '.png'
	plot_graph( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )
	
	fname = 'DX' + str( x1 ) + 'Y' + str( Yval ) + '.png'
	pltitle = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X' + str( x1 ) + ')'
	proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitle, Csuff, fname )
	
def proc_cons(  XvalList = [ ] ):
	#print 'List:', XvalList, 'LX:', len( XvalList)
	for n in range( len( XvalList) ):
		#print 'PC N:', n,'XVn:', XvalList[ n ], 'LenXn:', len( XvalList[ n ] )
		if ( len( XvalList[ n ] ) == 1 ):
			#print 'Call ONE'
			proc_cons1(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 2 ):
			#print 'Call TWO'
			proc_cons2(  XvalList[ n ] )
		elif ( len( XvalList[ n ] ) == 3 ):
			#print 'Call THREE'
			proc_cons3(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 4 ):
			#print 'Call FOUR'
			proc_cons4(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 5 ):
			#print 'Call FIVE'
			proc_cons5(  XvalList[ n ] )			
		elif ( len( XvalList[ n ] ) == 6 ):
			#print 'Call SIX'
			proc_cons6(  XvalList[ n ] )						
		

#***************************************************************
print 'Start:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print 'plotting for X1-6 & Y' + str( Yval ) + ' and CDYval' + str( CDYval )

read_file()
#varlist = [ 'X1', 'X2', 'X3', 'X4', 'X5', 'X6' ]
varlist = [ 1,2,3,4,5,6 ]

damping_factor   = 0.01
error_value      = 0.05

# Headers for output.
print '{:>10s}'.format( 'Label' ),
print '{:>2s}'.format( 'Y' ),
print '{:^7s}'.format( 'Csuff' ),
print '{:^6s}'.format( 'ssd' ),
print '{:^10s}'.format( 'F' ),
print '{:<5s}'.format( 'PVAL' ),
print '{:<3s}'.format( 'Num' ),
print
for Xindex in range( 1, len(varlist) + 1 ):
	XvalList = list( itertools.combinations( varlist, Xindex ) )
	#print 'List:', XvalList, 'LX:', len( XvalList)
	proc_cons( XvalList ) 
		
