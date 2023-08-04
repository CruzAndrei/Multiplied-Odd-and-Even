#write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
#The first output file will be named double.txt containing the square of all even integers found in intergers.txt 
#and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt

def Multiply():
#open the three text files
    with open("integers.txt", "r") as integers_numbers, open("double.txt", "a") as even_integers, open("triple.txt", "a") as odd_integers:
#read the numbers.txt that contains 20integers in each line 
        for line in integers_numbers:
            input_number = int(line)
            #if the numbers are even
            if input_number % 2 == 0:
            #square the numbers
                even_squared = input_number * input_number
            #write it in the double.txt
                even_integers.write(str(even_squared) + "\n")
            #if the numbers are odd
            else:
            #cubed the numbers
                odd_cubed = input_number * input_number * input_number

#write it in the triple.txt
Multiply()