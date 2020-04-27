import pygame
import random
random.seed

global x
global y
x=0
y=0

pygame.init()
window_size=[600,600]
sceen=pygame.display.set_mode(window_size)
image=pygame.image.load('./duck.png')
game_over=False

def new_img():
  global imagex
  global imagey
  imagex=x
  imagey=y
  sceen.fill([255, 255, 255])
  sceen.blit(image,(x,y))
  print('ch')

def check_image(mouse_x,mouse_y):
  if((imagex<mouse_x and mouse_x<imagex+120) or (imagey<mouse_y and mouse_y<imagey+120)):
    print('yes ch')
    return True
  else:
    print('no ch')
    return False

new_img()
x=random.randint(0,480)
y=random.randint(0,480)

while not game_over:
  mouse_position = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over=True
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_position = pygame.mouse.get_pos()
      if check_image(mouse_position[0],mouse_position[1]):
        new_img()
        x=random.randint(0,480)
        y=random.randint(0,480)
        print('yes',x,y)
        pygame.display.flip()
      else:
        print('no',x,y)
        pygame.display.flip()
  pygame.display.flip()

pygame.quit()