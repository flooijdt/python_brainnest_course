file = open("mbox.txt")
text = file.read()
listatest = text.split()
lista = []
counter = 0
for i in listatest:
    if i == "From:":
        lista.append("Sender: ")
        lista.append(listatest[counter+1])
    counter += 1
print(lista.join())
            
        
