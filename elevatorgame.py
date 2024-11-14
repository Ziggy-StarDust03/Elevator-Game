# Example file showing a circle moving on screen
import pygame
import time

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))

def gameloop():
    global screen
    running = True
    clock = pygame.time.Clock()
    dt = 0


    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    floor1_pos = pygame.Vector2(screen.get_width() / 2, 0)
    floor2_pos = pygame.Vector2(screen.get_width() / 2, 240)
    floor3_pos = pygame.Vector2(screen.get_width() / 2, 480)


    floorNum = 1


#passing floors
    floor1Up = False
    floor2Up = False
    floor3Up = False


    floor1Down = False
    floor2Down = False
    floor3Down = False


    floorTimer = 0
    previous_time = pygame.time.get_ticks()

    while running:
    #MAIN LOOP
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")


    
        pygame.draw.rect(screen, "white", (600, 260, 300, 200)) #elevator
        pygame.draw.rect(screen, "black", (750, 320, 120, 80))  
        pygame.draw.circle(screen, "black", (700, 260 + 100), 20)
        pygame.draw.circle(screen, "green", (620, 180 + 100), 10)
        pygame.draw.circle(screen, "blue", (620, 210 + 100), 10)
        pygame.draw.line(screen, "white", (600, 720), (600, 0), 10)
        pygame.draw.line(screen, "white", (0, floor1_pos.y), (600, floor1_pos.y), 10)
        pygame.draw.line(screen, "white", (0, floor2_pos.y), (600, floor2_pos.y), 10)
        pygame.draw.line(screen, "white", (0, floor3_pos.y), (600, floor3_pos.y), 10)
    
        font = pygame.font.SysFont("Arial", 24)
        counter_text = font.render(f"Floor: {floorNum}", True, (255, 255, 255))
        screen.blit(counter_text, (765, 345))


        # Timer display: Time spent on current floor
        time_on_floor_text = font.render(f"Time on floor: {floorTimer:.1f} sec", True, (255, 255, 255))
        screen.blit(time_on_floor_text, (950, 345))
        current_time = pygame.time.get_ticks()
        if current_time > previous_time:
            floorTimer = (current_time - previous_time) / 1000.0


        #Elevator movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if 365 < floor1_pos.y < 370 and floor1Up == False:  #bug: cannot guarantee that elevator will be within this field only once; if the elevator goes slowly it can activate this twice
                floorNum += 1
                floor1Up = True
                floor2Up = False
                floor3Up = False
                previous_time = current_time
            elif 365 < floor2_pos.y < 370 and floor2Up == False:
                floorNum += 1
                floor2Up = True
                floor1Up = False
                floor3Up = False
                previous_time = current_time
            elif 365 < floor3_pos.y < 370 and floor3Up == False:
                floorNum += 1
                floor3Up = True
                floor2Up = False
                floor1Up = False
                previous_time = current_time
            floor1_pos.y += 300 * dt
            floor2_pos.y += 300 * dt
            floor3_pos.y += 300 * dt
        
        if keys[pygame.K_s]:
            if not (floorNum ==1 and floor1_pos.y<=0):  #is it at the bottom?
                if 365 < floor1_pos.y < 370 and floor1Down == False:
                    floorNum -= 1
                    floor1Down = True
                    floor2Down = False
                    floor3Down = False
                    previous_time = current_time
                elif 365 < floor2_pos.y < 370 and floor2Down == False:
                    floorNum -= 1
                    floor2Up = True
                    floor1Up = False
                    floor3Up = False
                    previous_time = current_time
                elif 365 < floor3_pos.y < 370 and floor3Down == False:
                    floorNum -= 1
                    floor3Down = True
                    floor2Down = False
                    floor1Down = False
                    previous_time = current_time
                floor1_pos.y -= 300 * dt
                floor2_pos.y -= 300 * dt
                floor3_pos.y -= 300 * dt
        
    
        if floor1_pos.y < 0:
            if floorNum==1: #checks to see if it can go any lower, no point in looping if its at the bottom
                floor1_pos.y=0
            else:
                floor1_pos.y = 720
        elif floor1_pos.y > 720:
            floor1_pos.y = 0


        if floor2_pos.y < 0:
            floor2_pos.y = 720
        elif floor2_pos.y > 720:
            floor2_pos.y = 0


        if floor3_pos.y < 0:
            floor3_pos.y = 720
        elif floor3_pos.y > 720:
            floor3_pos.y = 0
        #print(floor1_pos.y)


        if floorNum == 1:
            pygame.draw.rect(screen, "black", (0, floor3_pos.y + 2, 800, 720))
        
        if floorTimer > 1:  #how long before event happens on each floor
            if floor1_pos.y < player_pos.y < floor2_pos.y:
                    # Draw a white rectangle between floor1 and floor2
                    pygame.draw.rect(screen, "white", (400, floor1_pos.y, 200, floor2_pos.y - floor1_pos.y))
            elif floor2_pos.y < player_pos.y < floor3_pos.y:
                    # Draw a white rectangle between floor2 and floor3
                    pygame.draw.rect(screen, "white", (400, floor2_pos.y, 200, floor3_pos.y - floor2_pos.y))
            elif floor3_pos.y < player_pos.y < floor1_pos.y:
                    # Draw a white rectangle between floor3 and floor1
                    pygame.draw.rect(screen, "white", (400, floor3_pos.y, 200, floor1_pos.y - floor3_pos.y))

            pygame.draw.circle(screen, "red",(500, 260 + 100), 20)
            #imp = pygame.image.load("\\Mac\Home\Downloads\PlayMenu-1.png.png").convert()
    


        # flip() the display to put your work on screenw
        pygame.display.flip()

#home page

runninghome= True   #to keep the homepage working
while runninghome:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # to make sure you can close the window
            runninghome=False
    
    #paints first so that, when closed, goes straight to exiting
    screen.fill("black")
    font = pygame.font.SysFont("Arial", 48) #title text, edit later
    title = font.render("Two-Button Terror: The Elevator Job", True, (255, 255, 255))
    screen.blit(title, (300, 100))

    font= pygame.font.SysFont("Arial",32)
    play= font.render("Play (W)",True,(255,255,255))    #play button
    screen.blit(play,(450,350))

    options= font.render("Options (S)",True,(255,255,255))  #options button (hiscores, credits, how to play maybe)
    screen.blit(options,(470,450))                          #made only 2 buttons to keep with the 2 button motif

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        runninghome= False  #otherwise it would go back to homescreen when you try to close
        gameloop()
    elif keys[pygame.K_s]:
        print("options selected")
        #options()     #will work similar to gameloop()

pygame.quit()