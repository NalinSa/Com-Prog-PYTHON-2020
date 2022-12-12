# Prog-06: Jaccard Similarity
# 6330271121 Nalin Baipluthong

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = stopwords.words('english')
STEMMER = PorterStemmer()

def read_tweets():
    f = open('biden.txt', encoding='utf-8')
    tweets = [line.strip() for line in f.readlines()]
    f.close()
    return tweets

def normalize_text( text ):
    words = []
    for w in word_tokenize(text.lower()):
        if w.isalnum() and w not in STOP_WORDS:
            words.append(STEMMER.stem(w))
    return get_unique( words )

def main():
    tweets = read_tweets()
    norm_tweets = []
    for t in tweets:
        norm_tweets.append( normalize_text(t) )

    print_width = 48
    while True:
        query = input('Query words   : ')
        if query == '': break
        n = int(input('No. of results: '))
        norm_query = normalize_text(query)
        top_n = top_n_similarity(norm_tweets, norm_query, n)
        if len(top_n) == 0:
            print('No matches found.')
        else:
            for tid, jc_coef in top_n:
                show_tweet(tid, tweets[tid], jc_coef, print_width)
        print('-' * print_width)

#--------------------------------------------------------
def get_unique( words ):
    unique_words = []
    for e in words:
        if e not in unique_words:
            unique_words.append(e)
    return unique_words
def jaccard(words_1, words_2):
    aa = 0
    cc = list(words_1)
    for e in words_1:
        if e in words_2:
            aa +=1
    for d in words_2:
        if d not in cc:
            cc.append(d)
    jaccard_coef = aa/len(cc)

    return jaccard_coef
def top_n_similarity(norm_tweets, norm_query, n):
    top = []
    for i in range(len(norm_tweets)):
        if jaccard(norm_tweets[i],norm_query)>0 :
            top.append([jaccard(norm_tweets[i],norm_query), -i])
    top.sort()
    x = top[-1:-n-1:-1]
    top_n = []
    for e in x:
        top_n.append([-e[1],e[0]])
    return top_n
def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print()
    print('#'+str(tweet_id)+' ('+str(round(jc_coef,2))+')')
    t = tweet_content.split(' ')
    x = ' '
    for e in t:
        if len(x) + len(e) + 1 <= print_width: 
            x += ' ' + e
        else:
            print(x)
            x = '  '+ e
    print(x)

#--------------------------------------------
main()