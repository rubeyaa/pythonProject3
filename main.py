#créé par Adam Rubeya
#créé en 2023
#Ce code est un jeu vidéo qui consiste à ce battre contre des monstres

from random import randint as oof

niveau_vie = 20
force_monstre = 0
menu = 0
deerandom = 0
deerandomboss = 0
deemonstre = 0
nbVictoire = 0
print("Vous êtes situés dans un long couloir et vous allez devoir combattre des monstres de différents niveaux de difficultés.")
print("Vous avez 20 pts de vie, si vous perdez contre un monstre, vous allez perdre des points de cette dernière")
#les deux print servent d'introduction au jeu

while niveau_vie > 0:
    if nbVictoire %3 == 0 and nbVictoire > 0:
        deemonstre = 11
        print("Vous venez de tomber contre un boss de niveau %d" %(deemonstre))

        choix = int(input("1- combattre \n 2- fuir\n 3- Voir le règles du jeu\n 4- Quitter la partie"))
        if choix == 1:

                print("vous allez combattre le boss")
                deerandomboss = oof(0, 22)
                print("votre chiffre est %d" % (deerandom))

                if deerandomboss > deemonstre:
                    print("Vous avez battu le monstre!")
                    nbVictoire = nbVictoire + 1
                    print("vous avez %d pv" % (niveau_vie))
                    print("vous avez %d victoires d'affilés" % (nbVictoire))
                    print("----------------------------------------------------------------------------------------------------------------------------------------------")
                elif deerandomboss < deemonstre:
                    niveau_vie = niveau_vie - deemonstre
                    print("vous avez perdu la bataille")
                    print("Vous avez %d pv" % (niveau_vie))
                    print("----------------------------------------------------------------------------------------------------------------------------------------------")
                elif deerandomboss == deemonstre:
                    niveau_vie = niveau_vie - deemonstre
                    print("vous avez perdu la bataille")
                    print("Vous avez %d pv" % (niveau_vie))
                    print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 2:
            print("Vous venez de fuir, vous êtes lache. Vous allez perdre des points de vies")
            niveau_vie = niveau_vie - 1
            nbVictoire = 0
            print("Vous avez %d pv" % (niveau_vie))
            print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 3:
            print("Il faut que vous roulez un dé et si ce dé est superieur a la force du monstre, vous gagnez. Si votre dé est inferieur vous perdez le combat et un peu de pv")
            print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 4:
            print("imagine avoir quitter le jeu")
            quit()
    else:
        deemonstre = oof(1,6)
        print("Vous tombez sur un monstre de dificulté : %d" %(deemonstre))
        print("Voulez vous combattre ou non")
        choix = int(input("1- combattre \n 2- fuir\n 3- Voir le règles du jeu\n 4- Quitter la partie"))

        if choix == 1:

            print("vous allez combattre le monstre")
            deerandom = oof(0,6)
            print("votre chiffre est %d" %(deerandom))

            if deerandom > deemonstre:
                print("Vous avez battu le monstre!")
                nbVictoire = nbVictoire + 1
                print("vous avez %d pv" %(niveau_vie))
                print("vous avez %d victoires d'affilé" %(nbVictoire))
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
            elif deerandom < deemonstre:
                niveau_vie = niveau_vie - deemonstre
                print("vous avez perdu la bataille")
                print("Vous avez %d pv" % (niveau_vie))
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
            elif deerandom == deemonstre:
                niveau_vie = niveau_vie - deemonstre
                print("vous avez perdu la bataille")
                print("Vous avez %d pv" % (niveau_vie))
                print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 2:
            print("Vous venez de fuir, vous êtes lache. Vous allez perdre des points de vies")
            niveau_vie = niveau_vie - 1
            nbVictoire = 0
            print("Vous avez %d pv" %(niveau_vie))
            print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 3:
            print("Il faut que vous roulez un dé et si ce dé est superieur a la force du monstre1, vous gagnez. Si votre dé est inferieur vous perdez le combat et un peu de pv")
            print("----------------------------------------------------------------------------------------------------------------------------------------------")

        elif choix == 4:
            print("imagine avoir quitter le jeu")
            quit()

