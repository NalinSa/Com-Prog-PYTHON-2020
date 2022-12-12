# Prog-10: Steganography
# 6330268321 Narapat Wichob ?

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
    a=load_image(file_in)
    clone=clone_image(a)
    
    c=len(clone)*len(clone[0])
    
    if c<16+8*len(text)/3:
        return False
    else:
        x=''
        for e in SPECIAL_BITS: #ทำไมไม่ x += SPECIAL_BITS ไปเลย?
            x+=e
        long_word=int_to_bits(len(text))
        x+=long_word
        for e in text:
            x+=char_to_bits(e)
        for e in SPECIAL_BITS:
            x+=e
        for i in range(len(clone)):
            
            for j in range(len(clone[0])):
                for n in range(3):
                    for e in x:
                        if clone[i][j][n]%2==0 and e=='0':
                            clone[i][j][n]=clone[i][j][n]
                        elif clone[i][j][n]%2==0 and e=='1':
                            clone[i][j][n]=clone[i][j][n]+1
                        elif clone[i][j][n]%2==1 and e=='0':
                            clone[i][j][n]=clone[i][j][n]-1
                        elif clone[i][j][n]%2==1 and e=='1':
                            clone[i][j][n]=clone[i][j][n]
            
        save_image(clone,file_out)              
        return True


# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    a=load_image(file_in)
    s=''
    for i in range(len(a)):
        
        for j in range(len(a[i])):
            for n in range(3):
                if int(a[i][j][n]) %2==0:
                    s+='0'
                elif int(a[i][j][n])%2==1:
                    s+='1'
    s_binary=''
    for i in range(len(s)):
        
        s_binary+=s[i]
        if len(s_binary)==16:
            if s_binary == SPECIAL_BITS:
                break #เจอลำดับบิดพิเศษแล้ว
            
            else:
                s_binary=''
       
        elif i == len(s)-1:
            return ''
    count_bit=''
    
    for k in range(i+1,len(s)): #หาเลขฐานสอง 16 ตัวต่อมาเพื่อไปหาว่ามีกี่ตัวอักษรที่แฝงเข้ามา (len ของตัวที่แฝงมา)
        count_bit += s[k]
        if len(count_bit)==16:
            break
    b= bits_to_int(count_bit)
    c=''
    d=''
    for m in range(k+1,k+1+8*b):
        c+=s[m]
        if len(c)==8:
            d+=bits_to_char(c)
            c=''
    end_binary=''
    for i in range(m+1,m+1+16): #หาลำดับพิเศษ 16 ตัวท้าย
        if m+1+16>len(s):
            return ''
        else: end_binary+=s[i]
    if end_binary == SPECIAL_BITS:
        return d
    else:
        return ''
# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()