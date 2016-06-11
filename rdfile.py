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

