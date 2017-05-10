import sys
import re

class Switch(object):

    def __nonzero__(self):
        return self.active

    def __init__(self, active=0):
        self.active = active

    def switch(self):
        self.active = 0 if self.active else 1


class LockedSwitch(Switch):

    def switch(self):
        pass


class Replaceable(object):

    def __init__(self, markdown, bb, value="", switch=None):
        self.markdown = markdown
        self._bbs = '[' + bb + ('='+value if value else "") + ']'
        self._bbe = '[/'+bb+']'
        self._switch = switch if switch is not None else Switch()
        
        self.length = len(markdown) - markdown.count('\\')

    def matched(self):
        replacement = self._bbe if self._switch else self._bbs
        self._switch.switch()
        return replacement

    def replaceIn(self, string):
        return re.sub(self.markdown, self.matched(), string, count=1)

    def isIn(self, string):
        return re.search(self.markdown, string)

    def len(self):
        return self.length

class ReplaceableAmbiguous(Replaceable):
    """Legacy switch for catching $_ as the close character doesn't work
    with multiple colored blocks on the same line. 
    """
    def __init__(self, markdown, bb, value="", switch=None):
        super(ReplaceableAmbiguous, self).__init__(markdown, bb, value, switch)
        self.markdown_pre = markdown[:-1]+'(\W|\Z|[^'+ markdown[-1]+'])'

    def replaceIn(self, string):
        if self._switch:
            # legacy = re.search(self.markdown, string)
            # if legacy: 
            #     return re.sub(self.markdown, self.matched(), string, count=1)
            whitespace = re.search(self.markdown_pre, string).group(1)
            return re.sub(self.markdown_pre, self.matched()+whitespace, string, count=1)
        return re.sub(self.markdown, self.matched(), string, count=1)

    def isIn(self, string):
        if self._switch: 
            # legacy =  re.search(self.markdown, string)
            # if legacy: 
            #     return re.search(self.markdown, string)
            return re.search(self.markdown_pre, string)
        return re.search(self.markdown, string)


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

class RepDec(object):

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
    RepDec_NewLineClose(Replaceable('\$m', 'center')),
    Replaceable('---', 'hr', switch=LockedSwitch()),
    RepDec_NewLineClose
    (
        ReplaceableOneMany('^#{3,6}[ ]*', Switch(), 
            Replaceable('\$m', 'center'),
            Replaceable('', 'b'), 
            Replaceable('', 'size', '14pt')
        )
    ),
    RepDec_NewLineClose
    (
        ReplaceableOneMany('^#[ ]*', Switch(), 
            Replaceable('\$m', 'center'),
            Replaceable('', 'b'), 
            Replaceable('', 'u'),
            ReplaceableAmbiguous('\$w', 'color', 'white'),
            Replaceable('', 'size', '18pt')
        )
    ),
    RepDec_NewLineClose
    (
        ReplaceableOneMany('^##[ ]*', Switch(), 
            Replaceable('\$m', 'center'),
            Replaceable('', 'b'), 
            Replaceable('', 'u'),
            Replaceable('', 'size', '16pt')
        )
    ),
    RepDec_NewLineClose(Replaceable('^> ', 'quote')),
    RepDec_NewLineClose(Replaceable('^\+ ', 'li')),

    ReplaceableAmbiguous('\$c', 'color', '#79ab66'),
    ReplaceableAmbiguous('\$s', 'color', '#ffb90f'),
    ReplaceableAmbiguous('\$r', 'color', '#9a5821'),
    
    ReplaceableAmbiguous('\$a', 'color', '#047800'),
    ReplaceableAmbiguous('\$v', 'color', '#ee5d5d'),
    ReplaceableAmbiguous('\$w', 'color', 'white'),

    ReplaceableAmbiguous('\$b', 'color', '#EC5800'),
    ReplaceableAmbiguous('\$p', 'color', '#D464E4'),
    ReplaceableAmbiguous('\$n', 'color', '#8E44AD'),
    ReplaceableAmbiguous('\$u', 'color', '#FBF9AB')
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
                    #print repr(line)
        writer.write(line)
        #writer.write('\n')
    return 0

if __name__ == "__main__":
    lines = loadText()
    convert(lines)
    print "Done!"
    with open('bbify.txt', 'r') as f:
        print f.read()