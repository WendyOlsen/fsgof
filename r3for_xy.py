#!/usr/bin/python

## Read in data from CSV file.
## Create R file for qnorm transform.
## Run copy of prog for x,y vals used in R script.
## Run using: f:\windows\python\python.exe r3for_xy.py

## df1 & df2 are degrees of freedom. 

import csv
import sys 
from scipy.stats import norm, f

#print 'Fname:', fname, 'Xval:', Xval
#sys.exit() 

Cons_Numerator   = 0.0
Cons_Denominator = 0.0
damping_factor   = 0.01
error_value      = 0.05


## x=c( 0.7,0.3,0.4,0.45 );
## y=c( 0.8,0.5,0.5,0.4 ); 
## Vals from R prog.

#xlist = [ 0.7,0.3,0.4,0.45 ]
#ylist = [ 0.8,0.5,0.5,0.4 ]

X1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0]

X2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

X3 = [0.87, 0.5, 0.5, 0.67, 0.33, 1.0, 0.5, 0.87, 0.87, 1.0, 0.87, 1.0, 1.0, 0.17, 0.87, 0.33, 0.87, 0.87, 0.0, 1.0, 0.5, 0.87, 0.0, 0.0, 0.87, 1.0, 0.33, 1.0, 1.0, 0.87, 0.0, 0.0, 0.0, 0.87, 0.17, 0.5, 0.0, 0.87, 1.0]

X4 = [0.17, 0.5, 1.0, 0.33, 0.17, 0.67, 0.87, 0.67, 1.0, 1.0, 0.17, 0.17, 0.33, 0.0, 0.67, 0.87, 1.0, 0.33, 0.33, 0.33, 0.0, 0.87, 0.17, 0.17, 0.87, 0.87, 0.5, 0.33, 0.87, 0.17, 0.5, 0.67, 0.87, 0.17, 0.17, 0.17, 0.5, 0.17, 0.87]

X5 = [1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

X6 = [1.0, 0.0, 1.0, 0.0, 0.87, 1.0, 0.0, 0.87, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.87, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0]

Y1 = [1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0]

xlist = X3
ylist = Y1

def Ztransform( zlist =[] ):
	for ZL in range(0, len( zlist ), 1 ):
		if   ( zlist[ ZL ] < damping_factor ):
			zlist[ ZL ] = damping_factor
		elif ( zlist[ ZL ] > 1 - damping_factor ):
			zlist[ ZL ] = 1 - damping_factor
		#print 'ZT - ZL:', zlist[ ZL ] 
		## still need to do qnorm ...
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
		
def calc_ssd(  xlist, ylist ):
# Need to check this bit ... do calc on xZ and yZ ie after norm.ppf
	ssd = 0.0
	zxlist = Ztransform( xlist )
	zylist = Ztransform( ylist )
	print 'SSD - ZX:', zxlist
	print 'SSD - ZY:', zylist
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



print 'Xlist:', xlist
print 'Ylist:', ylist

ssd = calc_ssd( xlist, ylist )
df1 = calc_df1(  xlist, ylist )
df2 = len( ylist )
msd = ssd/df1
#emsd = ( error_value )**2 * 4
## EMSD=EXPECTED MEAN SQUARE DISTANCE 
## New emsd error_value^2 / df2
emsd = ( error_value )**2 / df2

F = msd/emsd 
PVAL = f.sf ( F, df1, df2, loc=0, scale=1 ) 

print 'SSD:', ssd
print 'DF1:', df1
print 'DF2:', df2
print 'MSD:', msd
print 'EMSD:', emsd
print 'F:', F 
print 'PVAL - SF:', PVAL
## pval = pf( F, df1, df2, lower.tail = FALSE )
