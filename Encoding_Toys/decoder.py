low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
high = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
out = []
enteanlow =  'azyxewvtisrlpnomqkjhugfdcb'
enteanhigh = "AZYXEWVTISRLPNOMQKJHUGFDCB"

print "You have something to decode?"
print ""

a = raw_input("Well, you want to decode a entean script, y/n? ")
if a == 'y' or a == 'yes':
	print ""
	a = raw_input("What's the script? ")
	for x in a:
		if x in enteanlow:
			out.append(low[enteanlow.index(x)])
		elif x in enteanhigh:
			out.append(high[enteanhigh.index(x)])
		else:
			out.append(x)
	print ""
	print "The script reads:"
	print ''.join(out)



print ""
print "bye."
