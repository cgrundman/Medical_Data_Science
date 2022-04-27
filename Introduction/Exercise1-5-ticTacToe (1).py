import pygame
from pygame.locals import *
import numpy as np
# import random
# from copy import deepcopy

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 255, 0)


# Class which describes the board of TicTacToe
class Board:
    # list with all elements of the board
    list = None

    # different IDs
    player_id = 1
    computer_id = 2
    free_id = 0

    def __init__(self):
        self.empty_board()

    # Function empty_board(self)
    # Function to empty all values from the board. An empty board is represented by zeros. 
    # It should have the form of a list containing 3 lists. Each of the 3 lists is representing one row of the board.
    # 
    # Input arguments:
    # Output argument:
    def empty_board(self):
        # TODO: complete
        board = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):

        pass

    # Function make_move(self, player_id, i, j)
    # Function to make a move. Value of player is set to position (i,j) of the board if it is empty.
    # 
    # Input arguments:
    #    - [int] player_id: ID of the player which is doing the move
    #    - [int] i: i position of the move
    #    - [int] j: j position of the move
    # Output argument:
    #    - [bool] output: True, if it was a valid move, False if there is already a token.
    def make_move(self, player_id, i, j):
        # TODO: complete
        pass

    # Function is_there_free_space(self)
    # Function to determine if there is still some free space on the board.
    # 
    # Input arguments:
    # Output argument:
    #    - [bool] output: True, if there is a free space; False if not
    def is_there_free_space(self):
        # TODO
        # for row in range(BOARD_ROWS):
        #     for col in range(BOARD_COLS):
        #         if board[row][col] == 0:
        #             return False
        # if free_space is True:
        #     return True
        # else:
        #     return False
        pass

    # Function computer_random_move(self)
    # Function to make a random move by the computer. If there is a free space, a token is set at a random position.
    # 
    # Input arguments:
    # Output argument:
    #    - [bool] output: True, if there was a free space; False if not
    def computer_random_move(self):
        # TODO: complete
        pass

    # Function check_win(self, player_id):
    # Function to check if id has won the game.
    #
    #   Hint: Compare the current board with the win_states
    #   - Make a list of positions of tokens for ID
    #   - Check of the created list is a subset to any list in win_states
    # 
    # Input arguments:
    #   -[int] id: id of the player to check if he has one (1 = player; 2 = computer)
    # Output argument:
    #   -[bool] output: True, if id one; False if not
    def check_win(self, id):
        win_state = [[(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]]

        # TODO: complete
        pass

    #  -----------------> only implement this if you can play TicTacToe against random computer
    # Function test_win_move(self, player_id, i, j):
    # Function to check if a move made by id leads to a win.
    #
    #   Tasks:
    #   - Make a copy of the board
    #   - Set a token to the position
    #   - Check if it a win (test_win_move)
    # 
    # Input arguments:
    #   -[int] id: id of the player to check if he has one (1 = player; 2 = computer)
    #   -[int] i: i position of token
    #   -[int] j: j position of token
    #
    # Output argument:
    #   -[bool] output: True, if id one; False if not
    def test_win_move(self, id, i, j):
        # TODO: complete (only implement this if you can play TicTacToe against random computer)
        pass

    #  -----------------> only implement this if you can play TicTacToe against random computer
    # Function computer_move(self):
    # Function to make a  move by the computer. 
    #
    #   Tasks:
    #   Make a move checking the following things:   
    #       1) Check for a square that CPU can win on
    #       2) Check for square that player can win on
    #       3) Move on a free corner
    #       4) Move on free center
    #       5) Move on a free side
    # 
    # Input arguments:
    # Output argument:
    def computer_move(self):
        # TODO: complete (only implement this if you can play TicTacToe against random computer)
        pass


# Class which describes the game parameters of TicTacToe
class Game:
    # game parameters:
    window_width = 400
    window_height = 400
    element_width = window_width / 3
    element_height = window_height / 3
    gameboard = None
    turn = 1  # parameter to describe which turn it is. 1 = player, 2 = computer

    def __init__(self, board):
        self._running = True
        self._display_surf = None
        self.gameboard = board
        self.turn = 1

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE)
        pygame.display.set_caption('TicTacToe')
        self._running = True

    def on_render(self):
        if self.gameboard.list is None:
            return

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        self._display_surf.fill((0, 0, 0))

        # draw game board lines
        pygame.draw.line(self._display_surf, WHITE, [self.element_width, 0], [self.element_width, self.window_height],
                         3)
        pygame.draw.line(self._display_surf, WHITE, [self.element_width * 2, 0],
                         [self.element_width * 2, self.window_height], 3)

        pygame.draw.line(self._display_surf, WHITE, [0, self.element_height], [self.window_width, self.element_height],
                         3)
        pygame.draw.line(self._display_surf, WHITE, [0, self.element_height * 2],
                         [self.window_width, self.element_height * 2], 3)

        # draw game board elements
        for i, row in enumerate(self.gameboard.list):
            for j, element in enumerate(row):
                # print("(",i,",",j,"): ", element)
                if (element > 1):
                    pygame.draw.ellipse(self._display_surf, RED,
                                        [i * self.element_width, j * self.element_height, self.element_width,
                                         self.element_height])
                elif (element > 0):
                    pygame.draw.ellipse(self._display_surf, GREEN,
                                        [i * self.element_width, j * self.element_height, self.element_width,
                                         self.element_height])

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.turn = 1
        position = (0, 0)
        if self.on_init() == False:
            self._running = False

        print("Its your turn! Use your mouse ...")

        while (self._running):
            self.on_render()

            # pygame.event.pump()

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if (pygame.key.get_pressed()[K_ESCAPE]):
                    self._running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if (self.turn == 1):
                    x, y = self.get_element_cursor(position)
                    valid_move = self.gameboard.make_move(1, x, y)

                    if valid_move:
                        self.on_render()
                        self.turn = 2
                        # Check game over
                        if (self.is_game_over()):
                            self.restart_after_space()
                            return

                        # Computer randmom
                        self.gameboard.computer_random_move()

                        # Computer decision
                        # TODO uncomment if implemented
                        # self.gameboard.computer_move()

                        print("Computer made a decision.")
                        self.on_render()
                        self.turn = 1
                        # Check game over
                        if (self.is_game_over()):
                            self.restart_after_space()
                            return
                        print("Its your turn! Use your mouse ...")

    def restart_after_space(self):
        print("Press 'space' to restart_after_space ...")
        while (True):
            event = pygame.event.wait()
            if (pygame.key.get_pressed()[K_SPACE]):
                self.gameboard.empty_board()
                self.on_execute()
                return
            elif (pygame.key.get_pressed()[K_ESCAPE]):
                self.on_cleanup()
                return

    def get_element_cursor(self, position):
        x = int(position[0] // self.element_width)
        y = int(position[1] // self.element_height)
        return x, y

    def is_game_over(self):
        # Check if player has won
        if (self.gameboard.check_win(self.gameboard.player_id)):
            print("Player won!")
            return True

        # Check if computer has won
        if (self.gameboard.check_win(self.gameboard.computer_id)):
            print("Computer won!")
            return True

            # Check if board is full
        if (not self.gameboard.is_there_free_space()):
            print("There is no winner!")
            return True
        else:
            return False


if __name__ == "__main__":
    print("TicTacToe gestartet...")

    Board = Board()
    TicTacToe = Game(Board)
    TicTacToe.on_execute()
