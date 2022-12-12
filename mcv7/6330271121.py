# Prog-07: EAN-13 Barcode
# 6330271121 Nalin Baipluthong

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):       
    x = [[int(e) for e in ean13_code]] 
    plt.axis('off')  
    plt.imshow(x, aspect='auto', cmap='binary')    
    plt.title(digits)    
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')  
    codes = encode_EAN13(digits)       
    if codes == '': 
        print(digits, 'is not an EAN-13 number.') 
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================
pat = ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG', \
       'LGGGLL','LGLGLG','LGLGGL','LGGLGL']

def codes_of(digits, patterns):
    codes = ''
    for i in range(len(digits)):
        if patterns[i]=='L':
            codes += L_codes[int(digits[i])]
        elif patterns[i]=='G':
            codes += G_codes[int(digits[i])]
        elif patterns[i]=='R':
            codes += R_codes[int(digits[i])]
    return codes    

def digits_of(codes):
    digits = ''
    for i in range(0,len(codes),7):
        if codes[i:i+7:1] in L_codes:
            x = L_codes.index(codes[i:i+7:1])
            digits += str(x) 
        elif codes[i:i+7:1] in G_codes:
            x = G_codes.index(codes[i:i+7:1])
            digits += str(x)
        elif codes[i:i+7:1] in R_codes:
            x = R_codes.index(codes[i:i+7:1])
            digits += str(x)
        else:
            digits = ''
            return digits
    return digits

def patterns_of(codes):
    patterns = ''
    for i in range(0,len(codes),7):
        if codes[i:i+7:1] in L_codes:
            patterns += 'L' 
        elif codes[i:i+7:1] in G_codes:
            patterns += 'G'
        elif codes[i:i+7:1] in R_codes:
            patterns += 'R'
        else:
            patterns = ''
            return patterns
    return patterns

def check_digit(digits):
    di1 = []
    di2 = 0
    for e in digits:
        di1.append(int(e))
    for i in range(len(di1)):
        if i%2 == 0:
            di2 += di1[i]*1
        else:
            di2 += di1[i]*3
    if di2%10==0:
        ten = di2
    else:
        ten = ((di2//10)+1)*10
    check_di = str(ten-di2) 
    return check_di

def encode_EAN13(digits):
    if len(digits) != 13:
        return ''
    for e in digits:
        if e not in ['0','1','2','3','4','5','6','7','8','9']:
            return ''
    if check_digit(digits[0:12:]) != digits[12]:
        return ''    
    patterns = pat[int(digits[0])]
    codes = '101'+codes_of(digits[1:7:],patterns)+'01010'+codes_of(digits[7:13:],'RRRRRR')+'101'
    return codes

def decode_EAN13(codes):
    if len(codes) != 95:
        return ''
    for e in codes:
        if e not in ['0','1']:
            return ''
    if codes[0:3:] != '101':
        return ''
    if codes[45:50:] != '01010':
        return ''
    if codes[92:95:] != '101':
        return ''
    if patterns_of(codes[50:92:]) == 'RRRRRR':
        if patterns_of(codes[3:45:]) in pat:
            a = patterns_of(codes[3:45:])
            c = str(pat.index(a)) + digits_of(codes[3:45:]) + digits_of(codes[50:92:])
        else: return ''
    elif patterns_of(codes[44:2:-1]) == 'RRRRRR':
        editcodes = codes[::-1]
        if patterns_of(editcodes[3:45:]) in pat:
            a = patterns_of(editcodes[3:45:])
            c = str(pat.index(a)) + digits_of(editcodes[3:45:]) + digits_of(editcodes[50:92:])
        else: return ''
    else: return ''
    if check_digit(c[0:12:]) != c[12]:
        return ''
    return c

#-------------------------------------------------
test1()