##Second Chance algorithm using FIFO
##Miguel A. Hernandez Betancourt
##801-15-3480
##CCOM4017 Sistemas Operativos

import sys
import os

## Naming the arguments from the command line 
MEM_SIZE = int(sys.argv[1])                     ## Number of physical memory pages
INPUT_FILE = sys.argv[2]                        ## access sequence file


PAGE_FAULT = 0                                  ##Initializing global page fault counter varibale
PAGE_HIT = 0                                    ##Initialiazing global page hit counter variable 

PAGES = []                                      ##Initializing a list to store objects type Page

########################################################################################################

##Class that will initializa a page. Need as input the operation and the page memory address.
##The reference bit will always be initialized with zero for the second chance algorithm. 
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
        if len(self.fixedlist) >= self.max_size:
            raise IndexError("max capacity reached, release memory")
        
        if position == None:                                    ##Checking if position has a value if not it will default to the last index of the list 
            position = len(self.fixedlist)

        if 0 <= position < self.max_size:                       ##Checking if the proposed index position is within the max size set for it. 
            self.fixedlist.insert(position, element)            ##set_element will act as an append() as long as no value is set on position argument otherwise it will act as insert()
        else:
            raise IndexError("index out of list bound")        ##If by chance the intended position >= max_size then this error is raised 

    def pop_element(self, position):                            ##Takes out an element from list at the selected position
        self.fixedlist.pop(position)
     
    def get_list_length(self):                                  ##Returns the length of the current list
        return(len(self.fixedlist))

        

########################################################################################################  

def page_fault_counter():
    global PAGE_FAULT
    PAGE_FAULT = PAGE_FAULT + 1 

def page_hit_counter():
    global PAGE_HIT
    PAGE_HIT = PAGE_HIT + 1 


##This function reads a file, determines if it has one or multiple lines writen and based on that result takes a different action to copy its contents into a list.
##It returns a list
def file_to_list():

    access_sequence_list =[]                                    ##Initializing the list were file contents will be copy to

    with open(INPUT_FILE) as file:                              ##With handles the safe closing of the file
        line1 = file.readline()                                 ##Testing how many writen lines does the file have
        line2 = file.readline()                                 ##If the second line is empty then file is wrtiten in one line
    
        if not line2:
            access_sequence_list = line1.split()                ##If line2 is empty then we separete the contents of the input file with split() that detects any whitespace 
            return access_sequence_list
        else:
            file.seek(0)                                        ##If line2 has contents then reset the file pointer to the begining
            for line in file:                                   ##Iterate through each line and copy contents into list
                access_sequence_list.append(line.strip())
            return access_sequence_list                         ##Return the finished list



##This function is meant to split the strings stored in INPUT list.
##It returns tuple: operation and page_address 
def string_spliter(input_string):
    split = input_string.split(":")                             ##split(":") methods will divide the string in two when it detects ":" and will return a list of the divided parts
    operation = split[0]                                        ##In position 0 we will find the operation 
    page_address = int(split[1])                                ##In position 1 we will find the page_address. The list input type is a string and int() changes it to type int
    return operation, page_address                              ##Returns tuple 




## Function that will go through PHYSICAL MEMORY in search for a page address. It will call the appropriate functions to update the page faults and page hits variables
## It returns a boolean 
def search_page_in_memory(PHYSICAL_MEMORY, page_address):
    ##thinking in eliminating this if else and just leave the for loop 
    if not PHYSICAL_MEMORY.fixedlist:                                       ##If PHYSICAL MEMORY is empty then no search needed
        page_fault_counter()                                                ##Update page fault
        return False                                                        ##Reurns false since no page was found

    else:
        for i in range(len(PHYSICAL_MEMORY.fixedlist)):                     ##Linear search through the list        
            if page_address == PHYSICAL_MEMORY.fixedlist[i].page_address:             #If there is a page hit
                page_hit_counter()                                          ##Update page hit
                PHYSICAL_MEMORY.fixedlist[i].set_reference_bit_to_one()               ##Set reference bit to 1
                return True                                                 
                                                                       
        page_fault_counter()                                                ## If by the end of the for loop no hits were made we update the page fault     
        return False                                                        ## Return False 
            



##This function searches the first page with a reference bit == 0, pops it and inserts the new page at the end of the memory
def set_page_in_memory(PHYSICAL_MEMORY, page):
    if len(PHYSICAL_MEMORY.fixedlist) < PHYSICAL_MEMORY.max_size:
        PHYSICAL_MEMORY.set_element(page)
        return
                             
    for i in range(len(PHYSICAL_MEMORY.fixedlist)):
        
        if PHYSICAL_MEMORY.fixedlist[i].reference_bit == 0:                              ##First page found with a reference bit with 0
            PHYSICAL_MEMORY.pop_element(i)                                               ##Takes out the page 
            PHYSICAL_MEMORY.set_element(page)                                            ##Puts new page into the end of the list
            return
        else:
            PHYSICAL_MEMORY.fixedlist[i].set_reference_bit_to_zero()              ##Second chance used 


def second_chance(PHYSICAL_MEMORY,access_sequence_list):
    for i in range(len(access_sequence_list)):                                          ##Loop over access sequence list
        operation, page_address = string_spliter(access_sequence_list[i])               ##Separate the strings into workable parts
        PAGES.append(Page(operation, page_address))                                     ##Storing the page in a PAGES list for easy "variable creation"

        if search_page_in_memory(PHYSICAL_MEMORY, page_address):                        ##We search if the page is in PHYSICAL_MEMORY
            continue                                                                    ##If theres a page hit we cut the loop iteration to get to the next one
        
        else:
            set_page_in_memory(PHYSICAL_MEMORY, PAGES[i])                               ##If page not in memory we add it 



    return PAGE_FAULT, PAGE_HIT                                                         ##When loop ends returns tuple of total page fault and page hits 

########################################################################################################

def main():

    PHYSICAL_MEMORY = FixedList(MEM_SIZE)                       ## Creating the emulated physical memory and passing the set size sent through the command line 

    INPUT = file_to_list()                                      ## Creating a access sequence list from the given file 

    total_pf, total_ph = second_chance(PHYSICAL_MEMORY, INPUT)


    print(f"Total page faults: {total_pf}")                   ##Display Page Fault result
    print(f"Total page hits: {total_ph}")                     ##Display Page Hit result
    print(f"Total accceses: {total_ph + total_pf}")           ##Display total hits


########################################################################################################



if __name__ == "__main__":
    main()