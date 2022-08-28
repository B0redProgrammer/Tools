import os
import time
import pathlib

path = pathlib.Path(__file__).parent.resolve()

conf = input("Do you want to create a lookup table? (Y/N): ")
if conf != "Y":
    exit()

name = input("What name do you want to give your lookup table?")
Text_File_Name = path+name+".txt"

os.system('echo  > {}'.format('~/Documents/Code/Python/personal_programs/lookup_tables/created_tables/'+name+".py"))
os.system('echo  > {}'.format(Text_File_Name))

time.sleep(1)

script = open(path+name+".py", "a")
file = open(Text_File_Name, "a")

sample_script = open('{}/sample_table.py'.format(path), 'r')

for line in sample_script.readlines():
    if 'sample.txt' in line:
        line = line.replace('sample.txt', Text_File_Name)
    script.write(line)

file.close()
script.close()

command = input('With what command do you want to connect this lookup table?')

file = open('/home/sat/.bashrc', 'a')
file.write("alias {}='python3 {}/{}.py'".format(command, path, name))

file.close()

file = open('/home/sat/Desktop/customcommands.txt', 'a')
file.write("{} -> access the {} lookup table".format(command, name))

file.close()
