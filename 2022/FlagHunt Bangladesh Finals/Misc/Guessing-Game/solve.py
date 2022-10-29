filename = "string_list.txt"

stringlist = []
with open(filename, 'r') as file:
    for line in file:
        stringlist.append(line.rstrip())

stringlist.sort()

charlist = ['t', 'o', 's', 'o']
poslist = [11, 10, 5, 10]
potentialflag = []


def guesser():
    for stringno in range(len(stringlist)):
        for charnum in range(len(charlist)):

            if charlist[charnum] == stringlist[stringno][poslist[charnum]]:
                potentialflag.append(int(stringno))

    print(potentialflag)
    # print(potentialflag)
    pot = max(potentialflag, key=potentialflag.count)
    print(pot)
    return stringlist[pot]



from pwn import *  # pip install pwntools
import json

r = remote('103.191.240.57', 9000, level = 'debug')

def json_recv():
    return r.recvline()

def json_send(hsh):
    r.sendline(hsh)

for i in range(50):
    received = json_recv()
    received = json_recv()

    charlist = []
    poslist = []
    potentialflag = []

    for i in range(4):
        received = json_recv()
        s = chr(received[0])
        num = int(received[4:6])
        charlist.append(s)
        poslist.append(num)

    print(poslist)
    pt = guesser()

    print("Decoded value: " + pt)

    to_send = str(pt)
    json_send(to_send)

print("Flag is: ")
json_recv()
