import pygame
import time
# You obviously copied someone's code or your dad helped you lol but NICE!!!!!!! - JS427
# Over all you arent that bad at coding, nice commenting on code for reminder congrats - JS427
# Btw do you want to help with making a minecraft spigot plugin with me ill make a repo soon look at my profile sometime - JS427

pygame.init()
pygame.display.set_caption('Art Project')

# You should make some log messages for later on for debugging and when you have problems to fix it can be helpful - JS427
print("Starting Game!")

# Intitial Setup
screen_color_navy = (32, 42, 68)
start_time = pygame.time.get_ticks() # Get start time in order to maintain timing of fade in and out

# Set up the drawing window
screen_width = 1024
screen_hight = 768
screen = pygame.display.set_mode([screen_width, screen_hight])

# rectangle setupc
# color1 of rectangle
color_r1 = 188
color_g1 = 212
color_b1 = 230

color_r2 = 133
color_g2 = 176
color_b2 = 154

color_r3 = 204
color_g3 = 51
color_b3 = 51

time_for_solid = 3000
time_for_trans = 2000

time_span_1 = 3000
time_span_2 = 5000
time_span_3 = 8000
time_span_4 = 10000
time_span_5 = 13000
time_span_6 = 15000


border_width = 50 # border thickness



# Font setup
font = pygame.font.Font('DebugFreeTrial-MVdYB.otf', 160)
text = font.render('ERASE THE PAST', True, '#04d9ff', screen_color_navy)
textRect = text.get_rect()
textRect.center = (screen_width / 2, screen_hight / 2)



temp_r = 0
temp_g = 0
temp_b = 0
    
# Run until the user asks to quit
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    screen.fill(screen_color_navy)
    # textRect.center = (screen_width / 2, screen_hight / 2)
    
    # # draw text in the center
    # screen.blit(text, textRect)
    
    # Draw border
    # variables of starting color
    
    
    # middle target color : rgb(133,176,154)
    
    #time variable
    elapsed_time = (pygame.time.get_ticks()- start_time) % (time_for_solid*3 + time_for_trans*3)
    elapsed_time_in_sec = (int)(elapsed_time/1000)
    co_x = 0
    if(elapsed_time % 2 == 0):
        co_x = 3
    else:
        co_x = -3
        
    co_y = 0
    if(elapsed_time % 2 == 0):
        co_y = 2
    else:
        co_y = -2
    
    textRect.center = (screen_width / 2 + co_x, screen_hight / 2 + co_y)
    screen.blit(text, textRect)
    
    if(elapsed_time < time_span_1):
        temp_r = color_r1
        temp_g = color_g1
        temp_b = color_b1
    elif(elapsed_time < time_span_2):
        percent_move = (elapsed_time-time_span_1)/time_for_trans 
        temp_r = color_r1 - (int)((color_r1 - color_r2) * percent_move)
        temp_g = color_g1 - (int)((color_g1 - color_g2) * percent_move)
        temp_b = color_b1 - (int)((color_b1 - color_b2) * percent_move)
    elif(elapsed_time < time_span_3):
        temp_r = color_r2
        temp_g = color_g2
        temp_b = color_b2
    elif(elapsed_time < time_span_4):
        percent_move = (elapsed_time-time_span_3)/time_for_trans 
        temp_r = color_r2 - (int)((color_r2 - color_r3) * percent_move)
        temp_g = color_g2 - (int)((color_g2 - color_g3) * percent_move)
        temp_b = color_b2 - (int)((color_b2 - color_b3) * percent_move)
    elif(elapsed_time < time_span_5):
        temp_r = color_r3
        temp_g = color_g3
        temp_b = color_b3
    else:
        percent_move = (elapsed_time-time_span_5)/time_for_trans 
        temp_r = color_r3 - (int)((color_r3 - color_r1) * percent_move)
        temp_g = color_g3 - (int)((color_g3 - color_g1) * percent_move)
        temp_b = color_b3 - (int)((color_b3 - color_b1) * percent_move)
            
    br = pygame.draw.rect(screen, (temp_r, temp_g, temp_b), pygame.Rect(0, 0, screen_width, screen_hight), border_width)
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
print("Ending Game!")
pygame.quit()


