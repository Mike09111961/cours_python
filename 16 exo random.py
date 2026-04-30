
import random 
 
nombre_mystere = random.randrange(0,100) 
nombre_utilisateur = 101

while nombre_mystere != nombre_utilisateur: 
    nombre_utilisateur = int(input ("rentrer un nombre"))   
    if nombre_utilisateur == nombre_mystere :
        print("ok")
    elif nombre_utilisateur > nombre_mystere:
        print ("plus bas ")
    else:
        print ("plus haut")
