from pygame.locals import *
import pygame


class Player:
    prev_x = 1
    prev_y = 1

    x = 1
    y = 1
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

    def draw(self, display_surf, image_surf, coin_surf, player_surf, player):

        # check for collision with the wall
        if self.maze[player.x + (player.y*self.M)] == 1:
            # collision with a wall so reset player x and y to previous values
            player.x = player.prev_x
            player.y = player.prev_y
        else:
            # no collision with wall so set the player previous x and y values to the current
            player.prev_x = player.x
            player.prev_y = player.y

        # check for collision with coin
        if self.maze[player.x + (player.y * self.M)] == 2:
            print("COLLISION")
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
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Michaelas awesome maze')
        self._running = True
        self._coin_surf = pygame.image.load("coin.jpg")
        self._player_surf = pygame.image.load("player.png")
        self._block_surf = pygame.image.load("block.png").convert()
        print("GKGKGK")
        print(self._player_surf.get_rect())

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        #self._display_surf.blit(self._player_surf, (self.player.x, self.player.y))
        self.maze.draw(self._display_surf, self._block_surf, self._coin_surf, self._player_surf, self.player)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False



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

#            if (keys[K_RIGHT] and self.K_RIGHT_PRESSED == 0):
#                self.player.moveRight()

#            if (keys[K_LEFT]):
#                self.player.moveLeft()

#            if (keys[K_UP]):
#                self.player.moveUp()

#            if (keys[K_DOWN]):
#                self.player.moveDown()

#            if (keys[K_ESCAPE]):
#                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()