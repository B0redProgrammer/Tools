import os
import sys

sys.path.append('/home/sat/Documents/Code/Python/personal_programs/custom_terminal/help_scripts/')

from colors import colormessage

def extract_file(filename):
    file = open(filename, 'r')
    ord = {}

    for line in file.readlines():
        name, execution = line.split('|')
        ord[name] = execution
    file.close()
    return ord

commands = extract_file('commands.txt')

while True:
    Input = input(colormessage('{}>'.format(os.path.abspath(os.getcwd())), color = 'blue'))

    In = Input.split(' ')

    if len(In) > 0:
        if In[0] in commands:
            os.system(commands[In[0]]+''.join(Input[i] for i in (1, len(In))))
    else:
        if Input in commands:
            os.system(commands[Input])
        else:
            os.system(commands[Input])
    else:
        os.system(Input)
