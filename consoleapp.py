""" ConsoleApp sub-class of ggame App """

from ggame import App

def gginput(prompt):
    return input(prompt)

def step():
    """ periodic processing """
    
    x = gginput("enter x")
    y = gginput("enter y")
    print(x, y)

App().run(step)