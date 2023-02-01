def filer(filename):
    try:
        file = open(filename)
        text = file.read()
        return text.upper()
    except OSError:
        return "Wrong type fool!"

print(filer("attachment.txt"))
