import os
import subprocess

def processSingleFile(file_path, module_name):
    file_str = str
    with open(file_path, "r") as file:
        file_str = file.read()
    try:
        begin = file_str.index("<!-- " + module_name + " -->")
        end = file_str.index("<!-- " + module_name + "/ -->")
        module_str = str
        with open("modules/" + module_name, "r") as file:
            module_str = file.read()
        file_str = file_str[0:(begin + len(str("<!-- " + module_name + " -->")))] + \
            "\n\n" + module_str + "\n\n" + file_str[end:len(file_str)]
        os.remove(file_path)
        with open(file_path, "w+") as file:
            file.write(file_str)
        
    except ValueError:
        pass


current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)

files = os.listdir(current_directory)
suitable_files = [] 

for i in range(0, len(files)):
    if (files[i].find(".html") != -1):
        suitable_files.append(files[i])

del files

current_directory = os.path.dirname(current_file)

files = os.listdir(current_directory + "/modules")
suitable_modules = [] 

for i in range(0, len(files)):
    if (files[i].find(".html") != -1):
        suitable_modules.append(files[i])
del files

for file in suitable_files:
    for module in suitable_modules:
        processSingleFile(file, module)

prog = subprocess.Popen("/home/ilya/.local/bin/djlint *.html --indent 2 --reformat", shell=True, stdout=subprocess.PIPE)
prog.communicate()[0]

