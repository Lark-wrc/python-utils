low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
high = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
out = []
enteanlow =  'azyxewvtisrlpnomqkjhugfdcb'
enteanhigh = "AZYXEWVTISRLPNOMQKJHUGFDCB"
from random import randint

print "let's encrypt some data. Or really, encode it."
print " "

a = raw_input("Would you like to do a Ceasar cipher, y/n? ")
if a == 'y' or a == 'yes':
        print " "
        print """Okay. A Ceasar cipher works by replacing one character with another, 
usually a set distance down the alphabet. so B by a 25 ceasar cipher is A."""

        b = raw_input("Would you like to use a specific number shift, y/n? ")
        shift = ' '
        if b=='y' or b == 'yes':
                print " "
                shift = raw_input("What number? ")
        else:
        	print ' '
                print "We'll use a random one then."
                shift = randint(1, 24)
        print " "
        phrase = raw_input("Now, what will you encode? ")
        
        #for the unimplemented random shift. 
        if(shift == '*'):
                shift = randint(1, 24)
        else:
                shift = int(shift)
                while(shift > 26):
                        shift = shift - 26
        
	for x in phrase:
                if low.__contains__(x):
                        original = low.index(x)
                        new = original + shift
                        while(new > 26):
                                new = new - 26
                        out.append(low[new])
                elif high.__contains__(x):
                        original = high.index(x)
                        new = original + shift
                        while(new > 26):
                                new = new - 26
                        out.append(high[new])
                else:
                        out.append(x)
        print " "
        print "And we're all done. The encoded form is as follows."
        print ''.join(out)
        print " "
        print "Sayonara!"
        exit()
        
a = raw_input("Would you like to do Entean, the language of Ente Isla, y/n? ")
if a == 'y' or a == 'yes':
	print ' '
	phrase = raw_input("okay then. We'll need a phrase to translate then. ")
	
	for x in phrase:
		if low.__contains__(x):
			out.append(enteanlow[low.index(x)])
		elif high.__contains__(x):
			out.append(enteanhigh[high.index(x)])
		else:
			out.append(x)
	print " "
	print "And it's finished. Here is the translation."
	print ''.join(out)
	print " "
	print "Sayonara!"
	exit()
	
else: 
        print "Sayonara!"
