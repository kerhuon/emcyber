
import os
os.chdir('/Users/kerhuon/Dropbox/Python/EM_SSI_Cours_Python/EN-us-drchuck/materials')
f = open('mbox.txt', 'r')

liste = [line.split('@')[1].strip() for line in f if line.startswith('From:')] # gmail.com

liste_finale = sorted([[element, liste.count(element)] for i, element in enumerate(liste) 
	if element not in liste[:i]], # no duplicates
	key = lambda domaine : domaine[1], # sort by frequence
	reverse = True)

f.close()

for j in liste_finale:
	print("Domaine: {:20}{:5}".format(j[0], j[1]))

