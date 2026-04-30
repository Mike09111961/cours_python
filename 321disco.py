
#permet de stocker des données sous formes de clé : valeur
dictionnaire= {"prenom": "Jacques","age": "25"}

# Imbricable comme listes 
# /!\ les clés sont uniques ( impossible d'avoir 3 clef " prenom" par exemple)
# Pour exemple accéder à la valeur :
dictionnaire ["prenom"]
# Ou
dictionnaire.get("prenom") # Retourne une erreur si clé n'existe pas

print(dictionnaire)
