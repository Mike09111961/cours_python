
#importer le module
import time
#jour et mois en français
import locale
locale.setlocale(locale.LC_ALL,'fr_FR.UTF-8')

#temps écoulé depuis le 1 janvier 1970
print(time.time())

#temps détaillé
print(time.localtime())

#Afficher le jour de la semaine 
print(time.strftime("%A %d %B %Y"))
