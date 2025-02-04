#!/usr/bin/env python
# coding: utf-8

# # Matrici

# In[1]:


## download di un po' di file dal corso del Prof. Sterbini che ci sono utili


# In[2]:


# get_ipython().system(' wget https://twiki.di.uniroma1.it/pub/Programmazione1/AA20_21/DiarioDelleLezioni-CanaleAL/png.py.txt &>/dev/null')


# In[3]:


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
        img = png.from_array(self.pixels, self.mode)                                                                                   
        b = io.BytesIO()                                                                                                           
        img.save(b)                                                                                                                
        return b.getvalue()


# ## Definizione di matrice

# In[6]:


matrix_2x1 = [ [0], [1] ] 

matrix_3x2 = [ [0,1], [1,2], [3,4] ] 


# ## Dimensioni di una matrice

# In[7]:


def shape(mat):
    # immediatly check empty matrix
    if len(mat) == 0 or len(mat[0]) == 0:
        return 0, 0
    # rows corresponds to height
    r = len(mat)
    c = len(mat[0])
    return r, c


# ## Plot

# In[8]:


def plot_mat(mat_rows):
    for r in mat_rows:
        print(r)


# In[9]:


shape(matrix_3x2)


# ## Funzione per creare matrice

# In[10]:


def create_matrix(r,c,value=0):
    # define matrix
    matrix = []
    # for each row
    for each_r in range(r):
        # define row
        row = []
        # for each col
        for each_c in range(c):
            # append the col to the row
            row.append(value)
        # append the row to the matrix
        matrix.append(row)
    return matrix    


# In[11]:


my_mat = create_matrix(20,20)


# In[12]:


plot_mat(my_mat)
shape(my_mat)


# In[13]:


plot_mat(matrix_3x2)


# In[14]:


## Forse posso utilizzare questo operatore [<content>] * n_times due volte?
[ [0] * 10 ] * 2


# ### Diverse funzioni per creare la matrice

# In[15]:


def create_matrix_short_wrong(r, c, value=0):
    '''
    WARNING: implementation is not correct since
    each row refers to the same row (shallow copy)
    '''
    return [ [value] * c] * r

def create_matrix_short_ok(r, c, value=0):
    '''
    a single for loop
    '''
    matrix = []
    for each_r in range(r):
        matrix.append([value] *c )
    return matrix

def create_matrix_lc(r, c, value=0):
    '''
    with list comprehnsion
    '''
    return [ [value] * c for each_r in range(r) ]

def create_matrix_map(r, c, value=0):
    '''
    with map and lambda function
    '''
    return list(map(lambda each_row: [value] * c, range(r)))


# ### Matrice non corretta (ha la solita riga referenziata R volte)wrong_mat = create_matrix_short(256, 256)

# In[16]:


wrong_mat = create_matrix_short_wrong(256, 256)


# In[17]:


shape(wrong_mat)


# In[18]:


# first plot, all is good, L is for telling renderer is a grayscale image
Image(wrong_mat,mode='L')


# In[19]:


# now writing a SINGLE pixel, why down there we get a column?
wrong_mat[128][128] = 255


# In[20]:


Image(wrong_mat,mode='L')


# In[21]:


## Controlliamo, cambio la shape cosi che controllo che supporto matrici non quadrate


# In[22]:


def check_mat(create_func, r , c, value=0):
    '''
    helper function to check matrix init
    and draw a small white pixel in the middle
    finally render back the image
    '''
    mat = create_func(r,c,value=value)
    half_r, half_c = r//2, c//2
    mat[half_r][half_c] = 255
    return Image(mat,mode='L')


# In[23]:


check_mat(create_matrix_short_wrong, 128, 256)


# In[24]:


check_mat(create_matrix_short_ok, 128, 256)


# In[25]:


check_mat(create_matrix_lc, 128, 256)


# In[26]:


check_mat(create_matrix_map, 128, 256)


# # Disegnare su Matrici/Immagini

# In[27]:


# maps names to colors in tuple
colormap = { 'red': (255,0,0), 'blu': (0,0,255), 'green': (0,255,0),
            'black' : (0,0,0), 'white' : (255,255,255) 
            }


# ### Disegnare linee (allineate agli assi)

# In[28]:


# let's create a 256x256x(3) of all black pixels
color_mat = create_matrix_lc(256, 256, colormap['black'])


# In[29]:


Image(color_mat)


# In[30]:


# come parametrizziamo una linea axis-aligned. Nota solo 3 gradi di liberta'
# line = x,y,length
# una linea e' definita con punto di inizio (x,y) e lunghezza


# In[31]:


def plot_line_h(mat, x, y, length, value):
    '''
    ricordarsi che mat
     e' indicizzata [riga][colonna] oppure [y][x]
    '''
    mat[y][x:x+length] = [value] * length
    
    
def plot_line_v(mat, x, y, length, value):
    ''''
    ricordarsi che mat
    e' indicizzata [riga][colonna] oppure [y][x].
    ci muoviamo su y; 
    andiamo da y fino a y+length, x rimane fissa
    '''
    for each_y in range(y,y+length):
        mat[each_y][x] = value
        
        
def plot_rect(mat, x , y , w , h, value, clip=False):
    '''
    plottiamo il rettangolo:
    1. upper segment
    2. lower segment
    3. left segment
    4. right segment
    '''
    def clip(v, min_v, max_v):
        return min(max(min_v, v), max_v)
    
    H, W = shape(mat)
    
    # clipping to borders to avoid under/over flow
    # for x,y and h,w
    if clip:
        x, y = clip(x, 0, W-1), clip(y, 0, H-1)
        w, h = clip(w, 0, W-1-x), clip(h, 0, H-1-y)
    
    # plotting
    plot_line_h(mat, x,   y,   w, value)   #1)
    plot_line_h(mat, x,   y+h-1, w, value) #2)
    plot_line_v(mat, x,   y,   h, value)   #3)
    plot_line_v(mat, x+w-1, y,   h, value) #4)


# In[32]:


## Plot prima linea


# In[33]:


color_mat = create_matrix_lc(256, 256, colormap['black'])
*line_h, = 64, 128, 128
plot_line_h(color_mat, *line_h, colormap['red'])
Image(color_mat)


# In[34]:


plot_line_v(color_mat, 128, 64, 128, colormap['red'])
Image(color_mat)


# ### Disegnare rettangoli

# In[35]:


color_mat_w = create_matrix_lc(256, 256, colormap['black'])


# In[36]:


# note we pass to the height a huge value, which is 2000 pixel but we handle the overflow internally
# to the function

plot_rect(color_mat_w, 64, 128, 64, 2000, colormap['white'])


# In[37]:


Image(color_mat_w)


# In[38]:


## all works if the rectangle is inside 
plot_rect(color_mat_w, 32, 32, 128, 64, colormap['white'])
Image(color_mat_w)


# In[39]:


## Download and rename a useful module from Prof. Sterbini codebase to load images from PNG


# In[40]:


get_ipython().system(' wget https://twiki.di.uniroma1.it/pub/Programmazione1/AA20_21/DiarioDelleLezioni-CanaleAL/images.py.txt &>/dev/null')


# In[41]:


get_ipython().system(' mv images.py.txt images.py')


# In[42]:


import images


# [for curious people, the story behind Lena picture](https://en.wikipedia.org/wiki/Lenna)

# In[43]:


lena = images.load('lena.png')
Image(lena)


# ### Flipping images (Ribaltarle orizzontalmente e verticalmente)

# In[44]:


def flip_v(img):
    '''
    Flipping the image wrt to the vertical axis
    we loop over each row and we create another image
    by inverting each row/line
    '''
    
    H, W = shape(img)
    flipped_img = []
    for each_y in range(H):
        flipped_img.append(img[each_y][::-1])
    return flipped_img

def flip_v_map(img):
    '''
    Flipping the image wrt to the vertical axis
    in a functional way.
    More complex: img refers to <list of <list>> as [ row_0, ...., row_n-1]
    I can pass the iterator img to map that will see each item as a row
    then I define a lambda function that takes the row and flips it
    either with [::-1] or I could have used reversed()
    '''
    return list(map(lambda each_r: each_r[::-1],img))


# In[45]:


flipped_img = flip_v(lena)
flipped_img_map = flip_v_map(lena)


# In[46]:


Image(flipped_img_map)


# In[47]:


# sanity check
flipped_img == flipped_img_map


# In[48]:


def flip_h(img):
    '''
    We loop in a reverse way wrt to the indexes of the rows
    in the meantime we add to a new image the rows of the first image.
    Given that we are looping in a reverse order we flip
    the images wrt to horizontal axis.
    '''
    
    H, W = shape(img)
    flipped_img = []
    for each_y_flip in reversed(range(H)): #range(H-1,-1,-1):
        flipped_img.append(img[each_y_flip][:])
    return flipped_img

def flip_h_map(img):
    '''
    Img refers to <list of <list>> as [ row_0, ...., row_n-1].
    What we have to do is simply "reshuffle" the order of the 
    rows to follow the reverse order.
    So what I can do is to treat the img as an iterator that I can
    just reverse immediatly. The function that process each item
    will return in the correct orect just the row.
    '''
    
    return list(map(lambda each_rr: each_rr, reversed(img)))


# In[49]:


flipped_img = flip_h(lena)
flipped_img_map = flip_h_map(lena)


# In[50]:


# sanity check
flipped_img == flipped_img_map


# # Shallow vs Deep Copy

# In[51]:


# Immutable objects

import copy
a = 'Supercalifragilistichespiralidoso'
b_s = copy.copy(a)
b_d = copy.deepcopy(a)
b = a

*sanity_check, = a is b_s, a is b_d, a is b
'passed!' if all(sanity_check) else 'against expectation'


# In[52]:


# More sense with mutable objects
import copy

# compound object
l = [ {'a': 1}, {'b': 2}, {'c': 3} ]

# shallow
l_sc1 = list(l)
l_sc2 = l.copy()
l_sc3 = l[:]
l_sc4 = copy.copy(l)

# deep
l_dc = copy.deepcopy(l)

def check_reference(obj_src,obj_dst,idx=0):
    return obj_src is obj_dst, obj_src[idx] is obj_dst[idx] 


# #### Shallow

# In[53]:


check_reference(l,l_sc1)


# In[54]:


check_reference(l,l_sc2)


# In[55]:


check_reference(l,l_sc3)


# In[56]:


check_reference(l,l_sc4)


# #### Deep copy

# In[57]:


check_reference(l,l_dc)


# ### with matrix, case more tricky

# In[58]:


small_mat = [ [0, 0, 0], [128, 128, 128] ]
small_mat_sc = small_mat.copy()


# In[59]:


small_mat[0][0] = 255


# In[60]:


small_mat == small_mat_sc


# In[61]:


small_mat_sc[1][0] = 0


# In[62]:


small_mat == small_mat_sc


# In[63]:


small_mat


# In[64]:


# if we do this, what happens to small_mat_sc? 
small_mat[0] = [255,255,255]


# In[65]:


small_mat


# In[66]:


small_mat_sc

