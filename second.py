##Second Chance algorithm using FIFO 

import sys
import os

## Naming the arguments from the command line 
MEM_SIZE = int(sys.argv[1])                     ## Number of physical memory pages
INPUT_FILE = sys.argv[2]                        ## access sequence file


PAGE_FAULT = 0                                  ##Initializing global page fault counter varibale
PAGE_HIT = 0                                    ##Initialiazing global page hit counter variable 


########################################################################################################

##Class that will initializa a page in physical memory. Need as input the operation and the page memory address.
##The reference bit will always be initialized with zero. 
class Page:

    def __init__(self, op, address):                        ##Class page initializes with with 3 variables and two of them are taken as arguments
        self.operation = op
        self.page_address = address
        self.reference_bit = 0                              ##All pages will initialize with reference bit set at 0

    def set_reference_bit_to_one(self):                     ##Setter that evaluates the reference bit and if zero sets it to 1
        if self.reference_bit == 0:
            self.reference_bit = 1
    
    def set_reference_bit_to_zero(self):                    ##Setter that evaluates the references bit, if 1 it sets it to 0
        if self.reference_bit == 1:
            self.reference_bit = 0

    def get_reference_bit(self):                            ##Getter that returns the value of the reference pit
        return self.reference_bit 

class FixedList:

    def __init__(self, max_length):
        self.fixedlist = []
        self.max_size = max_length
    
    def set_element(self, element, position = None):

        if position == None:                                    ##Checking if position has a value if not it will default to the last index of the list 
            position = self.max_size - 1

        if 0 <= position < self.max_size:                       ##Checking if the proposed index position is within the max size set for it. 
            self.fixedlist.insert(position, element)            ##set_element will act as an append() as long as no value is set on position argument otherwise it will act as insert()
        else:
            raise IndexError("index overflow")                  ##If by chance the intended position >= max_size then this error is raised 

    def pop_element(self, position):                            ##Takes out an element from list at the selected position
        self.fixedlist.pop(position)
    
    def get_list_length(self):                                  ##Returns the length of the current list
        return(len(self.fixedlist))

        

########################################################################################################  

##This function reads a file, determines if it has one or multiple lines writen and based on that result takes a different action to copy its contents into a list.
##It returns a list
def file_to_list():

    access_sequence_list =[]                                    ##Initializing the list were file contents will be copy to

    with open(INPUT_FILE) as file:                              ##With handles the safe closing of the file
        line1 = file.readline()                                 ##Testing how many writen lines does the file have
        line2 = file.readline()                                 ##If this line is empty then file is wrtiten in one line
    
        if not line2:
            access_sequence_list = line1.split()                ##If line2 is empty then we separete the contents of the input file with split() that detects any whitespace 
            return access_sequence_list
        else:
            file.seek(0)                                        ##If line2 has contents then reset the file pointer to the begining
            for i in file:                                      ##Iterate through each line and copy contents into list
                access_sequence_list[i] = file
            return access_sequence_list





def instruction_spliter(inst):
    split = inst.split(":")
    operation = split[0]
    page_address = split[1]
    return operation, page_address


def search_page_in_memory(PHYSICAL_MEMORY, page_address):
    
    if not PHYSICAL_MEMORY:
        page_fault_counter()
        return False

    else:
        for i in PHYSICAL_MEMORY:
            if page_address == PHYSICAL_MEMORY[i].page_address:
                page_hit_counter()
                return True
            else:
                page_fault_counter()
                return False
            


def set_page_in_memory(PHYSICAL_MEMORY, page):
    for position in PHYSICAL_MEMORY:
        if PHYSICAL_MEMORY[position].reference_bit == 0:
            PHYSICAL_MEMORY.pop(position)
            PHYSICAL_MEMORY.append(page)
            break


def second_chance(PHYSICAL_MEMORY,access_sequence_list):
    while(len(PHYSICAL_MEMORY) < MEM_SIZE):
        pass



    return PAGE_FAULT, PAGE_HIT

def page_fault_counter():
    PAGE_FAULT = PAGE_FAULT + 1 

def page_hit_counter():
    PAGE_HIT = PAGE_HIT + 1 

def main():

    INPUT = file_to_list()

    second_chance(INPUT)

    print(f"Total page faults: {PAGE_FAULT}")
    print(f"Total page hits: {PAGE_HIT}")



########################################################################################################



if __name__ == "__main__":
    main()