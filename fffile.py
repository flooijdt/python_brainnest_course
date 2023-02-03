def reader(filename):
    try:
        r = open(filename)
        return r.read()
    except FileNotFoundError:
        print("File wasn't found.")

print(reader("attachment.txt"))