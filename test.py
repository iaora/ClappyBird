import pygame
import os

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done = False
is_blue = True

x = 30
y = 30


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(10, 10, 100, 100), 10)
    
    # Add this somewhere after the event pumping and before the display.flip()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    if is_blue: 
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    # reset screen to black before draw the rectangle
    screen.fill((0, 0, 0))
    screen.blit(get_image('person.png'), (20, 20))
    #pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    clock.tick(60)
        
    pygame.display.flip()
