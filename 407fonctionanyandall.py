
any([False, False, True, False]) #va donneer True

all([False, False, True, False]) # va donner False

# exemple 1
notes = [12, 14, 17, 10, 8]
notes_au_dessus_de_18 = any([x > 18 for x in notes])
print (notes_au_dessus_de_18)

# exemple 2
files =  ["chat.jpg" , "chien.jpg"]
all_files_jpg = all([f.endswith(".jpg") for f in files ])
print(all_files_jpg)


