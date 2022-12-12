dic = {'2':'a', '22':'b', '222':'c', '3':'d', '33':'e', '333':'f', '4':'g', '44':'h', '444':'i','5':'j', \
       '55':'k', '555':'l','6':'m', '66':'n', '666':'o', '7':'p', '77':'q', '777':'r','7777':'s', \
       '8':'t', '88':'u', '888':'v', '9':'w', '99':'x', '999':'y', '9999':'z', '0':' '}
dix = {}
for key in dic:
    j = dic[key]
    dix[j] = key
    dix[key] = j
def text2keys(text):
    tex = text.lower()
    te = []
    for e in tex:
        if e in dix:
            te.append(dix[e])
    return ' '.join(te)
def keys2text(keys):
    ke = keys.split()
    t = ''
    for e in ke:
        if e in dix:
            t += dix[e]
    return t
print(text2keys("I am busy."))
print(keys2text("444 0 2 6 0 22 88 7777 999")) 
