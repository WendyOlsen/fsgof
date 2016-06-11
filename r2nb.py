#!/cygdrive/c/Python27/python


## Read in data from CSV file.
## Use Cress & Snow 2000 Data only.
## Set value of X from 1 to 6.
## X axis is min X and Y. Y is Y1.

import csv
import sys
import matplotlib.pyplot as plt

Cons_Numerator   = 0.0
Cons_Denominator = 0.0
Yaxis     = []
linenum   = 0
minvalues = []

if ( len( sys.argv ) < 2 ):
	fname = 'cs2k.csv'
	Xval  = 1
else:
	fname = sys.argv[ 1 ]
	Xval  = int( sys.argv[ 2 ] )

#sys.exit() 

with open( fname, 'rb' ) as f:
	reader = csv.reader(f)
	for row in reader:
		linelist = list( row )
		#print 'Xn:', linelist[1], 'Y1', linelist[ 7 ] 
		Xn = linelist[ Xval ]
		Y1 = linelist[ 7 ] 
		try:
			Cons_Numerator   += float( min( Xn, Y1 ) ) 
			Cons_Denominator += float( Xn ) 
			linenum += 1
			print 'X {:<5} Xn {:<5} Y1 {:<5} Min {:<5} '.format( str( Xval ), Xn, Y1,  min( Xn, Y1 ) )
			#print 'X' + str( Xval ), Xn, '\tY1:', Y1, '\tMIN:', min( Xn, Y1 )
			minvalues.append( min( Xn, Y1 ) ) 
			Yaxis.append( Y1 )
			#Yaxis.append( Xn )
		except:
			print 'X' + str( Xval ), Xn, 'Y1:', 'Type:', type( Xn )


print 'Num:', Cons_Numerator, 'Den:', Cons_Denominator  
if ( Cons_Denominator != 0 ):
	print 'Quotient:', Cons_Numerator / Cons_Denominator
	Csuff = Cons_Numerator / Cons_Denominator
else:	
	print 'Div ZERO:', Cons_Numerator , Cons_Denominator

print 'Min Vals, X axis:', minvalues	
print 'Y axis:', Yaxis 
print 'Min Y axis:', min( Yaxis ), 'Min X axis:', min( minvalues )
print 'Max Y axis:', max( Yaxis ), 'Max X axis:', max( minvalues )

MinXaxis =  float( min( minvalues ) ) - 1.0
MaxXaxis =  float( max( minvalues ) ) + 1.0 

MinYaxis =  float( min( Yaxis ) ) - 1.00 
MaxYaxis =  float( max( Yaxis ) ) + 1.00 

print 'Axes:', MinXaxis, MaxXaxis, MinYaxis, MaxYaxis

fname = 'X' + str( Xval ) + 'Y1.png'

print 'Fname:', fname

pltitle = 'Minimum of X' + str( Xval ) + ' & Y1; Csuff = ' + str( Csuff )
print 'Title:', pltitle

plt.title( pltitle )
plt.xlabel( 'X' ) 
plt.ylabel('Y1')

plt.axis( [ MinXaxis, MaxXaxis, MinYaxis, MaxYaxis ] ) 

plt.plot( [ minvalues ], [ Yaxis ], 'ro') 
plt.show( )
#plt.savefig( fname )
