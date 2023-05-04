import os

print('Bienvenu sur le programme de conversion de secondes en heure(s), minute(s) et seconde(s)')


# Fonctions faisant les vérifications sur les secondes entrées par l'utilisateur
def demande():
    seconde = input('Entrez un nombre de secondes : ')
    if seconde.isdigit():
        seconde = int(seconde)
        if seconde < 0:
            print('Veuillez entrer des secondes valides')
            return demande()
        elif seconde == 0:
            print('Vous avez entrer 0 comme secondes. Veuillez entrer un nombre différents de 0 pour profiter du'
                  ' programme')
            return demande()
        else:
            return seconde
    else:
        print('Veuillez entrer un nombre')
        return demande()


# Recuperation des secondes entrées par l'utilisateur
temps = demande()

# Calcul et affichage du temps que représente les secondes entrées
if temps >= 3600:
    heures = temps // 3600
    minutes = (temps % 3600) // 60
    secondes = (temps % 3600) % 60
    print(temps, 'seconde(s) correspond à ', heures, 'heure(s), ', minutes, 'minute(s) et', secondes, 'seconde(s)')

elif temps >= 60:
    minutes = temps // 60
    secondes = temps % 60
    print(temps, 'seconde(s) correspond à ', minutes, 'minute(s) et ', secondes, 'seconde(s)')

else:
    print(temps, 'seconde(s) correspond à ', temps, 'seconde(s)')

os.system('pause')
