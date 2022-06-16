import random

m = int(input("Enter m: "))
n = int(input("Enter n: "))

def print_chocolate():
    global m, n
    for i in range(n):
        print("#" * m)

def break_chocolate(btype, bpos):
    global m, n
    if btype == "h":
        n = bpos
    if btype == "v":
        m = bpos

def is_gameover():
    global m, n
    if m == 1 and n == 1:
        return True
    return False

def cpu_break():
    global m, n
    #winning position
    if m > n:
        break_chocolate("v", n)
    elif n > m:
        break_chocolate("h", m)

    #if losing position do random move
    elif m == n:
        r = random.randrange(1, m)
        if (random.randrange(0, 2)):
            break_chocolate("h", r)
        else:
            break_chocolate("v", r)
            
print_chocolate() 
while (True):
    btype = input("Horizontal (h) or vertical (v) break: ")
    bpos = int(input("Break row/column: "))

    break_chocolate(btype, bpos)
    print_chocolate()

    if (is_gameover()):
        print("Gameover, you win.")
        break
    
    print("CPU play:")
    cpu_break()
    print_chocolate()
    
    if (is_gameover()):
        print("Gameover, you lose.")
        break
