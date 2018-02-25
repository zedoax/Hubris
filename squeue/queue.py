class SQueue:
    def __init__(self):
        self.players = []

    def enqueue(self, item):
        self.players.append(item)

    def dequeue(self):
        try:
            return self.players.pop(0)
        finally:
            return _

    def remove(self, index):
        self.players.pop(index)

    def reconstitute(self, players):
        for player in players:
            self.players.append(player)
