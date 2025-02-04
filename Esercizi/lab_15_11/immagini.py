
# coding: utf-8

# IMMAGINI

# In[1]:


## download di un po' di file dal corso del Prof. Sterbini che ci sono utili


# In[2]:


# get_ipython().system(' wget https://twiki.di.uniroma1.it/pub/Programmazione1/AA20_21/DiarioDelleLezioni-CanaleAL/png.py.txt &>/dev/null')


# # In[3]:


# get_ipython().system(' mv png.py.txt png.py')


# In[4]:


## Oggetto utile per visualizzare su ipython le immagini
## Nota ho modificato la classe per gestire anche immagini grayscale


# In[5]:



import png
import io 

# from Prof. Andrea Sterbini
class Image:                                                                                                                    
    '''Oggetto che contiene una immagine come lista di liste di colori (R,G,B) e che viene                                         
    direttamente visualizzate in IPython console/qtconsole/notebook col metodo _repr_png_'''  
    
    def __init__(self, img, mode='RGB'):                                                                                                       
        self.pixels = img  
        self.mode = mode

    def _repr_png_(self):                                                                                                          
        '''Produce la rappresentazione binaria della immagine in formato PNG'''                                                    
        if self.pixels:
            img = png.from_array(self.pixels, self.mode)                                                                                   
            b = io.BytesIO()                                                                                                           
            img.save(b)                                                                                                                
            return b.getvalue()


# In[6]:


## Download and rename a useful module from Prof. Sterbini codebase to load images from PNG


# In[7]:


# get_ipython().system(' wget https://twiki.di.uniroma1.it/pub/Programmazione1/AA20_21/DiarioDelleLezioni-CanaleAL/images.py.txt &>/dev/null')


# # In[8]:


# get_ipython().system(' mv images.py.txt images.py')


# %% Preliminari

import images


# [for curious people, the story behind Lena picture](https://en.wikipedia.org/wiki/Lenna)

# In[11]:


im = images.load('giotto_small.png')
Image(im)


# ## Shape di una matrice

# In[12]:


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


# %%% Colori come dizionario RGB

# maps names to colors in tuple
colormap = { 'red': (255,0,0), 'blu': (0,0,255), 'green': (0,255,0),
            'black' : (0,0,0), 'white' : (255,255,255), 'yellow' : (255,255,0)
            }


# 

# %%% Creare un'immagine

def create_matrix(R, C, value=(0,0,0)):
    '''
    with list comprehnsion
    '''
    if R > 0 and C > 0:
        return [ [value] * C for each_r in range(R) ]


# %%% Disegna un pixel
H, W = shape(im)
black = create_matrix(H, W, value=colormap['white'])
def draw_pix(im, x, y, col, W, H):
    # guarda per controllare se sbordiamo
    #if  0 <= x < W and 0 <= y < H: 
    im[y][x] = col

# %%% Disegna linea orizzontale

def draw_h_line(im, x, y, L, col, W, H):
    # for each_x in range(x,x+L):
        # draw_pix(im, each_x, y, col, W, H)
    ## modo piu compatto ma non controlliamo
    ## se sbordiamo, lo possiamo fare cmq
    im[y][x:x+L] = [col]*L
# %%%% Eval
line = [200,300,200] #x, y, L
draw_h_line(black, *line, colormap['green'], W, H)
images.visd(black)

# %%% Disegna linea verticale

def draw_v_line(im, x, y, L, col, W, H):
    for each_y in range(y,y+L):
        draw_pix(im, x, each_y, col, W, H)
    ## va fatto un for per forza!
# %%%% Eval
line = [300,200,200] #x, y, L
draw_v_line(black, *line, colormap['red'], W, H)
images.visd(black)


# %%% Controlliamo che i verdi siano davvero 200
assert sum(c == colormap['red'] for row in black for c in row) == 200, 'Errore!'

# %%% Disegna linea verticale con altra parametrizzazione

# inizio x1,y1
# finisce y2

# %%% Disegniamo un quadrato con soli bordi

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
    
# %%% Eval
draw_rect(black, 0, 0, W, H, colormap['red'])
images.visd(black)


# %%% rettangolo concentrici
H = 100
W = 50
black = create_matrix(H, W)
step = 2
den = 2

size = min(H,W)
for p in range(0,size//den,step):
    draw_rect(black, p, p, W-p-p, H-p-p, colormap['white'])
images.visd(black)
     

# %%% rettangolo pieno
black = create_matrix(H, W)
def fill_rect(im, x, y, Wr, Hr, col):
    H, W = shape(im)
    # x,y -------------- x+Wr-1,y
    # |-------------------- |
    # |                     |                                          
    # |                     |                     
    # |                     |                     
    # x,y+Hr-1,---------x+Wr-1,y+Hr-1
    for delta_h in range(Hr):
        draw_h_line(im, x, y+delta_h, Wr, col, W, H)

fill_rect(black, 0, 0, W, H, colormap['yellow'])
images.visd(black)

# %%% rettangolo concentrici pieni
black = create_matrix(H, W)
step = 2
keys = list(colormap.keys())
N = len(keys)
size = min(H,W)
for i, p in enumerate(range(0,size//2,step)):
    fill_rect(black, p, p, W-2*p, H-2*p, colormap[keys[i%N]])
images.visd(black)
     

# %% Trasformare Immagini
# %%% Flip Orizzontale

def flip_h(img):
    '''
    Img refers to <list of <list>> as [ row_0, ...., row_n-1].
    What we have to do is simply "reshuffle" the order of the 
    rows to follow the reverse order.
    So what I can do is to treat the img as an iterator that I can
    just reverse immediatly. The function that process each item
    will return in the correct orect just the row.
    Note: we optimized the function more to avoid calling the unused map
    
    [ r0
      r1
      ...
      rn-1
    ]
    
    becomes
    
    [ rn-1
      r0
      ...
      r1
    ]
    '''
    return list(reversed(img))

# %%% Flip Verticale

def flip_v(img):
    '''
    Flipping the image wrt to the vertical axis
    in a functional way.
    More complex: img refers to <list of <list>> as [ row_0, ...., row_n-1]
    I can pass the iterator img to map that will see each item as a row
    then I define a lambda function that takes the row and flips it
    either with [::-1] or I could have used reversed()
    '''
    return list(map(lambda r: r[::-1],img))

# ## Studiare cosa e' un PEP e vedere PEP 25
# 
# [PEP 257 -- Docstring Conventions ](https://www.python.org/dev/peps/pep-0257/)

# In[14]:


help(flip_h)



# %%% Ruotare Immagini

## Ruotare a sinistra

#          Sorgente
#    [c_0-- r_0 ------c_n-1]
#    [------ r_1 ----------]
#             .....
#    [------ r_n-1 --------]

# Destinazione (ragioniamo sulla riga i-esima)

# [c_0-- r_0 ------c_n-1] diventa la colonna

# [c_n-1
# ...
# ....
# c_0]

def rotate_left(im):
    return [ [im[r][c] for r in range(H)] for c in reversed(range(W))]
   
    
# %%% Ruota destra (PER CASA)
def rotate_right(im):
      pass


# %%% Trasporre matrice (scambiare righe con colonne)


matt = [ [1, 2, 3], [ 4, 5, 6], [7, 8, 9] ]

for row in matt: 
    print(row)


def transpose(im):
    H,W = shape(im)
    # blocco la riga C-estima prendi i valori dalle righe
    # li rimetto come righe nella nuova matrice
    return [ [ im[r][c] for r in range(H)] for c in range(W)  ] 

# %%% Stampa matrice senza for
mat_t = transpose(matt)
print(*mat_t,sep='\n')
# %%% Transposta funzione anche sulle immagini
images.visd(transpose(im))
# %%% Altri modi di trasporre/ruotare in programmazione funzional

images.visd((list(zip(*im))))
# %%% Mantiene lista di liste
trasposta = list(map(list,zip(*im)))
# mantiene struttura dati lista di liste
images.visd(trasposta)
# %%% Ruota a sinistra (trasposto e poi flip orizzontale)
left = list(reversed(list(map(list,zip(*im)))))
images.visd(left)

# %%% Ruota a Destra con zip (PER CASA)
right = None
#images.visd(right)

# %% Elaborazione Immagini


# %%%% Ritaglia immagine con input rettangolo

def crop(im, x, y, w, h):
    H, W = shape(im)
    return [ [c for c in row[x:x+w]] for row in im[y:y+h]]


images.visd(crop(im,0,0,W//2,H//2))
H,W = shape(im)
# %%% Quattro ritagli
meta_W = W//2
meta_H = H//2
list_W = [0, meta_W ]
list_H = [0, meta_H ]
images_list = []
for h in list_H:
    for w in list_W:
        cropim = crop(im,w,h,meta_W,meta_H)
        # le marco di giallo cosi poi vedo come sono rimesse insieme
        draw_rect(cropim,0, 0, meta_W, meta_H, colormap['yellow'])
        images_list.append(cropim)


for i in images_list:
    images.visd(i)

somma_sotto_img = sum(map(lambda mat: len(mat)*len(mat[0]),images_list))
assert somma_sotto_img == W*H, 'Stai  tagliando troppo'

# %%% ConCat images

images_list

def concat(img_list):
     # TODO: concatena sulle righe
     # NON appena si finisce la N-esima righa di TUTTE le matrici scrive nuova riga
     return [ [v for row in rows for v in row] for rows in  zip(*img_list) ]
         
images.visd(concat(images_list))

# %%% Cut and paste
def cut_paste(im, rect_crop, x, y):
    '''
    rect crop is x, y, w, h
    '''
    H, W = shape(im)
    # si croppa
    cropped = crop(im,*rect_crop)
    w = len(cropped[0])
    assert w == rect_crop[2]
    # si inserisce nel posto giusto
    for delta_y in range(len(cropped)):
        im[y+delta_y][x:x+w] = cropped[delta_y]
    # si puo anche scrivere con enumerate
    # for delta_y, row in enumerate(cropped):
    #     im[y+delta_y][x:x+w] = row
    return im
images.visd(cut_paste(im,[100,250,100,100], meta_W, meta_H))


# %%%% Trasforma in scala di grigi
im = images.load('giotto_small.png')
# per trasformare una immagine in livelli di grigio
def gray(im):
    return [[ (sum(c)//3,)*3 for c in row] for row in im ]

images.visd(gray(im))

# %%% Applico un filtro generico (passo una funzione)

def filtro_null(pix):
    return pix

def filter_im(im, filter_func):
    return [[ filter_func(c) for c in row] for row in im ]

images.visd(filter_im(im,filtro_null))


# %%% Applico un filtro aumenta intensita'
def luminosita(pix,k):
    def clip(p):
        return max(min(int(round(p*k)),255),0)
    return tuple(clip(p) for p in pix)

def filter_im(im, filter_func, k):
    return [[ filter_func(c,k) for c in row] for row in im ]

images.visd(filter_im(im,luminosita,20))

# %%% Shuffling (putting noise in the image)
import random
def shuffle(im,x,y, H, W, size=20):
    rx = random.randint(-size, size)
    ry = random.randint(-size, size)
    xx = x + rx
    yy = y + ry
    pix = im[y][x]
    if 0 <= xx < W and 0 <= yy < H:
        pix = im[yy][xx]
    return pix
    
# %%% Blurring
from tqdm import tqdm
def blur(im,x, y, H, W, k=5):
    # k=1;x=0 si fa -1, 0, +1 compreso
    somma = 0, 0, 0
    count = 0
    for xx in range(x-k,x+k+1):
        for yy in range(y-k,y+k+1):
            if 0 <= xx < W and 0 <= yy < H:
                pix = im[yy][xx]
                somma = tuple(map(lambda s,p: s+p, somma,pix))
                count += 1 
    return tuple(map(lambda s: min(max(s//count,0),255), somma))
    
    
def filter_im(im, filter_func):
    H, W = shape(im)
    return [[ filter_func(im,x,y, H, W) for x, c in enumerate(row)] 
            for y, row in tqdm(enumerate(im),desc='blurring',total=H) ]
images.visd(filter_im(im,blur))


# %% PER CASA: Dati i rettangoli definiti nella lista list_rect
# calcolarsi il rettangolo R di area minima che li racchiude tutti
# e disegnare R con colore (255,255,255) usando la funzione sopra fill_rect.
# Poi successivamente disegnare i rettangoli nella list_rect sempre usando
# fill_rect
# I rettangoli sono in formato
# pixel top left= (x1,y1) e bottom right (x2,y2) e
# c e' il colore come tupla rgb
# rettangolo (1,1,20,19,(255, 0, 0)) indica il rettangolo che parte dal punto
# in alto a sx (1,1) e termina a (20,19) compreso di colore rosso ossia
# (255, 0, 0).
# rettangolo = (x1,y1,x2,y2,c)
# provate a disegnare nell ordine suddetto in un un' immagine
# tutte nera con 300 colonne e 300 righe.
list_rect = [(210, 210, 210, 210 ,(255, 0, 0)),
             (50, 100, 100, 200, (255, 255, 0)),
             (220, 50, 250, 99, (255, 0, 255)),
             (150, 80, 150, 190, (0, 128, 0))
             ]


# %% PER CASA: cambiare il codice di prima in maniera che crei
# una classe per i rettangoli e per i colori e usi oggetti nella sua esecuzione.



# %% PER CASA: Per i piu coraggiosi ed esperti. scrivere la funzione
#di prima che disegna (senza classi va bene) SENZA cicli ma solo usando
# map, zip, lambda etc
