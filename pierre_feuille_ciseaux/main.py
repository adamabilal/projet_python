import random

score_joueur = 0
compteur_score = 0

nbrTour_joueur = int(input('Combien  de manches ? '))
nbrTour = 0
while (nbrTour < nbrTour_joueur):
     
	choix_du_joueur = input('Choisis  entre pierre feuille ou ciseaux : ')
	if(choix_du_joueur == 'pierre' or choix_du_joueur == 'feuille' or choix_du_joueur == 'ciseaux'):

		print('--------------------------')

		
		choix = ['pierre', 'feuille', 'ciseaux']
		compteur_choix = random.choice(choix)


		print('L\'ordinateur a choisis : ', compteur_choix)

		if(choix_du_joueur == compteur_choix):
			print('Egalitée')
		elif(choix_du_joueur == 'pierre' and compteur_choix == 'feuille'):
			print('L\'ordi gagne !')
			compteur_score = compteur_score + 1
		elif(choix_du_joueur == 'pierre' and compteur_choix == 'ciseaux'):
			print('Le joueur gagne')
			score_joueur = score_joueur + 1
		elif(choix_du_joueur == 'feuille' and compteur_choix == 'pierre'):
			print('Le joueur gagne')
			score_joueur = score_joueur + 1
		elif(choix_du_joueur == 'feuille' and compteur_choix == 'ciseaux'):
			print('L\'ordi gagne !')
			compteur_score = compteur_score + 1
		elif(choix_du_joueur == 'ciseaux' and compteur_choix == 'pierre'):
			print('L\'ordi gagne !')
			compteur_score = compteur_score + 1
		elif(choix_du_joueur == 'ciseaux' and compteur_choix == 'feuille'):
			print('Le Joueur gagne !')
			score_joueur = score_joueur + 1

		nbrTour = nbrTour + 1
		print('Manche numero ', nbrTour, ' sur ', nbrTour_joueur)

		#affiche score
		print('Tu as ', score_joueur, ' points')
		print('L\'ordi a ', compteur_score, ' points')

	else:
		print('Je ne comprend pas...')

#determine qui a gagné
if(score_joueur > compteur_score):
	print('------Partie finie sur une victoire ! :)------')
elif(compteur_score > score_joueur):
	print('------Partie finie sur une défaite :(------')
else:
	print('------Partie finie sur une égalitée :/------')