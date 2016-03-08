class Window(object):
    def __init__(self, state = "closed"):
        self.state = state

    def open(self):
        if self.state == "opened":
            print "Window already opened!"
        else:
            self.state = "opened"
            print "Window opened!"

    def close(self):
        if self.state == "closed":
            print "Window already closed!"
        else:
            self.state = "closed"
            print "Window closed!"
