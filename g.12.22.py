class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    
    def getScore(self):
        if self.value == 'A':
            return 1
        elif '2'<=self.value<='9':
            return int(self.value)
        elif self.value == '10':
            return 10
        else:
            return 10

    def sum(self, other):
        s = Card.getScore(self)
        o = Card.getScore(other)
        return (s+o)%10
    
    def __lt__(self, rhs):
        lis = ['3', '4','5','6','7','8','9','10','J','Q','K','A','2']
        l = ['club','diamond','heart', 'spade']
        if self.value != rhs.value:
            return lis.index(self.value)<lis.index(rhs.value)
        else:
            return l.index(self.suit)<l.index(rhs.suit)

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])