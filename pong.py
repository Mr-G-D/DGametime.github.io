import pygame

pygame.init()

clock = pygame.time.Clock()
speed=50
display_width = 700
display_height = 500

x=100
y=100
radius = 20
dx=3
dy=3

paddle_x = 10
paddle_y = 10
paddle_width = 5
paddle_height = 60

def hit_back():
    if x + radius>display_width:
        return True
    return False

def hit_sides():
    if y - radius < 0:
        return True
    if y + radius > display_height:
        return True
    return False

def hit_paddle():
    if x-radius <=paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        return True
    return False

def game_over():
    end_game = True
    display.fill(0,0,0)
    font_title = pygame.font.Font(None,36)
    font_instructions = pygame.font.Font(None,24)
    announcement = font_title.render("Game Over",True,(255,255,255))
    announcement_rect = announcement.get_rect(center = (int(display_width/2),int(display_height/2)))
    display.blit(announcement,announcement_rect)
    qinstructions = font_instructions.render("Press Q to Quit",True,(255,255,255))
    qinstructions_rect = qinstructions.get_rect(center = (int(display_width/2) , int(display_height/1.5)))
    display.blit(qinstructions,qinstructions_rect)
    rinstructions = font_instructions.render("Press R to Resume",True,(255,255,255))
    rinstructions_rect = rinstructions.get_rect(center = (int(display_width/2),int(display_height/1.3)))
    display.blit(rinstructions,rinstructions_rect)
    pygame.display.flip()
    while(end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.type == pygame.k_r:
                    end_game = False

display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("lets go and lets get it")
display.fill((0,0,0))
welcome_sr = pygame.font.Font(None,30)
welcome = welcome_sr.render("pongy!",True,(255,255,255))
welcome_rect = welcome.get_rect(center = (int(display_width/2),int(display_height/3)))
display.blit(welcome,welcome_rect)
pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT, 5000)

timer_active = True
while (timer_active):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False
while True:
    clock.tick(speed)
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height +10 <= display_height:
            paddle_y +=10
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y-10>=0:
            paddle_y-=10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    display.fill((0,0,0))
    x+=dx
    y+=dy
    
    pygame.draw.rect(display,(255,255,255),(paddle_x,paddle_y,paddle_width,paddle_height))
    pygame.draw.circle(display,(255,0,0),(x,y),radius)
    if x < radius:
        game_over()
        x = 250
        y = 150
        dx = abs(dx)
    if hit_back() or hit_paddle():
        dx*=-1
    if hit_sides():
        dy*=-1
    pygame.display.update()

