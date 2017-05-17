"""
Jeu Bonberman Labyrinthe Jeu dans lequel on doit déplacer Bonberman jusqu'aux coffres à travers un labyrinthe.

"""
import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

fenetre = pygame.display.set_mode((940,640), RESIZABLE)
icone = pygame.image.load("Image/Bonbermanimage.jpg")
pygame.display.set_icon(icone)
pygame.display.set_caption("Image/Bonberman made in School")
pygame.display.flip()
pygame.mixer.init()
son = pygame.mixer.music.load("Son/Super_Bomberman.mp3")
pygame.mixer.music.play(loops=-1 , start=0.0)


maxlife = 100
afficher_bombe = 0       #variables qui initialise la bombe.
bombe_active = 0
timer = 0

#On demare la boucle pour le jeu
continuer = 1

while continuer:
    accueil = pygame.image.load("Image/Bonbermanimage.jpg").convert()

    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    continuer_jeu = 1
    continuer_accueil = 1

    while continuer_accueil:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                choix = 0


            elif event.type == KEYDOWN:

                if event.key == K_F1:
                    continuer_accueil = 0
                    choix = 'n1'

                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'n2'

                elif event.key == K_F3:
                    continuer_accueil = 0
                    choix = 'n3'


    if choix != 0:
        fond = pygame.image.load("Image/fonddujeu.jpg").convert()
        fond_Original = pygame.image.load("Image/Bonbermanimage.jpg").convert()
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)
            #A se niveau Mico on crée Bonberman et la bombe #
        Bomberman = Perso("Image/Bomberman_droite.png","Image/Bomberman_gauche.png","Image/Bomberman_dos.png","Image/Bomberman.png", niveau)
        bombe = Bombe("Image/Bombe.png", niveau)

        pygame.key.set_repeat(200, 120)
        continuer = 1


#Là Mico on lance le jeu , enfin la boucle du jeu
        while continuer_jeu:

            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer_jeu = 0

#Là vielle branche on code les touches pour le déplacement de Bonberarabe
                    elif event.key == K_RIGHT:
                        Bomberman.deplacer('droite')
                    elif event.key == K_LEFT:
                        Bomberman.deplacer('gauche')
                    elif event.key == K_UP:
                        Bomberman.deplacer('haut')
                    elif event.key == K_DOWN:
                        Bomberman.deplacer('bas')
                    elif event.key == K_SPACE:
                        timer = pygame.time.get_ticks()
                        son = pygame.mixer.music.load("Son/son_explosion.mp3")
                        son = 1
                        pygame.mixer.music.play()
                        bombe.explose()    #affichage de la bombe
                        afficher_bombe = 1
                        bombe_active = 1
                        bombe.x = Bomberman.x
                        bombe.y = Bomberman.y

            if pygame.time.get_ticks() - timer >= 3000 :        #Au bout de 3 secondes, la bombe disparait
                bombe_active = 0
                afficher_bombe = 0
                son = 0
            fenetre.blit(fond, (0,0))
            niveau.afficher(fenetre)

            fenetre.blit(Bomberman.direction, (Bomberman.x, Bomberman.y))       #chargement du personnage, sa position sa direction
            if afficher_bombe:
                fenetre.blit(bombe.direction, (bombe.x, bombe.y))
            pygame.display.flip()
            fenetre.blit(fond,(0,0))
            pygame.display.flip

                   #chargement du personnage, sa position sa direction
            if niveau.structure[Bomberman.case_y][Bomberman.case_x] == 'a':
                continuer_jeu = 0
                 #ici il fallait redonner la nouvelle valeur <br>#de la position du personnage pour le deplacer a l'ecran, à la fin de ma boucle sans cette <br><br>#"mise a jour" la pos_mechant n'avait pas change.


pygame.quit()












