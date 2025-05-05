## Tasks

### 1.

**Objective:** Use ChatGPT to identify and correct errors in code samples.
```
$ cat factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result \*= n
    return result

f = factorial(int(sys.argv\[1\]))
print(f)

$ ./factorial.py 2
^CTraceback (most recent call last):
  File "/private/tmp/factorial.py", line 9, in <module>
    factorial(int(sys.argv\[1\]))
  File "/private/tmp/factorial.py", line 5, in factorial
    while n > 1:
          ^^^^^
KeyboardInterrupt
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/factorial.py "here").

Fix the code, it should print the factorial of the argument.



### 2.

**Objective:** Use ChatGPT to identify and correct errors in code samples.
```
$ cat print\_arguments.py
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv\[i\])

$ ./print\_arguments.py 1 2 3
print\_arguments.py
1
2
3
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/print_arguments.py "here").

Fix the code, it should print only the arguments without the python file name.



### 3.

**Objective:** Use ChatGPT to identify and correct errors in code samples.
```
$ cat change\_background.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Change Background Color</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
</head>
<body>

<h2>Click the button to change the background color</h2>

<button id="colorButon">Change Color</button>

<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        // Generate a random color
        var randomColor = "#" + Math.floor(Math.random()\*16777215).toString(16);
        // Change the background color of the body
        document.body.style.backgroundColor = randomColor;
    }
</script>

</body>
</html>
```
You can download the code [here](/rltoken/Q2IZY5FB9a-udDliTmvHOQ "here"). [This](/rltoken/EqntmyG56eyYIid9ghEO0g "This") editor can be use to test your code.

Fix the code, it should change the background color when you click on the button.



### 4.

**Objective:** Use ChatGPT to identify and correct errors in code samples.

**Game Overview**: Minesweeper is a puzzle game where the player must clear a field of hidden “mines” without detonating any of them, using clues about the number of neighboring mines in each field.
```
$ cat mines.py
#!/usr/bin/python3
import random
import os

def clear\_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def \_\_init\_\_(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width \* height), mines))
        self.field = \[\[' ' for \_ in range(width)\] for \_ in range(height)\]
        self.revealed = \[\[False for \_ in range(width)\] for \_ in range(height)\]

    def print\_board(self, reveal=False):
        clear\_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed\[y\]\[x\]:
                    if (y \* self.width + x) in self.mines:
                        print('\*', end=' ')
                    else:
                        count = self.count\_mines\_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count\_mines\_nearby(self, x, y):
        count = 0
        for dx in \[-1, 0, 1\]:
            for dy in \[-1, 0, 1\]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny \* self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y \* self.width + x) in self.mines:
            return False
        self.revealed\[y\]\[x\] = True
        if self.count\_mines\_nearby(x, y) == 0:
            for dx in \[-1, 0, 1\]:
                for dy in \[-1, 0, 1\]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed\[ny\]\[nx\]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print\_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print\_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if \_\_name\_\_ == "\_\_main\_\_":
    game = Minesweeper()
    game.play()
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/mines.py "here").

Fix the code, implement a mechanism to detect when all non-mine cells have been revealed, thus winning the game.
```
$ ./mines.py
0 1 2 3 4 5 6 7 8 9
1
2
3
4
5
6
7
8
9
...
...
0 1 2 3 4 5 6 7 8 9
0
1       1 1 1   1 1 1
2 1 1 1 1 . 1   2 . 2
3 2 . 2 1 1 1   2 . 2
4 2 . 3 1       1 1 1
5 1 2 . 1
6 1 2 2 3 2 1
7 . 1 1 . . 1
8 1 1 2 3 3 1
9     1 . 1
Congratulations! You've won the game.
```


### 5.

**Objective:** Use ChatGPT to document the code
```
$ cat factorial\_recursive.py
#!/usr/bin/python3
import sys

def factorial(n):
        if n == 0:
        return 1
    else:
        return n \* factorial(n-1)

f = factorial(int(sys.argv\[1\]))
print(f)

$ ./factorial\_recursive.py 4
24
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/factorial_recursive.py "here").

Add the comments to this code. You should have 3 sections: function description, parameters and returns.



### 6.

**Objective:** Use ChatGPT to document the code
```
$ cat checkbook.py
class Checkbook:
    def \_\_init\_\_(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get\_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get\_balance()
        else:
            print("Invalid command. Please try again.")

if \_\_name\_\_ == "\_\_main\_\_":
    main()
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/checkbook.py "here").

Fix the code, to prevent the program from crashing due to invalid input (e.g., non-numeric values), add error handling mechanisms.
```
$ ./checkbook.py
What would you like to do? (deposit, withdraw, balance, exit): deposit
Enter the amount to deposit: $test
Traceback (most recent call last):
  File "/private/tmp/3156/checkbook.py", line 39, in <module>
    main()
  File "/private/tmp/3156/checkbook.py", line 28, in main
    amount = float(input("Enter the amount to deposit: $"))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'test'
```


### 7.

**Objective:** Use ChatGPT to identify and correct errors in code samples. (There may be several errors on the code)

**Game Overview**: Players alternate placing “X” or “O” on a 3x3 board, aiming to get three in a row horizontally, vertically, or diagonally to win.
```
$ cat tic.py
#!/usr/bin/python3
def print\_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" \* 5)

def check\_winner(board):
    for row in board:
        if row.count(row\[0\]) == len(row) and row\[0\] != " ":
            return True

    for col in range(len(board\[0\])):
        if board\[0\]\[col\] == board\[1\]\[col\] == board\[2\]\[col\] and board\[0\]\[col\] != " ":
            return True

    if board\[0\]\[0\] == board\[1\]\[1\] == board\[2\]\[2\] and board\[0\]\[0\] != " ":
        return True

    if board\[0\]\[2\] == board\[1\]\[1\] == board\[2\]\[0\] and board\[0\]\[2\] != " ":
        return True

    return False

def tic\_tac\_toe():
    board = \[\[" "\]\*3 for \_ in range(3)\]
    player = "X"
    while not check\_winner(board):
        print\_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if board\[row\]\[col\] == " ":
            board\[row\]\[col\] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print\_board(board)
    print("Player " + player + " wins!")

tic\_tac\_toe()
```
You can download the code [here](https://github.com/hs-hq-service/3156/blob/main/tic.py "here").

**Warning:** Test all the user inputs !
