# 'Clear Code' source: https://www.youtube.com/watch?v=QFvqStqPCRU

import pygame
import sys
import random
from pygame.math import Vector2

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        # head images
        self.head_up = pygame.image.load('Snake_Game/Images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Snake_Game/Images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Snake_Game/Images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Snake_Game/Images/head_left.png').convert_alpha()
        # tail images
        self.tail_up = pygame.image.load('Snake_Game/Images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Snake_Game/Images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Snake_Game/Images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Snake_Game/Images/tail_left.png').convert_alpha()
        # body images
        self.body_vertical = pygame.image.load('Snake_Game/Images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Snake_Game/Images/body_horizontal.png').convert_alpha()
        # body bend images 
        self.body_tr = pygame.image.load('Snake_Game/Images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Snake_Game/Images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Snake_Game/Images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Snake_Game/Images/body_bl.png').convert_alpha()
        # sound
        self.eat_sound = pygame.mixer.Sound('Snake_Game/Sound/Sound_eat.wav')
    
    def draw_snake(self) -> None:
        self.update_head_image()
        self.update_tail_image()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw a head
            if index == 0:
                screen.blit(self.head, block_rect)
            # fraw a tail
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            # draw a body
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
    
    def update_head_image(self) -> None:
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
    
    def update_tail_image(self) -> None:
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up
    
    def move_snake(self) -> None:
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self) -> None:
        self.new_block = True
    
    def play_sound(self) -> None:
        self.eat_sound.play()
    
    def reset(self) -> None:
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

class Fruit:
    def __init__(self) -> None:
        self.randomize()
        self.apple = pygame.image.load('Snake_Game/Images/apple.png').convert_alpha()
    
    def draw_fruit(self) -> None:
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.apple, fruit_rect)
    
    def randomize(self) -> None:
        # x and y positions of the fruit
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
        self.game_font = pygame.font.Font('Snake_Game/Font/PoetsenOne-Regular.ttf', 25)
        self.game_end = False
    
    def update(self) -> None:
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.speed_update()
    
    def draw_elements(self) -> None:
        if self.game_end == True:
            self.draw_grass()
            self.draw_score()
            self.draw_level()
            self.draw_final_screen()
        else:
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()
            self.draw_level()
    
    def check_collision(self) -> None:
        # snake eats a friut
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()
        # fruit appears under the body of the snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self) -> None:
        # snake hits a border of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self) -> None:
        self.game_end = True
    
    def draw_final_screen(self) -> None:
        self.draw_text('Game over',
                        DARK,
                        int(cell_size * cell_number / 2),
                        int(cell_size * cell_number / 2),
                        'midbottom')
        self.draw_text('Your score is ' + str(len(self.snake.body) - 3),
                        DARK,
                        int(cell_size * cell_number / 2),
                        int(cell_size * cell_number / 2),
                        'midtop')
        self.draw_text('Press ESC to exit',
                        DARK,
                        20,
                        int(cell_size * cell_number - 40),
                        'midleft')
        self.draw_text('Press ENTER to restart',
                        DARK,
                        int(cell_size * cell_number - 20),
                        int(cell_size * cell_number - 40),
                        'midright')
        while self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # quite and close the game window
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # restart the game
                        self.snake.reset()
                        self.game_end = False
                        self.speed_update()
                    if event.key == pygame.K_ESCAPE: # quite and close the game window
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(60)
    
    def draw_text(self, text: str, color: tuple, x: int, y: int, position: str) -> None:
        text_surface = self.game_font.render(text, True, color)
        match position:
            case 'midbottom':
                text_rect = text_surface.get_rect(midbottom = (x, y))
            case 'midtop':
                text_rect = text_surface.get_rect(midtop = (x, y))
            case 'midleft':
                text_rect = text_surface.get_rect(midleft = (x, y))
            case 'midright':
                text_rect = text_surface.get_rect(midright = (x, y))
            case 'center':
                text_rect = text_surface.get_rect(center = (x, y))
        screen.blit(text_surface, text_rect)

    def draw_grass(self) -> None:
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, DARK_GREENISH, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, DARK_GREENISH, grass_rect)
    
    def draw_score(self) -> None:
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, DARK)
        score_x = int(cell_size * cell_number - 40)
        score_y = 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_score_rect = pygame.Rect(apple_rect.left - 6, apple_rect.top - 2, apple_rect.width + score_rect.width + 14, apple_rect.height + 4)
        # draw a score background
        pygame.draw.rect(screen, DARK_GREENISH, bg_score_rect)
        # draw a frame of the score background
        pygame.draw.rect(screen, DARK, bg_score_rect, 2)
        # draw a score
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.apple, apple_rect)
    
    def draw_level(self) -> None:
        self.draw_text('Level ' + str((len(self.snake.body) - 3) // 15 + 1),
                        DARK,
                        20,
                        40,
                        'midleft')
    
    def speed_update(self) -> None:
        level = (len(self.snake.body) - 3) // 15
        pygame.time.set_timer(SCREEN_UPDATE, 170 - level * 20)
    
    def pause_game(self) -> None:
        self.draw_text('Press ESC to exit',
                        DARK,
                        20,
                        int(cell_size * cell_number - 40),
                        'midleft')
        self.draw_text('Press SPACE to continue',
                        DARK,
                        int(cell_size * cell_number - 20),
                        int(cell_size * cell_number - 40),
                        'midright')
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # quite and close the game window
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # restart the game
                        pause = False
                    if event.key == pygame.K_ESCAPE: # quite and close the game window
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(60)

GREENISH = (175, 215, 70)
DARK_GREENISH = (167, 209, 61)
DARK = (56, 74, 12)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 170)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quite and close the game window
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_SPACE: # pause the game
                main_game.pause_game()
    
    screen.fill(GREENISH) # set a color for the background
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) # game is never going to run faster than 60 frames per second
