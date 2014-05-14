import os, sys

checker = True

"""	Takes in the arguements. First being the directory in question,
	the secound, if exists, can be -q to turn off confirmation.

	old version.

if len(sys.argv) == 2:
	os.chdir(sys.argv[1])
elif len(sys.argv) == 3:
	os.chdir(sys.argv[1])
	if sys.argv[2] == '-q':
		checker = False
else:
	print '[-q] directory'
	exit()
"""

dirs = []
for x in sys.argv[1:]:
	if x[0] == '-':
		arg = x[1:]
		if arg == 'q':
			checker = False
	else:
		dirs.append(x)

#No directories found.
if len(dirs) == 0:
	print '[-q] directories'


startdir = os.getcwd()
for cdir in dirs:
	os.chdir(cdir)
	
	#List out all of the files.
	files = os.listdir('.')

	#For each file, split it into the name and the extension, b and c.
	#All directories are skipped.
	for f in files:
		if os.path.isdir(f):
			continue
		out = []
		inpareth = False
		fname = f[0:len(f)-4]
		ext = f[len(f)-4:]

		""" 
		For every character in the filename, either replace '_' or 
		'.' with a ' ' character, do nothing with regular characters, or
		filter out every character between any type of paretheses.
		"""
		for i in fname:
			if not inpareth:
				if i == '_' or i == '.':
					out.append(" ")
					continue
				elif i == '[' or i == '(' or i == '{':
					inpareth = True
				else:
					out.append(i)
			elif inpareth:
				if i == ']' or i == ')' or i == '}':
					inpareth = False

		#Update the filename to the changed one.
		fname = out
		if fname[0] == '+':
			fname = fname[1:]

		#combine the filename into a string and attach it's extension.
		out = ''.join(fname)
		out = out.strip() + ext

		#print the file name, and ask for confirmation before renaming. 
		print out
		if checker:
			a = raw_input("this okay? y/n ")
			if a=='y' or a=='yes' or a=='':
				os.rename(f, out)
		else:
			os.rename(f, out)
	os.chdir(startdir)
	
print 'Sayonara.'
