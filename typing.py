'''typing practice'''
import random
import curses

def practice(k, r, m):
    try:
        win = curses.initscr()
        win.addstr("   {}\nround {}.       {} : ".format(m, r, k))
        result = win.getkey()
    except:
        raise
    finally:
        curses.endwin()

    if result == k:
        return True
    return False

# selects a new key from the pool
def new_key(l):
    return l[random.randrange(len(l))]

rounds_default = 10
keys = list(str(input("which keys to practice? : ")))
rounds = input("how many rounds? (default = {}):".format(rounds_default))
if not rounds:
    rounds = rounds_default
else:
    rounds = int(rounds)

message = "let's practice {} for {} rounds".format(keys, rounds)
current = new_key(keys)
incorrect = 0

while rounds > 0:
    if practice(current, rounds, message):
        current = new_key(keys)
        rounds -= 1
        message = 'correct!'
    else:
        message = 'incorrect!'
        incorrect += 1

s = ''
if incorrect != 1:
    s = 's'
print("you made {} mistake{}".format(incorrect, s))
