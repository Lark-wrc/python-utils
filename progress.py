from sys import stdout

class Spinner():
    # It spins one click every time you call animate. Budget way of showing activity is still going on.
    
    def __init__(self):
        self.FRAMES = ['\\', '|', '/', '-']
    
    def _write(self, content, tail=''):
        stdout.write('\r['+content+']'+tail)
        stdout.flush()

    def animate(self):
        self.FRAMES = self.FRAMES[1:]+self.FRAMES[:1]
        self._write(self.FRAMES[0])

class CounterForm(Spinner):
    def __init__(self, decorated, count=25):
        self.decorated = decorated
        self.ticks = 0
        self.count = 25
    
    def animate(self):
        self.decorated.animate()
        self.ticks+=1
        if self.ticks%self.count == 0:
            self._write(str(self.ticks), '\n')

if __name__ == "__main__":
    from time import sleep
    
    s = CounterForm(Spinner())
    while 1:
        s.animate()
        sleep(.5)