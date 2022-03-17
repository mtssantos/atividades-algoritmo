def consulta(palavra):
   contador_vogais = 0
   contador_consoantes = 0
   for letra in palavra:
       if letra in "aeiouAEIOU":
           contador_vogais += 1
       else:
           contador_consoantes += 1 
   print(f"A palavra {palavra}, contém: {contador_vogais} vogais e {contador_consoantes} consoantes")


palavra = input("Digite a string a ser consultada: ")
consulta(palavra)