#What does the Global Interpreter Lock (GIL) do?
#Restricts execution to one thread at a time
import threading

# Both threads run, but NOT truly in parallel
# GIL forces them to take turns
def task():
    for _ in range(1_000_000):
        pass

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start(); t2.start()

# Without GIL, two threads could corrupt this simultaneously
import sys
a = [1, 2, 3]
sys.getrefcount(a)  # GIL keeps this count safe