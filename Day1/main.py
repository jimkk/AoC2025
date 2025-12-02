
class Lock:
    currentLoc = 50
    zeroCount = 0
    zeroClicks = 0

    def rotate(self, direction, number):
        if direction == 'L':
            number = -number

        # This works but feels wrong
        if number < 0:
            self.zeroClicks += abs((self.currentLoc + number - 1) // 100) - (1 if self.currentLoc == 0 and self.currentLoc + number < 0 else 0)
        else:
            self.zeroClicks += (self.currentLoc + number) // 100

        self.currentLoc = (self.currentLoc + number) % 100
        if self.currentLoc == 0:
            self.zeroCount += 1



if __name__ == "__main__":
    lock = Lock()
    with open('input.txt', 'r') as file:
        instructions = [(x[0],int(x[1:])) for x in file.readlines()]
    
    for direction, number in instructions:
        lock.rotate(direction, number)
        print(f"After rotating {direction} by {number}, current location is: {lock.currentLoc}", end='')
        print(f"  (Zero clicks after rotation: {lock.zeroClicks})")
    
    print(f"Final location: {lock.currentLoc}")
    print(f"Number of times landed on zero: {lock.zeroCount}")
    print(f"Total zero clicks counted: {lock.zeroClicks}")
