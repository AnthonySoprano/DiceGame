class Player:
    def __init__(self, name, next):
        self.name = name            # player name
        self.points = 0             # current points
        self.prev_rolls = [0,0]     # previous two rolls are stored to detect consecutive '1'
        self.skip_flag = False      # flag to skip round if consecutive ones were rolled
        self.next = next            # points to next player in play order

# circular linked list to store current order of play
class PlayerOrder:
    def __init__(self):
        self.head = None

    # add at last position
    def addPlayer(self, name):
        if self.head is None:
            player = Player(name, None)
            self.head = player
            player.next = self.head
        else:
            player = Player(name, self.head)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = player
    
    def removePlayer(self, name):
        if name == self.head.name:
            if self.head.next == self.head:
                self.head = None
                return
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next.name != name:
                cur = cur.next
            cur.next = cur.next.next

    def getNextPlayer(self, player):
        return player.next

    # Prints active players and scores by Rank
    def printOrder(self, startRank=1):
        if self.head is None:
            print("empty list")
            return
        cur = self.head
        lis = []
        while cur.next != self.head:
            lis.append([cur.name, cur.points])
            cur = cur.next
        lis.append([cur.name, cur.points])
        ranks = sorted(lis, key = lambda x: x[1], reverse=True)
        for i in range(len(ranks)):
            print(startRank+i, ranks[i][0], ranks[i][1])