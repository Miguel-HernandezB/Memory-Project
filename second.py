##Second Chance algorithm using FIFO 

import sys
import os

## Naming the arguments from the command line 
MEM_SIZE = int(sys.argv[1])                     ## Number of physical memory pages
INPUT_FILE = sys.argv[2]                        ## access sequence file

########################################################################################################

INPUT = []                                      ##Initializing empty list
with open(INPUT_FILE) as file:
    for i in file:
        INPUT[i] = file

########################################################################################################
class Page:
    def __init__(self, inst, address):
         instruction = inst
         page_address = address
         reference_bit = 0

    def set_reference_bit():
        pass

    def get_reference_bit():
        pass 


########################################################################################################   

def instruction_spliter():
    pass


def search_page_in_memory():
    pass


def set_page_in_memory():
    pass


def second_chance():
    pass 


def main():
    pass


########################################################################################################



if __name__ == "__main__":
    main()