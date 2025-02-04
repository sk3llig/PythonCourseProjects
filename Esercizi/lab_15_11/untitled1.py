# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:39:25 2023

@author: Leonardo
"""
import images
def create_matrix(R, C, value=(0,0,0)):
    '''
    with list comprehnsion
    '''
    if R > 0 and C > 0:
        return [ [value] * C for each_r in range(R) ]

colormap = { 'red': (255,0,0), 'blu': (0,0,255), 'green': (0,255,0),
            'black' : (0,0,0), 'white' : (255,255,255), 'yellow' : (255,255,0)
            }



prova=create_matrix(255,255)
def shape(mat):
    # immediatly check empty matrix
    if len(mat) == 0:
        return 0, 0
    if len(mat[0]) == 0:
        return 1, 0
    # rows corresponds to height
    r = len(mat)
    c = len(mat[0])
    return r, c


def draw_pix(im, x, y, col, W, H):
    # guarda per controllare se sbordiamo
    #if  0 <= x < W and 0 <= y < H: 
    im[y][x] = col

def draw_h_line(im, x, y, L, col, W, H):
    # for each_x in range(x,x+L):
        # draw_pix(im, each_x, y, col, W, H)
    ## modo piu compatto ma non controlliamo
    ## se sbordiamo, lo possiamo fare cmq
    im[y][x:x+L] = [col]*L
    
def draw_v_line(im, x, y, L, col, W, H):
    for each_y in range(y,y+L):
        draw_pix(im, x, each_y, col, W, H)
    ## va fatto un for per forza!
    
def draw_rect(img, x, y, Wr, Hr, col):
    
    # x,y -------------- x+Wr-1,y
    # |                     |
    # |                     |                                          
    # |                     |                     
    # |                     |                     
    # x,y+Hr-1,---------x+Wr-1,y+Hr-1
    
    # Hr- 1 ultimo elemento che va scritto
    
    H, W = shape(img)
    # H
    draw_h_line(img, x, y, Wr, col, W, H)
    draw_h_line(img, x, y+Hr-1, Wr, col, W, H)
    # V
    draw_v_line(img, x, y, Hr, col, W, H)
    draw_v_line(img, x+Wr-1, y, Hr, col, W, H)
    
    
draw_rect(prova, 10, 10, 100, 100, (255,255,255))
draw_rect(prova, 20, 20, 100, 100, (255,255,255))

    
images.save(prova,'prova.png')

    