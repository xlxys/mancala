from game import Game
from board import MancalaBoard
from play import Play
import button


import pygame
import os
from pygame import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_MINUS, K_EQUALS
import time


pygame.init()

width = 745
height = 430
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Mancala')
running = 1
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define some fonts
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

play = Play()
clock = pygame.time.Clock()
clock.tick(1)
bgcolor = (0, 0, 0)
screen.fill(bgcolor)

# board and holes images
board_path = os.path.join("images", "board.jpg")
board = pygame.image.load(board_path)
he_path = os.path.join("images", "e.jpg")
he = pygame.image.load(he_path).convert()
h1_path = os.path.join("images", "1.jpg")
h1 = pygame.image.load(h1_path).convert()
h2_path = os.path.join("images", "2.jpg")
h2 = pygame.image.load(h2_path).convert()
h3_path = os.path.join("images", "3.jpg")
h3 = pygame.image.load(h3_path).convert()
h4_path = os.path.join("images", "4.jpg")
h4 = pygame.image.load(h4_path).convert()
h5_path = os.path.join("images", "5.jpg")
h5 = pygame.image.load(h5_path).convert()
hm_path = os.path.join("images", "m.jpg")
hm = pygame.image.load(hm_path).convert()


# stores
se_path = os.path.join("images", "se.jpg")
se = pygame.image.load(se_path).convert()

s1_path = os.path.join("images", "s1.jpg")
s1 = pygame.image.load(s1_path).convert()
s2_path = os.path.join("images", "s2.jpg")
s2 = pygame.image.load(s2_path).convert()
s3_path = os.path.join("images", "s3.jpg")
s3 = pygame.image.load(s3_path).convert()
s4_path = os.path.join("images", "s4.jpg")
s4 = pygame.image.load(s4_path).convert()
s5_path = os.path.join("images", "s5.jpg")
s5 = pygame.image.load(s5_path).convert()
sm_path = os.path.join("images", "sm.jpg")
sm = pygame.image.load(sm_path).convert()


# help board & winings & turns & Mancala
boardhelp_path = os.path.join("images", "boardhelp.jpg")
boardhelp = pygame.image.load(boardhelp_path).convert()
player1_path = os.path.join("images", "player1.jpg")
player1 = pygame.image.load(player1_path).convert()
player2_path = os.path.join("images", "player2.jpg")
player2 = pygame.image.load(player2_path).convert()
player1wins_path = os.path.join("images", "player1wins.jpg")
player1wins = pygame.image.load(player1wins_path).convert()
player2wins_path = os.path.join("images", "player2wins.jpg")
player2wins = pygame.image.load(player2wins_path).convert()
mancala_path = os.path.join("images", "mancala.jpg")
mancala = pygame.image.load(mancala_path).convert()
tie_path = os.path.join("images", "tie.jpg")
tie = pygame.image.load(tie_path).convert()
# score images
n0_path = os.path.join("images", "n0.jpg")
n0 = pygame.image.load(n0_path).convert()
n1_path = os.path.join("images", "n1.jpg")
n1 = pygame.image.load(n1_path).convert()
n2_path = os.path.join("images", "n2.jpg")
n2 = pygame.image.load(n2_path).convert()
n3_path = os.path.join("images", "n3.jpg")
n3 = pygame.image.load(n3_path).convert()
n4_path = os.path.join("images", "n4.jpg")
n4 = pygame.image.load(n4_path).convert()
n5_path = os.path.join("images", "n5.jpg")
n5 = pygame.image.load(n5_path).convert()
n6_path = os.path.join("images", "n6.jpg")
n6 = pygame.image.load(n6_path).convert()
n7_path = os.path.join("images", "n7.jpg")
n7 = pygame.image.load(n7_path).convert()
n8_path = os.path.join("images", "n8.jpg")
n8 = pygame.image.load(n8_path).convert()
n9_path = os.path.join("images", "n9.jpg")
n9 = pygame.image.load(n9_path).convert()
n10_path = os.path.join("images", "n10.jpg")
n10 = pygame.image.load(n10_path).convert()
n11_path = os.path.join("images", "n11.jpg")
n11 = pygame.image.load(n11_path).convert()
n12_path = os.path.join("images", "n12.jpg")
n12 = pygame.image.load(n12_path).convert()
n13_path = os.path.join("images", "n13.jpg")
n13 = pygame.image.load(n13_path).convert()
n14_path = os.path.join("images", "n14.jpg")
n14 = pygame.image.load(n14_path).convert()
n15_path = os.path.join("images", "n15.jpg")
n15 = pygame.image.load(n15_path).convert()
n16_path = os.path.join("images", "n16.jpg")
n16 = pygame.image.load(n16_path).convert()
n17_path = os.path.join("images", "n17.jpg")
n17 = pygame.image.load(n17_path).convert()
n18_path = os.path.join("images", "n18.jpg")
n18 = pygame.image.load(n18_path).convert()
n19_path = os.path.join("images", "n19.jpg")
n19 = pygame.image.load(n19_path).convert()
n20_path = os.path.join("images", "n20.jpg")
n20 = pygame.image.load(n20_path).convert()
n21_path = os.path.join("images", "n21.jpg")
n21 = pygame.image.load(n21_path).convert()
n22_path = os.path.join("images", "n22.jpg")
n22 = pygame.image.load(n22_path).convert()
n23_path = os.path.join("images", "n23.jpg")
n23 = pygame.image.load(n23_path).convert()
n24_path = os.path.join("images", "n24.jpg")
n24 = pygame.image.load(n24_path).convert()
n25_path = os.path.join("images", "n25.jpg")
n25 = pygame.image.load(n25_path).convert()
n26_path = os.path.join("images", "n26.jpg")
n26 = pygame.image.load(n26_path).convert()
n27_path = os.path.join("images", "n27.jpg")
n27 = pygame.image.load(n27_path).convert()
n28_path = os.path.join("images", "n28.jpg")
n28 = pygame.image.load(n28_path).convert()
n29_path = os.path.join("images", "n29.jpg")
n29 = pygame.image.load(n29_path).convert()
n30_path = os.path.join("images", "n30.jpg")
n30 = pygame.image.load(n30_path).convert()
n_path = os.path.join("images", "n+.jpg")
n = pygame.image.load(n_path).convert()


def ReturnStoneImage(value):
	if value == 0:
		return he
	elif value == 1:
		return h1
	elif value == 2:
		return h2
	elif value == 3:
		return h3
	elif value == 4:
		return h4
	elif value == 5:
		return h5
	elif value > 5:
		return hm


def ReturnImageForScore(score):
	if score == 0:
		image = n0
	elif score == 1:
		image = n1
	elif score == 2:
		image = n2
	elif score == 3:
		image = n3
	elif score == 4:
		image = n4
	elif score == 5:
		image = n5
	elif score == 6:
		image = n6
	elif score == 7:
		image = n7
	elif score == 8:
		image = n8
	elif score == 9:
		image = n9
	elif score == 10:
		image = n10
	elif score == 11:
		image = n11
	elif score == 12:
		image = n12
	elif score == 13:
		image = n13
	elif score == 14:
		image = n14
	elif score == 15:
		image = n15
	elif score == 16:
		image = n16
	elif score == 17:
		image = n17
	elif score == 18:
		image = n18
	elif score == 19:
		image = n19
	elif score == 20:
		image = n20
	elif score == 21:
		image = n21
	elif score == 22:
		image = n22
	elif score == 23:
		image = n23
	elif score == 24:
		image = n24
	elif score == 25:
		image = n25
	elif score == 26:
		image = n26
	elif score == 27:
		image = n27
	elif score == 28:
		image = n28
	elif score == 29:
		image = n29
	elif score == 30:
		image = n30
	elif score > 30:
		image = n
	return image


def ReturnScoreImages(scores):
	player1 = ReturnImageForScore(scores[0])
	player2 = ReturnImageForScore(scores[1])
	scores = (player1, player2)
	return scores


def ReturnStoreImage(value):
	if value == 0:
		return se
	elif value == 1:
		return s1
	elif value == 2:
		return s2
	elif value == 3:
		return s3
	elif value == 4:
		return s4
	elif value == 5:
		return s5
	elif value > 5:
		return sm


def UpdateScreen():

    screen.blit(currentPlayerImage, (240, 40))

    scores = [game.state.board["1"], game.state.board["2"]]
    scores = ReturnScoreImages(scores)

    # images scores
    screen.blit(scores[0], (664, 130))
    screen.blit(scores[1], (28, 130))

    # ----------------------------------------------------
    # Stones on the board
    G = ReturnStoneImage(game.state.board["G"])
    H = ReturnStoneImage(game.state.board["H"])
    I = ReturnStoneImage(game.state.board["I"])
    J = ReturnStoneImage(game.state.board["J"])
    K = ReturnStoneImage(game.state.board["K"])
    L = ReturnStoneImage(game.state.board["L"])
    F = ReturnStoneImage(game.state.board["F"])
    E = ReturnStoneImage(game.state.board["E"])
    D = ReturnStoneImage(game.state.board["D"])
    C = ReturnStoneImage(game.state.board["C"])
    B = ReturnStoneImage(game.state.board["B"])
    A = ReturnStoneImage(game.state.board["A"])

    # top row 12-7
    screen.blit(G, (180, 110))  # 237x167
    screen.blit(H, (237, 110))  # 294x167
    screen.blit(I, (294, 110))  # 351x167
    screen.blit(J, (398, 110))  # 455x167
    screen.blit(K, (455, 110))  # 512x167
    screen.blit(L, (512, 110))  # 569x167

    # bottom row 1-6
    screen.blit(A, (180, 177))  # 237x234
    screen.blit(B, (237, 177))  # 294x234
    screen.blit(C, (294, 177))  # 351x234
    screen.blit(D, (398, 177))  # 455x234
    screen.blit(E, (455, 177))  # 521x234
    screen.blit(F, (512, 177))  # 569x234

    # store

    store1 = ReturnStoreImage(game.state.board["1"])
    store2 = ReturnStoreImage(game.state.board["2"])

    screen.blit(store2, (118, 110))  # 173x232
    screen.blit(store1, (574, 110))  # 629x232
    # ----------------------------------------------------

    # updates the screen with the new data
    pygame.display.flip()


# load button images

pva_img = pygame.image.load("images/button_pva.png").convert_alpha()
pvp_img =  pygame.image.load("images/button_pvp.png").convert_alpha()

hard_img = pygame.image.load("images/button_hard.png").convert_alpha()
normal_img = pygame.image.load("images/button_normal.png").convert_alpha()
easy_img = pygame.image.load("images/button_easy.png").convert_alpha()


p1_img = pygame.image.load("images/button_p1.png").convert_alpha()
p2_img = pygame.image.load("images/button_p2.png").convert_alpha()


# create button instances
pva_button = button.Button(240, 40, pva_img, 1)
pvp_button = button.Button(240, 160, pvp_img, 1)

hard_button = button.Button(40, 160, hard_img, 1)
normal_button = button.Button(260, 160, normal_img, 1)
easy_button = button.Button(480, 160, easy_img, 1)

p1_button = button.Button(65, 220, p1_img, 1)
p2_button = button.Button(440, 220, p2_img, 1)

pva = False
pvp = False


clock = pygame.time.Clock()
clock.tick(0.5)

game = Game(MancalaBoard(), 1)

menu_state = "select mode"

while running:
	

	
	for event in pygame.event.get():
		if game.playerSide == 1:
			currentPlayerImage = player1
		else:
			currentPlayerImage = player2
			if pva:
				time.sleep(1)
				game.playerSide = play.computerTrun(game, heristique)
					
					
				
		if event.type == pygame.QUIT:
				running = 0
				pygame.quit()
				quit()


		if menu_state == "selected": 			
			if game.gameOver() == False:
				if pvp:	

					if event.type == pygame.KEYDOWN:
						if event.key == K_1:
							value = "A"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_2:	
							value = "B"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_3:	
							value = "C"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_4:
							value = "D"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_5:
							value = "E"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_6:	
							value = "F"
							game.playerSide = play.humanTurn(value, game)			
						if  event.key ==  K_7:
							value = "G"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_8:	
							value = "H"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_9: 
							value = "J"
							game.playerSide = play.humanTurn(value, game)
						if  event.key ==  K_0:
							value = "I"
							game.playerSide = play.humanTurn(value, game)
						if  event.key ==  K_MINUS:
							value = "K"
							game.playerSide = play.humanTurn(value, game)
						if  event.key ==  K_EQUALS:	
							value = "L"
							game.playerSide = play.humanTurn(value, game)

				if pva:
					if event.type == pygame.KEYDOWN:
		
						if event.key == K_1:
							value = "A"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_2:	
							value = "B"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_3:	
							value = "C"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_4:
							value = "D"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_5:
							value = "E"
							game.playerSide = play.humanTurn(value, game)
						if  event.key == K_6:	
							value = "F"
							game.playerSide = play.humanTurn(value, game)

					
							
				screen.fill(bgcolor)
				screen.blit(board, (100,100))
				UpdateScreen()
			else: 
				UpdateScreen()
				winner,_ = game.findWinner()
				if winner == 1:
					screen.blit(player1wins, (240,40))
				elif winner == 2:
					screen.blit(player2wins, (240,40))
				elif winner == 3:
					screen.blit(tie, (240,40))
					
				pygame.display.flip()
		else:
			screen.fill(bgcolor)


	if pvp == False:
		if menu_state == "select difficulty":
			if hard_button.draw(screen):
				heristique = 3
				menu_state = "selected"    
			if normal_button.draw(screen):
				heristique = 2
				menu_state = "selected"   
			if easy_button.draw(screen):
				heristique = 1
				menu_state = "selected"  
	


	if menu_state == "select player":
		if p1_button.draw(screen):
			menu_state = "select difficulty"
			if pvp:
				menu_state = "selected"  
			game.playerSide = 1
			
		if p2_button.draw(screen):
			menu_state = "select difficulty"
			if pvp:
				menu_state = "selected"  
			game.playerSide = 2


			

		
	if menu_state == "select mode":

		if pva_button.draw(screen):
			menu_state = "select player"
			pva = True
		if pvp_button.draw(screen):
			menu_state = "select player"
			pvp = True


	pygame.display.update()

pygame.quit()
