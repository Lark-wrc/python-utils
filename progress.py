from sys import stdout

class Spinner():
    # It spins one click every time you call animate. Budget way of showing activity is still going on.
    
    def __init__(self):
        self.FRAMES = ['\\', '|', '/', '-']

    def animate(self):
        self.FRAMES = self.FRAMES[1:]+self.FRAMES[:1]
        stdout.write('\r'+self.FRAMES[0])
        stdout.flush()

if __name__ == "__main__":
    from time import sleep
    
    s = Spinner()
    while 1:
        s.animate()
        sleep(.2)