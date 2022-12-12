class Card:
 def __init__(self, value, suit):
    self.value = value
    self.suit = suit
 def __str__(self):
    return '(' + self.value +' '+ str(self.suit)+')'
     
 def next1(self):
    l1 = ['3', '4','5','6','7','8','9','10','J','Q','K','A','2','3']
    l2 = ['club','diamond','heart', 'spade']
    if self.suit == 'spade':
         j = l1.index(self.value)
         return Card(l1[j+1],'club')
    else:
        j = l2.index(self.suit)
        return Card(self.value,l2[j+1])
     
 def next2(self):
    l1 = ['3', '4','5','6','7','8','9','10','J','Q','K','A','2','3']
    l2 = ['club','diamond','heart', 'spade']
    if self.suit == 'spade':
         j = l1.index(self.value)
         self.value = l1[j+1]
         self.suit = 'club'
    else:
        j = l2.index(self.suit)
        self.suit = l2[j+1]
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])