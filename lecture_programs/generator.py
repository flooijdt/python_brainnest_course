def generator(word, file):
    with open(file) as f:
        for line in f:
            # line = f.readline()
            if word in line:
                yield line


gen = generator("boi", "text.txt")
print(next(gen))
print(next(gen))
print(next(gen))
