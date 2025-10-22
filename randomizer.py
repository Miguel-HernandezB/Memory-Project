import sys
import random

##Asignning names to command line arguments
NUMBER_OF_PAGES = int(sys.argv[1])                     ##int() formats the arguments from type string to type int
SAMPLE_SIZE = int(sys.argv[2])

##List of instructions 
INSTRUCTIONS = ["R", "W"]

##Naming the soon to be created file
file_name = "input.txt"

##Function that construct the format of the instructions within the .txt file
def construct_inst():
    system_call = random.choice(INSTRUCTIONS)                           ##choice returns a random element from the given list
    mem_address = random.randrange(0, int(NUMBER_OF_PAGES))                 ##randint returns 

    instruction_format = f"{system_call}:{mem_address} \n"              ##Creatring the wanted format in a string

    return instruction_format               

##Creating a file named input.txt and appending the random strings created by construct_inst()
with open(file_name, 'a') as file:                                      ##By using "with" I dont need to worry to close an open file                                  
    for i in range(SAMPLE_SIZE):    
        instruction = construct_inst()
        file.write(instruction)

