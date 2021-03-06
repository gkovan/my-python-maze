from pygame.locals import *
import pygame
import random


class Player:
    prev_x = 1
    prev_y = 1

    x = 2
    y = 2
    speed = 1

    def moveRight(self):
        self.x = self.x + 1

    def moveLeft(self):
        self.x = self.x - 1

    def moveUp(self):
        self.y = self.y - 1

    def moveDown(self):
        self.y = self.y + 1

class Maze:
    def __init__(self):
        self.M = 10
        self.N = 8
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 2, 0, 0, 2, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 2, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

    def drawQuestion(self, display_surf, question):

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        _question_surf = myfont.render(question[0], False, (255, 255, 255))
        display_surf.blit(_question_surf, (0, 400))
        _multiple_choice_a_surf = myfont.render(question[1], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_a_surf, (0, 450))
        _multiple_choice_b_surf = myfont.render(question[2], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_b_surf, (0, 500))
        _multiple_choice_c_surf = myfont.render(question[3], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_c_surf, (0, 550))
        _multiple_choice_d_surf = myfont.render(question[4], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_a_surf, (0, 600))


    def draw(self, display_surf, image_surf, coin_surf, player_surf, player, questions):

        # check for collision with the wall
        if self.maze[player.x + (player.y*self.M)] == 1:
            # collision with a wall so reset player x and y to previous values
            player.x = player.prev_x
            player.y = player.prev_y
        else:
            # no collision with wall so set the player previous x and y values to the current
            player.prev_x = player.x
            player.prev_y = player.y

        need_answer = False
        # check for collision with coin
        if self.maze[player.x + (player.y * self.M)] == 2:
            print("COLLISION")
            need_answer = True
            random_number = random.randint(1, 3)
            question = questions.questionsHashMap[random_number]
            self.drawQuestion(display_surf, question)
            self.maze[player.x + (player.y * self.M)] = 0

        display_surf.blit(player_surf, (player.x * 44, player.y * 44))
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * 44, by * 44))

            if self.maze[bx + (by * self.M)] == 2:
                display_surf.blit(coin_surf, (bx * 44, by * 44))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1

        pygame.display.flip()

        if need_answer:
            need_answer = False
            correct_answer = question[5];
            print("The correct answer is: " + correct_answer)
            user_answer = 'z'
            correct = False
            while not correct:
                events = pygame.event.get()
                for event in events:
                    print(event)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            user_answer = 'a'
                            print("pressed a")
                        if event.key == pygame.K_b:
                            user_answer = 'b'
                        if event.key == pygame.K_c:
                            user_answer = 'c'
                        if event.key == pygame.K_d:
                            user_answer = 'd'

                        print("User answer is: " + user_answer)

                if user_answer == correct_answer:
                    correct = True
                    print ("HOORAAY. You got the correct answer.")
                    break




class Questions:
    question1 = ['What is your name?', 'a) Daniel', 'b) Eliana', 'c) Michaela', 'd) David', 'c']
    question2 = ['How old are you?', 'a) 16', 'b) 14', 'c) 12', 'd) 9', 'c']
    question3 = ['What is your favorite color?', 'a) blue', 'b) green', 'c) red', 'd) orange', 'b']
    questionsHashMap = {}
    questionsHashMap[1] = question1
    questionsHashMap[2] = question2
    questionsHashMap[3] = question3




class App:
    windowWidth = 800
    windowHeight = 800
    player = 0
    K_RIGHT_PRESSED = 0
    K_LEFT_PRESSED = 0
    K_UP_PRESSED = 0
    K_DOWN_PRESSED = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._question_surf = None
        self.player = Player()
        self.maze = Maze()
        self.questions = Questions()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._coin_surf = pygame.image.load("coin.jpg")
        self._player_surf = pygame.image.load("player.png")
        self._block_surf = pygame.image.load("block.png").convert()

        pygame.font.init()


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.maze.draw(self._display_surf, self._block_surf, self._coin_surf, self._player_surf, self.player, self.questions)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        # draw the initial maze state
        self.on_render()

        while (self._running):
            pygame.event.pump()
            pygame.key.set_repeat(5000)
            keys = pygame.key.get_pressed()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()
                    if event.key == pygame.K_UP:
                        self.player.moveUp()

                    # redraw the maze only when an event (user pushed an arrow key) occurs
                    self.on_loop()
                    self.on_render()


        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()