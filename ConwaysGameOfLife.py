#!/usr/bin/env python3

#Pygame implementation of Conways Game of Life, with basic ruleset

import os, sys
import time
import pygame as pg

class Game:
    def __init__(self, size):
        self.size = size
        pg.display.init()
        pg.font.init()
        self.window = pg.display.set_mode((self.size * 20, self.size * 20))
        pg.display.set_caption("Conways Game of Life")
        self.board = [[(0, 0, 0) for i in range(self.size)] for j in range(self.size)]
        self.next_board = [[(0, 0, 0) for i in range(self.size)] for j in range(self.size)]
        self.mouse_pos = ()
        self.start_sim = False

    def update(self):
        for i in range(self.size):
            for j in range(self.size):
                pg.draw.rect(self.window, self.board[i][j], (i*20, j*20, 20, 20))
        if self.mouse_pos:
            pg.draw.rect(self.window, (255, 255, 255), (self.mouse_pos[0]//20*20, self.mouse_pos[1]//20*20, 20, 20))
        if self.start_sim:
            self.calculate(self.board, self.next_board)
        pg.display.update()

    def calculate(self, BOARD, NEXT_BOARD):
        live_neighbors = 0
        neighbors = []
        for i in range(self.size):
            for j in range(self.size):
                if j == self.size - 1:
                    if i == self.size - 1:
                        neighbors.append(BOARD[i-1][j])
                        neighbors.append(BOARD[i-1][j-1])
                        neighbors.append(BOARD[i][j-1])
                    elif i == 0:
                        neighbors.append(BOARD[i+1][j])
                        neighbors.append(BOARD[i+1][j-1])
                        neighbors.append(BOARD[i][j-1])
                    else:
                        neighbors.append(BOARD[i][j-1])
                        neighbors.append(BOARD[i+1][j])
                        neighbors.append(BOARD[i+1][j-1])
                        neighbors.append(BOARD[i-1][j])
                        neighbors.append(BOARD[i-1][j-1])
                elif j == 0:
                    if i == self.size - 1:
                        neighbors.append(BOARD[i-1][j])
                        neighbors.append(BOARD[i-1][j+1])
                        neighbors.append(BOARD[i][j+1])
                    elif i == 0:
                        neighbors.append(BOARD[i+1][j])
                        neighbors.append(BOARD[i+1][j+1])
                        neighbors.append(BOARD[i][j+1])
                    else:
                        neighbors.append(BOARD[i][j+1])
                        neighbors.append(BOARD[i+1][j])
                        neighbors.append(BOARD[i+1][j+1])
                        neighbors.append(BOARD[i-1][j])
                        neighbors.append(BOARD[i-1][j+1])
                elif i == self.size - 1 and j != 0 and j != self.size - 1:
                    neighbors.append(BOARD[i][j-1])
                    neighbors.append(BOARD[i][j+1])
                    neighbors.append(BOARD[i-1][j])
                    neighbors.append(BOARD[i-1][j-1])
                    neighbors.append(BOARD[i-1][j+1])
                elif i == 0 and j != 0 and j != self.size - 1:
                    neighbors.append(BOARD[i][j-1])
                    neighbors.append(BOARD[i][j+1])
                    neighbors.append(BOARD[i+1][j])
                    neighbors.append(BOARD[i+1][j+1])
                    neighbors.append(BOARD[i+1][j-1])
                else:
                    neighbors.append(BOARD[i][j+1])
                    neighbors.append(BOARD[i][j-1])
                    neighbors.append(BOARD[i+1][j])
                    neighbors.append(BOARD[i-1][j])
                    neighbors.append(BOARD[i+1][j+1])
                    neighbors.append(BOARD[i+1][j-1])
                    neighbors.append(BOARD[i-1][j+1])
                    neighbors.append(BOARD[i-1][j-1])
                live_neighbors = neighbors.count((255, 255, 255))
                if BOARD[i][j] == (0, 0, 0):
                    if live_neighbors == 3:
                        NEXT_BOARD[i][j] = (255, 255, 255)
                    else:
                        NEXT_BOARD[i][j] = (0, 0, 0)
                elif BOARD[i][j] == (255, 255, 255):
                    if live_neighbors < 2:
                        NEXT_BOARD[i][j] = (0, 0, 0)
                    elif live_neighbors > 3:
                        NEXT_BOARD[i][j] = (0, 0, 0)
                    else:
                        NEXT_BOARD[i][j] = (255, 255, 255)
                live_neighbors = 0
                neighbors.clear()
        for m in range(self.size):
            for n in range(self.size):
                    BOARD[m][n] = NEXT_BOARD[m][n]
        NEXT_BOARD = [[(0, 0, 0) for i in range(self.size)] for j in range(self.size)]

    def run(self):
        running = True
        while running:
            self.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEMOTION:
                    self.mouse_pos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    x, y = pos[0]//20, pos[1]//20
                    self.board[x][y] = (255, 255, 255)
                if event.type == pg.KEYDOWN:
                    if chr(event.key) == " ":
                        self.start_sim = True

        pg.quit()
        quit()

Game(50).run()
