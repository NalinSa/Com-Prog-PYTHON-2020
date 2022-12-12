# Prog-10: Steganography
# 6330271121 Nalin Baipluthong

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename):       
    im = Image.open(filename).convert('RGB') 
    return numpy.asarray(im).tolist()  
    
def save_image(img, filename):    
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
  
def show_image(filename):       
    im = Image.open(filename) 
    im.show() 

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------



# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    img1 = load_image( file_in )
    if (16+8*(len(text))/3)<= len(img1)*len(img1[0]):
        count = int_to_bits(len(text))
        want = ''
        for ch in text:
            want += char_to_bits(ch)
        al = SPECIAL_BITS + count + want + SPECIAL_BITS
        img2 = clone_image( img1 )
        b = 0
        T = False
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                for k in range(len(img2[0][0])):
                    if b >= len(al):
                        T = True
                        break
                    elif img1[i][j][k]%2 == 0:
                        if al[b]=='0':
                            img2[i][j][k] = img1[i][j][k]
                        elif al[b]=='1':
                            img2[i][j][k] = img1[i][j][k]+1
                    else:
                        if al[b]=='0':
                            img2[i][j][k] = img1[i][j][k]-1
                        elif al[b]=='1':
                            img2[i][j][k] = img1[i][j][k]
                    b += 1
                if T: break
            if T: break
        save_image(img2, file_out)
        return True
    
    else: return False

# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    img = load_image( file_in )
    al = ''
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(len(img[0][0])):
                if img[i][j][k]%2 == 0:
                    al += '0'
                else: al += '1'
    if al[:16:] != SPECIAL_BITS:
        return ''
    else:
        if 0<=bits_to_int(al[16:32:])<=65535:
            c = bits_to_int(al[16:32:])
            want = ''
            for i in range(32,32+8*c,8):
                want += bits_to_char(al[i:i+8:])
            if al[32+8*c:48+8*c:] ==  SPECIAL_BITS:
                return want
            else: return ''
        else:
            return '' 

# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
embed_text_to_image('9'*900, 'gear.png', 'gear1.png')
t = get_embedded_text_from_image('gear1.png')
print(t=='9'*900)
main()