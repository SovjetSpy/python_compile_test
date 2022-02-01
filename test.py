from numba import jit
import datetime
import platform

@jit
def test_jit():
    primenumcount = 20000
    for i in range(2, primenumcount):
        isprime = True
        for j in range(2, i):
            if (i % j == 0):
                isprime = False
        if (isprime == True):
            print(i, "is prime")

def test():
    primenumcount = 20000
    for i in range(2, primenumcount):
        isprime = True
        for j in range(2, i):
            if (i % j == 0):
                isprime = False
        if (isprime == True):
            print(i, "is prime")

my_system = platform.uname()
f = open("results.txt", "a")
f.write(f"System: {my_system.system}\n")
f.write(f"Node Name: {my_system.node}\n")
f.write(f"Release: {my_system.release}\n")
f.write(f"Version: {my_system.version}\n")
f.write(f"Machine: {my_system.machine}\n")
f.write(f"Processor: {my_system.processor}\n")

test_jit()

for c in range(10):
    t = datetime.datetime.now()
    test_jit()
    t = datetime.datetime.now() - t
    f.write(("python jit (numba) => ronde: {0}, time: {1} microsec\n".format(c + 1,(t.microseconds))))

for c in range(10):
    t = datetime.datetime.now()
    test()
    t = datetime.datetime.now() - t
    f.write(("python => ronde: {0}, time: {1} microsec\n".format(c + 1,(t.microseconds))))

f.close()
