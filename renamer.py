import os, sys

checker = True

"""	Takes in the arguements. First being the directory in question,
	the secound, if exists, can be -q to turn off confirmation.
"""
if len(sys.argv) == 2:
	os.chdir(sys.argv[1])
elif len(sys.argv) == 3:
	os.chdir(sys.argv[1])
	if sys.argv[2] == '-q':
		checker = False
else:
	print 'false'
	exit()

#List out all of the files.
files = os.listdir('.')

#For each file, split it into the name and the extension, b and c.
#All directories are skipped.
for f in files:
	if os.path.isdir(f):
		continue
	out = []
	inpareth = False
	b = f[0:len(f)-4]
	c = f[len(f)-4:]

	""" 
	For every character in the filename, either replace '_' or 
	'.' with a ' ' character, do nothing with regular characters, or
	filter out every character between any type of paretheses.
	"""
	for i in b:
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

	#Join the new file name, and remove a leading '+' if neccessary.
	b = ''.join(out)
	b = b.split()
	d = []
	if b[0][0] == '+':
		b[0] = b[0][1:]

	#removed, for appending a 1x to the episode number.
	"""
	for i in b:
		if i.isdigit():
			#d.append('1x' + i)
			d.append(i)
		else:
			d.append(i)
		d.append(' ')
	"""

	#combine the filename into a string and attach it's extension.
	out = ' '.join(b)
	out = out.strip() + c

	#print the file name, and ask for confirmation before renaming. 
	print out
	if checker:
		a = raw_input("this okay? y/n ")
		if a=='y' or a=='yes' or a=='':
			os.rename(f, out)
	else:
		os.rename(f, out)
	
print 'Sayonara.'
