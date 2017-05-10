import sys
import re

class Switch():

    def __nonzero__(self):
        return self.flag

    def __init__(self, flag=0):
        self.flag = flag

    def switch(self):
        self.flag = 0 if self.flag else 1


class LockedSwitch(Switch):

    def switch(self):
        pass


class Replaceable():

    def __init__(self, markdown, bb, value="", switch=None):
        self.markdown = markdown
        self._bbs = '[' + bb + ('='+value if value else "") + ']'
        self._bbe = '[/'+bb+']'
        self._switch = switch if switch is not None else Switch()
        
        self.length = len(markdown) - markdown.count('\\')

    def matched(self):
        replacement = self._bbe if self._switch.flag else self._bbs
        self._switch.switch()
        return replacement

    def replaceIn(self, string):
        return re.sub(self.markdown, self.matched(), string, count=1)

    def isIn(self, string):
        return re.search(self.markdown, string)

    def len(self):
        return self.length

class ReplaceableOneMany(Replaceable):

    def __init__(self, markdown, switch, *replaceables):
        self.markdown = markdown
        self._switch = switch if switch is not None else Switch()
        self.length = len(markdown) - markdown.count('\\')
        self.replaces = replaceables

    def matched(self):
        if not self._switch:
            replacement = ''
            for replaceable in self.replaces:
                replacement+=replaceable.matched()
            self._switch.switch()
            return replacement
        else:
            for replaceable in self.replaces[1:]:
                replaceable.matched()
            self._switch.switch()
            return self.replaces[0].matched()

class RepDec():

    def __init__(self, base):
        self.base = base

    def matched(self):
        return self.base.matched()

    def replaceIn(self, string):
        return self.base.replaceIn(string)

    def isIn(self, string):
        return self.base.isIn(string)

    def len(self):
        return self.base.len()


class RepDec_NewLineClose(RepDec):

    def replaceIn(self, string):
        return re.sub(self.base.markdown, self.base.matched(), string, count=1).rstrip('\n') + self.base.matched() + '\n'

replacements = [
    Replaceable('\*', 'i'),
    Replaceable('\*\*', 'b'),
    Replaceable('_', 'u'),
    Replaceable('&&c', 'center'),
    Replaceable('---', 'hr', switch=LockedSwitch()),
    RepDec_NewLineClose
    (
        ReplaceableOneMany('^#{1,6} ', Switch(), 
            Replaceable('', 'b'), 
            Replaceable('', 'size', '14pt')
        )
    ),

    Replaceable('&c', 'color', '#79ab66'),
    Replaceable('&s', 'color', '#ffb90f'),
    Replaceable('&r', 'color', '#9a5821'),
    
    Replaceable('&a', 'color', '#047800'),
    Replaceable('&v', 'color', '#ee5d5d'),
    Replaceable('&w', 'color', 'white'),

    Replaceable('&b', 'color', '#EC5800'),
    Replaceable('&p', 'color', '#D464E4'),
    Replaceable('&n', 'color', '#8E44AD'),
    Replaceable('&u', 'color', '#FBF9AB')
]

def loadText():
    lines = []
    if len(sys.argv) > 1:
        lines = open(sys.argv[1], 'r').readlines()
    else:
        paste_data = raw_input("Input text -> ")
        lines.append(paste_data)
        while paste_data is not "":
            paste_data = raw_input("")
            lines.append(paste_data)
    return lines


def convert(lines):
    writer = open('bbify.txt', 'w')
    for line in lines:
        for replaceable in reversed(sorted(replacements, key=lambda x: x.len())):
            if line != '\n':
                while replaceable.isIn(line):
                    line = replaceable.replaceIn(line)
        writer.write(line)
        writer.write('\n')
    return 0

if __name__ == "__main__":
    lines = loadText()
    convert(lines)
    print "Done!"
    with open('bbify.txt', 'r') as f:
        print f.read()