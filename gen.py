import os

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
            "\n" + module_str + "\n" + file_str[end:len(file_str)]
        if file_path == "index.html":
            print(file_str)

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



