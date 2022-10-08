script_files = [r"G:/py/exdata/13_script1.txt",
                r"G:/py/exdata/13_script1.txt"]

for file in script_files:
    try:
        with open(file) as fl:
            script = fl.read()
            print("Processing file: ", file)
            exec(script)
    except FileNotFoundError:
        print("File {1:s} does not exist".format(file))
