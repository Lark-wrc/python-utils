import itertools
import copy

inits = []

#Generates the team names, using the leader at index lead of initial array.
def gen(lead=0):
    results = []
    base = inits.pop(lead)
    #first
    tail = [x[0] for x in [member for member in inits]]
    results.append([base[0]+"".join(x) for x in itertools.permutations(tail, 3)])
    #last
    tail = [x[1] for x in [member for member in inits]]
    results.append([base[1]+"".join(x) for x in itertools.permutations(tail, 3)])
    #mix
    results.append([])
    for tail in [x for x in _tails(inits)]:
        for lead in base:
            results[2].extend([lead+"".join(x) for x in itertools.permutations(tail, 3)])
    return results

#Recursive helper method.
def _tails(team):
    if len(team) == 1:
        for x in team[0]:
            yield x
    else:
        for y in team.pop():
            for x in tails(team):
                yield y+x

#Prints teams with leader at index lead. Types 0 prints none, 1 Given names, 2, given and family, 3 all names. 
def doprint(lead=0, types=3):
    for res, pref, _ in zip(gen(lead), ["Leader First Given:","Leader Last Family:","Leader First Mixed:"], range(0,types)):
        print pref
        print "\n".join(["    ".join(res[i:i+6]) for i in xrange(0,len(res),6)]).upper()
        print

# Prints all the leader choices. 
def doprintall():
    global inits
    back = inits[:]
    for i in xrange(4):
        print "With leader:", [back[i]]
        inits = back[:]
        doprint(i)

#Take input from command line. Alternative to cgi maybeh?
def cmdin():
    print "\nEnter Initial/Name for each Member. \"Sherwood Cathasaigh\" OR \"S C\""
    print "Start with Leader."
    while len(inits) < 4:
        io = raw_input("> ").split()
        inits.append((io[0][0], io[1][0]))
    print "\n\n"

#Runs if you run the file directly
if __name__ == "__main__":
    io = raw_input("(A)ll or (1) leader? > ")
    cmdin()
    if io.strip()[0].lower() in ['a','all']: doprintall()
    elif io[0] == '1': doprint()
    else: print "RTFM."