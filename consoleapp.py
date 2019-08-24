""" ConsoleApp sub-class of ggame App """

from ggame import App

   


def main(state, data):
    """ main function """
    global x
    global y
    if not state:
        input("enter x", 1)
    elif state == 1:
        x = data
        input("enter y", 2)
    else:
        y = data
        print(x, y)
    

class ConsoleApp(App):
    """ ConsoleApp sub-class of App """
    _input = input
    
    def __init__(self, *args, entry=None):
        super().__init__(*args)
        self._instack = []
        self.run()
        self._entry = entry
        self._routemain(None)
    
    def _routemain(self, newstate):
        if not self._entry:
            main(newstate)
        else:
            self._entry(newstate)
        
    def _pushInput(self, prompt, newstate, newfunc):
        self._instack.append((prompt, newstate, newfunc))
        
    def step(self):
        """ periodic processing """
        if self._instack:
            prompt, newstate, newfunc = self._instack.pop(0)
            inval = self._input(prompt)
            if newfunc:
                newfunc(newstate)
            else:
                self._routemain(newstate)
            
def input(prompt, newstate=None, newfunc=None):
    inval = _input(prompt)
 

ConsoleApp()
