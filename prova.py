import pygame
 
screen = pygame.display.set_mode((800,600))
GREEN = (0, 255, 0)
BLACK = (255, 255, 255)
FPS = 60
dis_width = 800
dis_height  = 600
segment_width = 15
segment_height = 15
x_change = segment_width 
y_change = 0
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
pygame.init()
screen.fill(BLACK)
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Wang Yanchen Test')
allspriteslist = pygame.sprite.Group()
snake_segments = []
for i in range(30):
    x = 600 - (segment_width ) * i
    y = 300
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
    clock = pygame.time.Clock()
done = False
 
while not done:
    for event in pygame.event.get():
        screen.fill(BLACK)
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width) * -1 
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width )
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height)
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        done = True   
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
    x = snake_segments[0].rect.x + x_change 
    y = snake_segments[0].rect.y + y_change 
    segment = Segment(x, y)
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
    screen.fill(BLACK)
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(5)
 
pygame.quit()