import pygame as py
import math
import random
words_lists = ("PYTHON","NUMPY","PANDAS","PYGAME")

py.init()
#set display
WIDTH,HEIGHT=800,500
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Hangman Game")

#button variables
RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH - (RADIUS*2+GAP)*13)/2)
starty= 400
A=65
for i in range(26):
  #  RADIUS*2+GAP = the distance between the circles
  #  i % 13= selectes the nect line 
  #  GAP * 2= the distance from the boaders
  x= startx + GAP * 2 + (( RADIUS*2+GAP)*(i % 13))
  y= starty+((i//13)*(GAP+RADIUS*2))
  letters.append([x,y,chr(A+i),True])

#fonts
LETTER_FONT= py.font.SysFont('comicsans',25)
WORD_FONT=py.font.SysFont('comicsans',30)
#load images
images=[]
for i in range(7):
  image=py.image.load("hangman"+str(i)+".png")
  images.append(image)

#games variables
hangman_status = 0

word=random.choice(words_lists)
guessed=[]
#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
#set up game loop
FPS = 60
clock = py.time.Clock()
run=True

def draw():
  #sleceting the background colour as white
  win.fill(WHITE)
  #draw word
  display_word =" "
  for letter in word:
    if letter in guessed:
       display_word += letter + "  "
    else:
       display_word+="_ "
  text= WORD_FONT.render(display_word, 1, BLACK)
  win.blit(text,(400,200))
  
  #draw buttons
  for letter in letters:
    x,y, ltr,visible =letter
    if visible:
     py.draw.circle(win,BLACK,(x,y),RADIUS,3)
     text=LETTER_FONT.render(ltr,1,BLACK)
     win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
  #selecting the location of the image and appling the image over the 
  #the white background with "blit"
  win.blit(images[hangman_status],(150,100))
  py.display.update()

#end screen
def display_message(message):
    win.fill(WHITE)
    text=WORD_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 ))
    py.display.update()
    py.time.delay(1500)

def answer_is(Answer):
  win.fill(WHITE)
  text=WORD_FONT.render(Answer,1,BLACK)
  win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 ))
  py.display.update()
  py.time.delay(1500)
  

while run:
  clock.tick(FPS)
  draw()

#  for exting the game with "X" button
  for event in py.event.get():
    if event.type == py.QUIT:
       run=False
    # gets the position or the coordinates of the mouse
    if event.type==py.MOUSEBUTTONDOWN:
      m_x,m_y = py.mouse.get_pos()
      for letter in letters:
         x,y,ltr,visible= letter
         if visible:
          dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
          if dis < RADIUS:
           letter[3]=False
           guessed.append(ltr)
           if ltr not in word:
             hangman_status +=1
  
  won=True
  for letter in word:
    if letter not in guessed:
      won = False
      break

  if won:
    display_message("YOU WON!!!!")
    break

  if hangman_status==6:
    display_message("YOU LOST ¯\_( ͡° ͜ʖ ͡°)_/¯ !!!!")
    display_message("THE ANSWER WAS")
    answer_is(word)
    break

py.quit()