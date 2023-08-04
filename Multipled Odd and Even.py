#write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
#The first output file will be named double.txt containing the square of all even integers found in intergers.txt 
#and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt

def Multiply():
#open the three text files
    with open("integers.txt", "r") as integers_numbers, open("double.txt", "a") as even_integers, open("triple.txt", "a") as odd_integers:

#read the numbers.txt that contains 20integers in each line    
#if the numbers are even
#square the numbers
#write it in the double.txt
#if the numbers are odd
#cubed the numbers
#write it in the triple.txt
Multiply()