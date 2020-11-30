from pygame.locals import *
import pygame
import random


class Player:
    prev_x = 1
    prev_y = 1

    x = 2
    y = 2
    speed = 1

    score = 0


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
        self.M = 20
        self.N = 20
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
                     1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 1,
                     1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1,
                     1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 2, 0, 0, 2, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 2, 1, 1,
                     1, 1, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def drawQuestion(self, display_surf, question):

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        _question_surf = myfont.render(question[0], False, (255, 255, 255))
        display_surf.blit(_question_surf, (0, 900))
        _multiple_choice_a_surf = myfont.render(question[1], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_a_surf, (0, 950))
        _multiple_choice_b_surf = myfont.render(question[2], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_b_surf, (0, 1000))
        _multiple_choice_c_surf = myfont.render(question[3], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_c_surf, (0, 1050))
        _multiple_choice_d_surf = myfont.render(question[4], False, (255, 255, 255))
        display_surf.blit(_multiple_choice_d_surf, (0, 1100))


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
            random_number = random.randint(1, 27)
            print("The random number is: ")
            print(random_number)
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

        font_for_score = pygame.font.SysFont('Comic Sans MS', 30)
        score_label_surf = font_for_score.render('Score', False, (255, 255, 255))
        score_surf = font_for_score.render(str(player.score), False, (255, 255, 255))
        display_surf.blit(score_label_surf, (1000, 0))
        display_surf.blit(score_surf, (1000, 50))

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

                    # clear the previous score by drawing it in black
                    score_surf = font_for_score.render(str(player.score), False, (0, 0, 0))
                    display_surf.blit(score_surf, (1000, 50))

                    # increment the new score
                    player.score = player.score + 100

                    # display the new score in white
                    score_surf = font_for_score.render(str(player.score), False, (255, 255, 255))
                    display_surf.blit(score_surf, (1000, 50))

                    pygame.display.flip()
                    break




class Questions:
#    question1 = ['What is your name?', 'a) Daniel', 'b) Eliana', 'c) Michaela', 'd) David', 'c']
#    question2 = ['How old are you?', 'a) 16', 'b) 14', 'c) 12', 'd) 9', 'c']
#    question3 = ['What is your favorite color?', 'a) blue', 'b) green', 'c) red', 'd) orange', 'b']
    question1 = ['Where was ponyboy coming from when he got jumped by the Socs?' , 'a) Home' , 'b) School' , 'c) The Movies' , 'd) The Park' , 'c']
    question2 = ['What happened to Ponyboy\'s parents?' , 'a) they died in a car accident' , 'b) They abandoned Ponyboy and his brothers' , 'c) They died in a fire' , 'd) They abuse Ponyboy' , 'a']
    question3 = ['Who was Ponyboy\'s oldest brother?' , 'a) Soda Pop' , 'b) Dally', 'c) Johnny' , 'd) Darry' , 'd']
    question4 = ['Who does Cherry say she could fall in love with?' , 'a) Ponyboy' , 'b) Dally' , 'c)darry' , 'd) Johnny' , 'b']
    question5 = ['How did Johnny change after getting jumped by the Socs?' , 'a) He carries a 6-inch switchblade with him everywhere' , 'b)  he scares more easily' , 'c) he never walks alone' , 'd) all of the above' , 'd']
    question6 = ['What do Cherry and Ponyboy both watch?' , 'a) sunsets' , 'b) video games' , 'c) star wars' , 'the NBA' , 'a']
    question7 = ['Who says that money is not the only thing that separates the Greasers from the Socs?' , 'a) Ponyboy' , 'b) Randy' , 'c) Cherry' , 'd) Marcia' , 'c']
    question8 = ['What does Ponyboy visualize as a fantasy life?' , 'a) life in the country' , 'b) no gangs' , 'c) Parents still alive' , 'd) all of the above' , 'd']
    question9 = ['Why does Ponyboy run out of the house at 2 am?' , 'a) Because Darry slapped him and yelled at him for getting home so late' , 'b) to meet up with Cherry' , 'c) to fight with Bob' , 'd) to fo to a club' , 'a']
    question10 = ['Why did Johnny stab Bob?' , 'a) Bob was trying to drown a Ponyboy with some of the other Socs ' , 'b) Johnny didnt like Bob' , 'c) Bob was about to kill Johnny' , 'd) Bob was about stab two-bit' , 'a']
    question11 = ['How did Johnny and Ponyboy get to Windrixville?' , 'a) car' , 'b) train' , 'c) plane' , 'd) by foot' , 'b']
    question12 = ['Where did Ponyboy and Johnny hide in windrixville?' , 'a) in a car' , 'b) in a cafe' , 'c) in an abandoned church' , 'd) on the streets' , 'c']
    question13 = ['What book do Johnny and Ponyboy read while hiding in the abandoned church?' , 'a) Gone With the Wind' , 'b) Angels and Demons' , 'c) Gone With the Rain' , 'd) Gone With the Time' , 'a']
    question14 = ['What does dally do to scare off the socs?' , 'a) carries an unloaded gun' , 'b) gets fake vampire teeth' , 'c) carries a knife' , 'd) wears chains' , 'a']
    question15 = ['Who is a spy for the greasers now?' , 'a) cherry' , 'b) Bob' , 'c) Randy' , 'd) Marcia' , 'a']
    question16 = ['What is Ponyboys biggest fear?' , 'a) dying' , 'b) running away from home' , 'c) killing someone' , 'd) being put in a boys home' , 'd']
    question17 = ['What sport does Pony participate in?' , 'a) basketball' , 'b) football' , 'c) track' , 'd) soccer' , 'c']
    question18 = ['True or false: Dally is relieved that he won’t be in the rumble.' , 'a) true' , 'b) False' , 'c) neither' , 'd) both' , 'b']
    question19 = ['What does Johnny ask Two-Bit to bring him?' , 'a) a switchblade' , 'b) a copy of Gone With the Wind' , 'c) His mothers necklace' , 'd) a cigarette' , 'b']
    question20 = ['When Johnnys mother came to visit him at the hospital, what was Johnnys reaction?' , 'a) he was happy to see her' , 'b) he was sleeping' , 'c) he wished his father had come instead' , 'd) he didnt want to see her' , 'd']
    question21 = ['Who was the youngest one at the rumble?' , 'a) Ponyboy' , 'b) Randy' , 'c) Johnny' , 'd) Soda' , 'a']
    question22 = ['Who won the rumble?' , 'a) greasers' , 'b) Socs' , 'c) they didnt end up fighting' , 'd) they both ran away' , 'a']
    question23 = ['Why did dally and ponyboy go to the hospital after the fight?' , 'a) to see Johnny' , 'b) ' , 'c) ' , 'd) ' , '']
    question24 = ['What news does Pony tell the guys?' , 'a) That Johnny died' , 'b) That Dally was shot' , 'c) That he is going to run away' , 'd) That Darry was killed in the rumble' , 'a']
    question25 = ['How did Dally deal with the death of Johnny?' , 'a) he robbed a store' , 'b) he ran away' , 'c) he broke down crying' , 'd) he killed Randy' , 'a']
    question26 = ['Who came to visit Ponyboy at his house while he was recovering?', 'a) Bob', 'b) Randy', 'c) Johnny', 'd) Two Bit', 'b']
    question27 = ['Who speaks to the judge before the hearing begins?', 'a) Ponyboy', 'b) Randy', 'c) Johnny', 'd) Cherry', 'a']

    questionsHashMap = {}
    questionsHashMap[1] = question1
    questionsHashMap[2] = question2
    questionsHashMap[3] = question3
    questionsHashMap[4] = question4
    questionsHashMap[5] = question5
    questionsHashMap[6] = question6
    questionsHashMap[7] = question7
    questionsHashMap[8] = question8
    questionsHashMap[9] = question9
    questionsHashMap[10] = question10
    questionsHashMap[11] = question11
    questionsHashMap[12] = question12
    questionsHashMap[13] = question13
    questionsHashMap[14] = question14
    questionsHashMap[15] = question15
    questionsHashMap[16] = question16
    questionsHashMap[17] = question17
    questionsHashMap[18] = question18
    questionsHashMap[19] = question19
    questionsHashMap[20] = question20
    questionsHashMap[21] = question21
    questionsHashMap[22] = question22
    questionsHashMap[23] = question23
    questionsHashMap[24] = question24
    questionsHashMap[25] = question25
    questionsHashMap[26] = question26
    questionsHashMap[27] = question27



class App:
    windowWidth = 1200
    windowHeight = 1700
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
        self._coin_surf = pygame.image.load("coin2.png")
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