import os, sys

helpstring = """\
	-c      --check         Disable filename checker.
	-n      --nocur         Disables recurance.
	-d      --nodirchk      Disables recursion confirmation. RISKY.
	-h      --help          This should be obvious.
"""

def fix(dir='.', check=1, recur=1, chk=1):
	userconfirm = check
	recurse = recur
	dirchk = chk

	if len(sys.argv) > 1:
		for x in sys.argv[1:]:
			if x == '--check' or x == '-c':
				userconfirm = 0
			elif x == '--help' or x == '-h':
				print 'Recusively renames all files in the directory listed.'
				print 'Commands: '
				print  helpstring
				exit()
			elif x == '--norecur' or x == '-n':
				recur = 0
			elif x == '--nodirchk' or x == '-d':
				dirchk = 0
			else:
				os.chdir(x)
		sys.argv = []
	else:
		os.chdir(dir)
	
	
	list = os.listdir('.')
	
	for f in list:
		if os.path.isdir(f):
			if dirchk and recur:
				a = raw_input(f + ' recurse? ')
				if a == 'y' or a == 'yes' or a == '':
					fix(f, userconfirm, recurse, dirchk)
					os.chdir('../')
			elif recur:
				fix(f, userconfirm, recurse, dirchk)
                                os.chdir('../')
			continue
		output = []
		clearing = 0
		
		filename = f[0:-4]
		extent = f[-4:]
		for i in filename:
			if not clearing:
				if i == '_' or i == '.':
					output.append(' ')
				elif i == '[' or i == '(' or i == '{':
					clearing = 1
				else:
					output.append(i)
			else:
				if i == ']' or i == ')' or i == '}':
					clearing = 0
		if output[0] == '+':
			output = output[1:]
		output = ''.join(output)
		output = output.strip() + extent
		
		print output
		if userconfirm:
			a = raw_input("Okay? y/n ")
			if a=='kill':
				exit()
			if a=='y' or a=='yes' or a=='':
				os.rename(f, output)
		else:
			os.rename(f, output)
	print 'Folder Complete~'
if __name__ == "__main__":
	fix()
	print 'Mission Complete~'
