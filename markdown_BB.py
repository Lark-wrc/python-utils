import sys
import re


class Flag:
    flag = 0


class Instance:
    def __init__(self):
        self.flag = 0

subs = {'*':'i', '**':'b', '_':'u', '&':'color', '&&c':'center',
        '&c':'color=#79ab66', '&s':'color=#ffb90f', '&r': 'color=#9a5821',
        '&a':'color=#047800', '&v':'color=#ee5d5d', '&w':'color=white'}
color_flag = Flag()
state = {code: color_flag if 'color' in code else Instance() for code in subs.values()}


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
    writer = open('bbify.txt', 'w')
    for line in lines:
        for markdown in reversed(sorted(subs, key=lambda x: len(x))):
            if line != '\n':
                while re.search(re.escape(markdown), line) is not None:
                    line = re.sub(re.escape(markdown), replace(markdown), line, count=1)
        writer.write(line)
        writer.write('\n')


def replace(markdown):
    code = subs[markdown]
    if state[code].flag:
        state[code].flag = 0
        return '[/'+code+']' if 'color' not in code else '[/'+code+']"'
    else:
        state[code].flag = 1
        return '['+code+']' if 'color' not in code else '"['+code+']'

if __name__ == "__main__":
    lines = loadText()
    convert(lines)
    print "Done!"