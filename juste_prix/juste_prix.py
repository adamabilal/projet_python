"""
    DEBUT
"""
debut = str(input("bienvenue au jeux : ! (tapez merci au clavier pour commencer le jeu)"))
while debut != "merci":
     debut = str(input("bienvenue au jeux : ! (tapez merci au clavier pour commencer le jeu)"))

     print ("Bonne chance !")
"""
    JEUX
"""
import random
nombre = random.randint(0,100)
nombre1 =  int (input("Devinez un prix: "))
scoreInit = 10

while nombre != nombre1:
        if  nombre < nombre1:
                if scoreInit != 0:
                    print("nombre petit")
                    scoreInit = scoreInit-1
                    print("socre est "  + str(scoreInit))
                    nombre = int(input("Devinez un prix: "))
                else:
                    print ("veuillez recommencer le jeu vous n'avez plus de point.")
            
        elif nombre > nombre1:
                if scoreInit != 0:
                    scoreInit = scoreInit-1
                    print ("nombre grand")
                    print("score est "  + str(scoreInit))
                    nombre = int(input("Devinez un prix: "))
                else:
                    print ("veuillez recommencer le jeu vous n'avez plus de point.")
            
else :
  scoreInit = scoreInit + 2
  print("vous avez gagné :)")
  print("votre score est  " + str(scoreInit))