""" ConsoleApp sub-class of ggame App """

from ggame import App

def gginput(prompt):
    return input(prompt)


def main():
    """ main function """
    x = gginput("enter x")
    y = gginput("enter y")
    print(x, y)
    

class ConsoleApp(App):


    def __init__(self, *args, entry=None):
        super().__init__(*args)
        self.run()
        if not entry:
            main()
        else:
            entry()
        
    def step(self):
        """ periodic processing """
        print("step")


ConsoleApp()
