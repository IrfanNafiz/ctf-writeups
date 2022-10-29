
# Guessing Game

You're given an ip:port, which gives the character and position of letters in a string.
eg. <br>
s --- 4<br>
t --- 5<br>
u --- 10<br>
t --- 11<br>
<br>
A string_list.txt is also given with multiple lines of string.

Description said that after guessing correctly 50 times the flag will be given.

From this we are to understand that we have to find the string from the .txt file that has these characters in the given positions.

Solving for one such string gives us a new set of 4 characters with positions. So we have to solve these for 50 times.

We have to make a recieve, send also from the port in python. And parse the recieved data such that we can use the char and position information and find the string from the txt file.

Turns out the txt file also has to be sorted in ascending order in order to solve the challenge. (There is absolutely no way to know this as per my knowledge.)

The solve.py is given.

Flag is: CTF_BD{345y_p35y_5cr1p71n6}
