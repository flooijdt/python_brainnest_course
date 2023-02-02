file = open("mbox-short.txt")
text = file.read()
listatest = text.split()
lista = []
dictio = {}
domain = {}
counter = 0
for i in listatest:
    if i == "From:":
        lista.append("\nSender: ")
        lista.append(listatest[counter+1])
        dictio.update({listatest[counter+1]: listatest.count(listatest[counter+1])})
    counter += 1
# print("".join(lista))
# print(dictio)
dictio2={}
new = []
for k, v in dictio.items():
    dictio2.update({k.split("@")[1]: v})

print(dictio2)

            
        
