string = input("Digite uma string: ")
inversa = ""

for i in range(len(string)-1, -1, -1):
    inversa += string[i]

print("String invertida:", inversa)
