

nombre1 = 0
nombre2 = 0
choix  = 0
Résultat = 0 

nombre1  = int(input("entrer un nombre a"))
nombre2  = int(input("Entrer un nombre b "))

# choix utilisateur
c = int(input(" rentrer un choix 1 = addition,choix 2 : soustraction , choix 3 : multiplication , choix 4 : division"))

if c == 1 : 
    print(nombre1+nombre2) 
    
elif c == 2 :
    print(nombre1-nombre2) 

elif  c == 3 : 
    print(nombre1*nombre2) 

elif c ==4 :
    print(nombre1/nombre2) 



