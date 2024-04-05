texto = input("Insira a palavra ou texto para inverter: ")
inverso = []
for i in texto[::-1]:
 inverso.append(i)
inverso = "".join(str(element) for element in inverso)
print(inverso)