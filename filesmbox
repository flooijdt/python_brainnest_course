filename = input("give me the file's name: ")
def filer(filename):
    try:
        if filename == "demofile.txt":
            return "No way I'm reading this sheee."
        file = open(filename)
        text = file.read()
        return text.upper()
    except OSError:
        return "Wrong type fool!"

