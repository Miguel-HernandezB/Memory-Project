# Memory-Project
Miguel Hernandez Betancourt

801-15-3480

CCOM4017 

## Introduction
This project is about understanding the principles of memory management by simulating 3 page replacement algorithms. Optimal replacement, Second Chance using FIFO and WSClock algorithms. There are 4 files in total: Each algorithm is its own program and a file called randomizer.py that will create a .txt file of random "instructions" of reads and writes with their corresponding page address in memory. 

## Files

### randomizer.py

This program is meant to create .txt files that have a random assortment of read/write instructions. It takes 2 arguments from the command line. First argument is an int that specifies the amount of instructions you want to create and the second argument that specifies the memory size. With this as input the program randomizes instructions and what "memory address is accessing" creating a format `instruction:memory_address`. It then outputs a file named input.txt 

### optimal.py

### second.py

### wsclock.py


## Instructions

### Creating a file from the randomizer.py

```bash
python3 randomizer.py {number_of_instructions} {memory_size}
``` 



## References

### File Handling
- https://www.w3schools.com/python/python_file_handling.asp 

### Using markdown
- https://www.markdownguide.org/getting-started/

### Writing a ReadMe 
- https://www.makeareadme.com

