# Embedded_OS_Scheduling

Scripts act on the input data txt files which contain 50000 sets of input parameters.  One main page table and 4 sub page tables (one for each process) are created by the script. The first input parameter dictats which process(1, 2, 3, or 4) the task would run on.  The second parameter contains the page table entry information, the page table and offset is determined by this number.  The final parameter determines if a read or write needs to occur.

# rand.py

Implements the random selection algorithm for choosing which main memory page to replace next.

To run this file in the terminal:

	python3 rand.py data1.txt
	OR
	python3 rand.py data2.txt


# fifo.py

Implements the FIFO algorithm for choosing which main memory page to replace next.


To run this file in the terminal:

	python3 fifo.py data1.txt
	OR
	python3 fifo.py data2.txt
