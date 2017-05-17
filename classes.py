"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import *
from constantes import *

class Niveau:

    def __init__(self, fichier):
    	self.fichier = fichier
    	self.structure = 0


    def generer(self):
	   	with open(self.fichier, "r") as fichier:
	   		structure_niveau = []
	   		for ligne in fichier:
	   			ligne_niveau = []

	   			for sprite in ligne:

	   				if sprite != '\n':

	   					ligne_niveau.append(sprite)

	   			structure_niveau.append(ligne_niveau)

	   		self.structure = structure_niveau

    def afficher(self, fenetre):
        mur = pygame.image.load("Image/mur.png").convert()
        mur_incassable = pygame.image.load("Image/mur.png").convert()
        mechant = pygame.image.load("Image/mechant.png").convert()
        ennemi_gauche = pygame.image.load("Image/ennemi_gauche.png").convert()
        ennemi_droite = pygame.image.load("Image/ennemi_droite.png").convert()
        ennemi_dos = pygame.image.load("Image/ennemi_dos.png").convert()
        depart = pygame.image.load("Image/depart.png").convert()
        arrivee = pygame.image.load("Image/arrivee.png").convert_alpha()

        num_ligne = 0
       	for ligne in self.structure:

           num_case = 0
           for sprite in ligne:

                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':
                    fenetre.blit(mur, (x,y))
                elif sprite == 't':
                    fenetre.blit(mur_incassable, (x,y))
                elif sprite == 'p':
                    fenetre.blit(mechant, (x,y))
                elif sprite == 'e':
                    fenetre.blit(ennemi_gauche, (x,y))
                elif sprite == 'f':
                    fenetre.blit(ennemi_droite, (x,y))
                elif sprite == 'g':
                    fenetre.blit(ennemi_dos, (x,y))
                elif sprite == 'd':
                   	fenetre.blit(depart, (x,y))
                elif sprite == 'a':
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
           num_ligne += 1

class Ennemie:

    def __init__(self,random_direction , niveau):
        self

class Perso:

    def __init__(self, droite, gauche, haut, bas, niveau):
        #sprites de bonberman#
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()


        #POUR RENDRE TRANSPARENT LE BLANC#
        self.droite.set_colorkey((255,255,255))
        self.gauche.set_colorkey((255,255,255))
        self.haut.set_colorkey((255,255,255))
        self.bas.set_colorkey((255,255,255))
        #posotion de bomberman en case et pixel#
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #ces la direction par defaut#
        self.direction = self.droite
        self.niveau = niveau
        #Position de la bombe#




    def deplacer(self, direction):

        if direction == 'droite':
            if self.case_x < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and self.niveau.structure[self.case_y][self.case_x+1] != 't':
                    self.case_x += 1
                    self.x = self.case_x * taille_sprite
                self.direction = self.droite


        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and self.niveau.structure[self.case_y][self.case_x-1] != 'y':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche


        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 't':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 't':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas



class Bombe :


    def __init__(self, explosion, niveau):

        self.explosion=pygame.image.load(explosion).convert()
        self.explosion.set_colorkey((255,255,255))
        self.x=0
        self.y=0
        self.case_x=0
        self.case_y=0
        self.direction = self.explosion
        self.niveau=niveau

    def explose(self):


        if self.niveau.structure[self.case_x+1][self.case_y]=="m":
            self.niveau.structure[self.case_x+1][self.case_y]="0"



        if self.niveau.structure[self.case_y+1][self.case_x]=="m":
            self.niveau.structure[self.case_y+1][self.case_x]="0"



        if self.niveau.structure[self.case_x-1][self.case_y]=="m":
            self.niveau.structure[self.case_x-1][self.case_y]="0"

        if self.niveau.structure[self.case_y-1][self.case_x]=="m":
            self.niveau.structure[self.case_y-1][self.case_x]="0"



