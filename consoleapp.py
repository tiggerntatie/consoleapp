""" ConsoleApp sub-class of ggame App """

from ggame import App

   


def main(state, data):
    """ main function 
    
        Entry with data = None first time
    """
    global x
    global y
    if not state:
        input("enter x ", state=1)
    elif state == 1:
        x = data
        input("enter y ", state=2)
    else:
        y = data
        print(x, y)
    

class ConsoleApp(App):
    """ ConsoleApp sub-class of App """
    _input = input
    _instack = []
    
    def __init__(self, *args, entry=None):
        super().__init__(*args)
        self._instack = []
        self.run()
        self._entry = entry
        self._routemain(None)
    
    def _routemain(self, newstate, data=None):
        if not self._entry:
            main(newstate, data)
        else:
            self._entry(newstate, data)
        
    @classmethod
    def _pushInput(cls, prompt, newstate, newfunc):
        cls._instack.append((prompt, newstate, newfunc))
        
    def step(self):
        """ periodic processing """
        if type(self)._instack:
            (prompt, newstate, newfunc) = type(self)._instack.pop(0)
            inval = type(self)._input(prompt)
            if newfunc:
                newfunc(newstate, inval)
            else:
                self._routemain(newstate, inval)
            
def input(prompt, **kwargs):
    """ input 
    
        optional keyword arguments
        state = value to be passed into next function (default main entry)
        func = next function to execute (will be passed state and input result)
    """
    newstate = kwargs.get('state', None)
    newfunc = kwargs.get('func', None)
    ConsoleApp._pushInput(prompt, newstate, newfunc)
 

ConsoleApp()
