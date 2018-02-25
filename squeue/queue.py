class SQueue:
    def __init__(self):
        self.players = []

    def enqueue(self, item):
        self.players.append(item)

    def dequeue(self, index):
        try:
            item = self.players.pop(index)
            return item
        except IndexError as e:
            return e

    def remove(self, index):
        self.players.pop(index)

    def reconstitute(self, players):
        for player in players:
            self.players.append(player)
