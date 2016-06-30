# fsgof
FSGOF Source Code
Instructions for Use:
How to run the python code for fuzzy set goodness of fit tables and plots.
.Prep.  Put the python anaconda programmes onto your c: drive to run, e.g. in a c:\python directory.
.Prep the file area for your work:  md c:\fsgof  and check it by dir.  These are run from the command line, or on a MAC or Linux, do it as appropriate.
.Command line.  The programme we wrote is command-line driven.  Below you find the format for this single line, with some options.  You will need to be clear about where the input is coming from, and this director is key.  That’s where the output should go.  The plots will go in the directory from which you run the comments.  The table of output is called here a doc file, but it is in txt format and can also be called a rtf file if you wish (but not docx nor anything else). There is another table of output in csv format:  this is the same file, but translated into csv, and this is the one you name in your command line.
.Get the cursor in the right area.  On Windows machines this is done as:  START > COMMAND PROMPT then cd c:\fsgof  using our suggested area.  If you didn’t yet create this directory, return to PREP stage.
Suppose I have put the Python Anaconda programmes on a chip, which is F: drive.
.run the command like this:
C:\fsgof> f:\python.exe CDsuff.py c:\data\****.csv 4 > op4.doc
The command options are as follows:
Python  inputfilename  Ychoice “>” [that means output the text file to] textfileoutputfilename
Thus another option is:  

C:\fsgof>  python.exe CDsuff.py c:\fsgof\inputIndia.csv 1 > outputforY1India.doc
NOTES: 
# Contact developers John Mcloughlin and Wendy Olsen of the
# Unversity of Manchester via the Facebook Group:
# Integrated Mixed Methods Network.
# This work is released under the Creative Commons Licence.
# You are free to use, change and distribute this work as long
# as you cite:
# Fuzzy Set Goodness of Fit Tests Version 1.
# JM & WO 2016/06/28
# Requirements: Python modules numpy and matplotlib must be installed.
# The Anaconda Python distribution contains all the required modules.
# Download from: https://www.continuum.io/downloads
# Usage - Windows Command Prompt: 
# c:\python\python.exe CDsuff.py inputfile.csv Y-Value > outputfile.txt
# where Y-Value is from 1 to 4. Eg
# c:\python\python.exe CDsuff.py indiafile.csv 3 > outputfile.txt
# Mac or Linux Terminal:
# CDsuff.py inputfile.csv Y-Value > outputfile.txt
# The path to the python executable is provided by the first line 
# of the program. See line 1 above.
# This program implements Ronggui Huang's 2010 R program for
## Goodness-of-Fit Tests and Descriptive Measures in Fuzzy-Set Analysis
## Eliason S. & Stryker R. 2009. Sociological Methods & Research 38:102-146.

