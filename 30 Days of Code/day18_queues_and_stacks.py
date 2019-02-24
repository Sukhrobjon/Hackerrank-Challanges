class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop(-1)

    def dequeueCharacter(self):
        return self.queue.pop(0)
