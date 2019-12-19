import pygame


L=[[0,0,0],[0,0,0],[0,0,0]]
joueur = 1


def display(L,x,y,marginRight,marginLeft,marginTop,marginBottom):
    for i in range(x):
        for j in range(y):
            pygame.draw.rect(Fond_Ecran,BLUE,(marginRight+100*i,marginTop+100*j,100,100),2)
            if L[i][j]==1:
                pygame.draw.circle(Fond_Ecran,BLUE,(marginRight+100*i+50,marginTop+100*j+50),50,2)
            elif L[i][j]==2:
                pygame.draw.line(Fond_Ecran,BLUE, (marginRight+100*i,marginTop+100*j), (marginRight+100*(i+1),marginTop+100*(j+1)),2)
                pygame.draw.line(Fond_Ecran,BLUE, (marginRight+100*(i+1),marginTop+100*j), (marginRight+100*i,marginTop+100*(j+1)),2)

def caseDispo(L):
    for i in L:
        for j in i:
            if j==0:
                return True
    return False

def fin():
    Police_Texte = pygame.font.Font("freesansbold.ttf",25) 
    Fond_Texte = Police_Texte.render("Rejouer", True,WHITE,BLACK)
    Fond_Ecran.blit(Fond_Texte,(475,150))
    Police_Texte = pygame.font.Font("freesansbold.ttf",25) 
    Fond_Texte = Police_Texte.render("Quitter", True,WHITE,BLACK)
    Fond_Ecran.blit(Fond_Texte,(475,250))
    pygame.display.update()

def win(L,joueur):
    j=0
    etat=False
    for i in L:
        if i[j]==i[j+1]==i[j+2]==joueur:
            etat=True
    for x in range(len(L)):
        if L[j][x]==L[j+1][x]==L[j+2][x]==joueur:
            etat=True
        elif L[0][0]==L[1][1]==L[2][2]==joueur:
            etat=True
        elif L[2][0]==L[1][1]==L[0][2]==joueur:
            etat=True
    return etat

def displayInit(marginRight,marginLeft,marginTop,marginBottom):
    Police_Texte = pygame.font.Font("freesansbold.ttf",48) #Police d'écriture
    Fond_Texte = Police_Texte.render("Morpion 2.0", True,RED,BLACK) # Couleur pour l'écriture
    Forme_Texte = Fond_Texte.get_rect()
    Forme_Texte.topleft = (165,50)
    Fond_Ecran.blit(Fond_Texte,Forme_Texte)
    display(L,3,3,marginRight,marginLeft,marginTop,marginBottom)

#Initialisation de pygame
pygame.init()
Fond_Ecran = pygame.display.set_mode((600,600))# Taille de la fenetre (en pixel)
pygame.display.set_caption("Morpion")  #Nom de la fenetre

marginRight = 150
marginLeft = 450
marginTop = 150
marginBottom = 450


#Couleurs PYGAME
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,40,0)


displayInit(marginRight,marginLeft,marginTop,marginBottom)


inProgress = True
finish=False
while inProgress:
    for event in pygame.event.get():
        #Fermer la fenetre
        if event.type == pygame.QUIT:
            inProgress = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = event.pos
            # Vérification - Il reste dans le tableau
            if not finish:
                if posX >= marginRight and posX <= marginLeft and posY >=marginTop and posY <=marginBottom:
                    x=(posX-marginRight)//100
                    y=(posY-marginTop)//100
                    if L[x][y] == 0:
                        L[x][y]=joueur
                        display(L,3,3,marginRight,marginLeft,marginTop,marginBottom)
                        pygame.display.update()
                        if win(L,joueur):
                            fin()
                            Police_Texte = pygame.font.Font("freesansbold.ttf",25) 
                            Fond_Texte = Police_Texte.render("Victoire Joueur "+str(joueur), True,WHITE,BLACK)
                            Fond_Ecran.blit(Fond_Texte,(175,500))
                            finish = True

                        elif not caseDispo(L):
                            fin()
                            Police_Texte = pygame.font.Font("freesansbold.ttf",25) 
                            Fond_Texte = Police_Texte.render("Egalité", True,WHITE,BLACK)
                            Fond_Ecran.blit(Fond_Texte,(300,500))
                            finish = True

                        joueur = 3-joueur
            else:
                if posX >= marginLeft and posX <= 600 and posY >=marginTop and posY <=175:
                    L=[[0,0,0],[0,0,0],[0,0,0]]
                    finish = False
                    Fond_Ecran.fill(BLACK)
                    displayInit(marginRight,marginLeft,marginTop,marginBottom)
                    display(L,3,3,marginRight,marginLeft,marginTop,marginBottom)
                    pygame.display.update()
                elif posX >= marginLeft and posX <= 600 and posY >=marginTop+100 and posY <=275:
                    inProgress = False
               
         
    pygame.display.update()
pygame.quit()
