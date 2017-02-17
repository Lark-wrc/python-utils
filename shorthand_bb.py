import sys

def openers(line):
    tabs = 0
    while line[0] == '\\' and line[1] == 't':
        line[0] = line[2:]
        tabs+=1
    return tabs, line

def nullLine(line):
    if line == '\n' or line == "": return True
    return False

def leadword(word):
    if nullLine(word): return "", ""
    tags = ""
    cursor = 0
    while word[cursor] in ignore: cursor+=1
    while word is not "" and word[cursor] in switches:
        trim, tag = flips[word[cursor]](word[cursor+1] if len(word) > 1 else 'Nil')
        if tag: tags+=tag
        word = word[:cursor] + word[trim+cursor:]
    return word, tags

def tailword(word):
    if nullLine(word): return "", ""
    tags = ""
    cursor = -1
    while word[cursor] in ignore: cursor-=1
    while word[cursor] in switches:
        trim, tag = flips[word[cursor]]("Nil")
        if tag: tags= tag+tags
        word = word[:cursor] + (word[cursor+1:] if cursor < -1 else "")
    return word, tags


def bold(lookahead):
    if not switches['*']: tag="[b]"
    else: tag='[/b]'
    switches['*'] = not switches['*']
    return 1, tag

def underline(lookahead):
    if not switches['_']: tag="[u]"
    else: tag='[/u]'
    switches['_'] = not switches['_']
    return 1, tag

def italic(lookahead):
    global tag
    if not switches['^']: tag="[i]"
    else: tag='[/i]'
    switches['^'] = not switches['^']
    return 1, tag

def color(lookahead):
    global tag
    if not switches['#']:
        tag="[color={}]".format(colors[lookahead])
        switches['#'] = not switches['#']
        return 2, tag
    else:
        tag='[/color]'
        switches['#'] = not switches['#']
        return 1, tag

def slash(lookahead):
    if lookahead == 'c':
        if not switches['\c']:
            tag="[center]".format(colors[lookahead])
            switches['\c'] = not switches['\c']
            return 2, tag
        else:
            tag='[/center]'
            switches['\c'] = not switches['\c']
            return 2, tag
    return 2 if lookahead != '\\' else 3, ""

switches = {'*':0, '_':0, '^':0, '#':0, '\\':0, '\c':0}
flips = {'*':bold, '_':underline, '^':italic, '#':color, '\\':slash}
colors = {'c':'#79ab66', 's':'#ffb90f', 'a':'#047800', 'v':'#ee5d5d', 'w':'white'}
ignore = ["\"", "."]

def loadText():
    lines = []
    if len(sys.argv) > 1:
        pass
    else:
        paste_data = raw_input("Input text -> ")
        lines.append(paste_data)
        while paste_data is not "":
            paste_data = raw_input("")
            lines.append(paste_data)
    return lines

def convert(lines):
    out = "bbify.txt"
    f = open(out, 'w')

    for line in lines:
        if line == "-":
            f.write('[hr]\n')
            continue
        if not nullLine(line):
            tabs, newline = openers(line)
            f.write('\t'*tabs)

            for word in newline.split(" "):
                newword, tags = leadword(word)
                if tags: f.write(tags)

                newword, tags  = tailword(newword)
                f.write(newword)
                if tags: f.write(tags)
                if newword is not "": f.write(' ')

        f.write('\n')
    f.close()
    return 0

if __name__ == "__main__":
    lines = loadText()
    convert(lines)
    print "Done!"
