
import os

# on se positionne sur le répertoire qui contient le fichier
os.chdir('/Users/kerhuon/Dropbox/Python/EM_SSI_Cours_Python/EN-us-drchuck/materials')
f = open('mbox.txt', 'r')

domaines = []

for line in f:
	if line.startswith('From:'):
		domaines.append(line.split('@')[1].strip()) # gmail.com

# domaines comprend maintenant la liste de tous les domaines de tous les emails
# il y a donc beaucoup de doublons

f.close() # important, il faut fermer le fichier

liste_finale = []

for i, domaine in enumerate(domaines):
	if domaine not in domaines[i+1:]: # pour éviter les doublons
		liste_finale.append([domaine, domaines.count(domaine)])

# NOTA : liste_finale n'est pas triée
# cf log_mails_01.py pour le tri de la comprehension list

print(liste_finale)