#PTE = | 1-bit dirty | 6-bit translation
import sys
import random

def main():	
	#define global variables used for statistics tracking
	global freePages
	global currMainPage
	global totPageFault
	global totDiskRef
	global totDirtyPage

	freePages = 32
	currMainPage = 0
	totPageFault = 0
	totDiskRef = 0
	totDirtyPage = 0
	
	
	#open/read file
	file = open(sys.argv[1], 'r')
	text_input = file.readlines()
	file.close
	
	#input file formate, 3 parameters ['process num','virtual address','R/W']
	#read in the data file into a list
	processes = []
	processes = [(line.strip()).split() for line in text_input]
	
	
	#get length of parameter list to use for interation line by line
	dataLen = len(processes)

	
	#initialize the page tables and main memory for simulation
	p1PT = [32] * 128
	p2PT = [32] * 128
	p3PT = [32] * 128
	p4PT = [32] * 128
	mainMem = [0] * 32

	for i in range(dataLen):
		temp = processes[i]
		processNum = int(temp[0])
		virtualAdd = int(temp[1])
		readWrite = temp[2]
		PTE = virtualAdd >> 9

		if(processNum == 1):
			#get lower 6 bits for main mem translation
			translation = p1PT[PTE] & 63
					
			#check if PTE translation is invalid
			if(translation > 31):
				totPageFault += 1
				totDiskRef += 1
				
				if(freePages > 0):
					#set valid translation
					p1PT[PTE] = p1PT[PTE] | (currMainPage & 31)
					p1PT[PTE] = p1PT[PTE] ^ (1 << 5)
					
					#store the current process and page pointing to main mem
					mainMem[currMainPage] = (1 << 7) | PTE
					
					currMainPage += 1
					freePages -= 1
				
				else:	
					currMainPage = random.randint(0,31)
					
					#get the previous process and PTE pointing to this mem
					prevProcess = mainMem[currMainPage] >> 7
					prevPTE = mainMem[currMainPage] & 127

					#set previous PT translation to invalid
					if(prevProcess == 1):
						p1PT[prevPTE] = 32
					elif(prevProcess == 2):
						p2PT[prevPTE] = 32
					elif(prevProcess == 3):
						p3PT[prevPTE] = 32
					else:
						p4PT[prevPTE] = 32
					
					p1PT[PTE] = p1PT[PTE] | (currMainPage & 31)
					p1PT[PTE] = p1PT[PTE] ^ (1 << 5)
					
					#store the current process and page pointing to main mem
					mainMem[currMainPage] = (1 << 7) | PTE
					
					#replaced page adds to page faults
					totPageFault += 1
					
				if(readWrite == 'W'):
					#check if page is dirty
					if((p1PT[PTE] >> 6) == 1):
						totDiskRef += 1
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p1PT[PTE] = p1PT[PTE] | (1 << 6)
			
			#if translation was valid
			else:
				if(readWrite == 'W'):
					#check if page is dirty
					if((p1PT[PTE] >> 6) == 1):
						totDiskRef += 2
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p1PT[PTE] = p1PT[PTE] | (1 << 6)

		
		if(processNum == 2):
			#get lower 5 bits for main mem translation
			translation = p2PT[PTE] & 63
					
			#check if PTE translation is invalid
			if(translation > 31):
				totPageFault += 1
				totDiskRef += 1
				
				if(freePages > 0):
					#set valid translation
					p2PT[PTE] = p2PT[PTE] | (currMainPage & 31)
					p2PT[PTE] = p2PT[PTE] ^ (1 << 5)
					
					#store the current pr0cess and page pointing to main mem
					mainMem[currMainPage] = (2 << 7) | PTE
					
					currMainPage += 1
					freePages -= 1
				
				else:
					currMainPage = random.randint(0,31)
					
					#get the previous process and PTE pointing to this mem
					prevProcess = mainMem[currMainPage] >> 7
					prevPTE = mainMem[currMainPage] & 127

					#set previous PT translation to invalid
					if(prevProcess == 1):
						p1PT[prevPTE] = 32
					elif(prevProcess == 2):
						p2PT[prevPTE] = 32
					elif(prevProcess == 3):
						p3PT[prevPTE] = 32
					else:
						p4PT[prevPTE] = 32
					
					p2PT[PTE] = p2PT[PTE] | (currMainPage & 31)
					p2PT[PTE] = p2PT[PTE] ^ (1 << 5)
					
					#store the current process and page pointing to main mem
					mainMem[currMainPage] = (2 << 7) | PTE
					
					#replaced page adds to page faults
					totPageFault += 1
					
				if(readWrite == 'W'):
					#check if page is dirty
					if((p2PT[PTE] >> 6) == 1):
						totDiskRef += 1
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p2PT[PTE] = p2PT[PTE] | (1 << 6)
			
			#if translation was valid
			else:
				if(readWrite == 'W'):
					#check if page is dirty
					if((p2PT[PTE] >> 6) == 1):
						totDiskRef += 2
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p2PT[PTE] = p2PT[PTE] | (1 << 6)

		if(processNum == 3):
			#get lower 5 bits for main mem translation
			translation = p3PT[PTE] & 63
					
			#check if PTE translation is invalid
			if(translation > 31):
				totPageFault += 1
				totDiskRef += 1
				
				if(freePages > 0):
					#set valid translation
					p3PT[PTE] = p3PT[PTE] | (currMainPage & 31)
					p3PT[PTE] = p3PT[PTE] ^ (1 << 5)
					
					#store the current pr0cess and page pointing to main mem
					mainMem[currMainPage] = (3 << 7) | PTE
					
					currMainPage += 1
					freePages -= 1
				
				else:
					currMainPage = random.randint(0,31)
					
					#get the previous process and PTE pointing to this mem
					prevProcess = mainMem[currMainPage] >> 7
					prevPTE = mainMem[currMainPage] & 127

					#set previous PT translation to invalid
					if(prevProcess == 1):
						p1PT[prevPTE] = 32
					elif(prevProcess == 2):
						p2PT[prevPTE] = 32
					elif(prevProcess == 3):
						p3PT[prevPTE] = 32
					else:
						p4PT[prevPTE] = 32
					
					p3PT[PTE] = p3PT[PTE] | (currMainPage & 31)
					p3PT[PTE] = p3PT[PTE] ^ (1 << 5)
					
					#store the current process and page pointing to main mem
					mainMem[currMainPage] = (3 << 7) | PTE
					
					#replaced page adds to page faults
					totPageFault += 1
					
				if(readWrite == 'W'):
					#check if page is dirty
					if((p3PT[PTE] >> 6) == 1):
						totDiskRef += 1
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p3PT[PTE] = p3PT[PTE] | (1 << 6)
			
			#if translation was valid
			else:
				if(readWrite == 'W'):
					#check if page is dirty
					if((p3PT[PTE] >> 6) == 1):
						totDiskRef += 2
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p3PT[PTE] = p3PT[PTE] | (1 << 6)
				
				
		if(processNum == 4):
			#get lower 5 bits for main mem translation
			translation = p4PT[PTE] & 63
					
			#check if PTE translation is invalid
			if(translation > 31):
				totPageFault += 1
				totDiskRef += 1
				
				if(freePages > 0):
					#set valid translation
					p4PT[PTE] = p4PT[PTE] | (currMainPage & 31)
					p4PT[PTE] = p4PT[PTE] ^ (1 << 5)
					
					#store the current pr0cess and page pointing to main mem
					mainMem[currMainPage] = (4 << 7) | PTE
					
					currMainPage += 1
					freePages -= 1
				
				else:
					currMainPage = random.randint(0,31)
					
					#get the previous process and PTE pointing to this mem
					prevProcess = mainMem[currMainPage] >> 7
					prevPTE = mainMem[currMainPage] & 127

					#set previous PT translation to invalid
					if(prevProcess == 1):
						p1PT[prevPTE] = 32
					elif(prevProcess == 2):
						p2PT[prevPTE] = 32
					elif(prevProcess == 3):
						p3PT[prevPTE] = 32
					else:
						p4PT[prevPTE] = 32
					
					p4PT[PTE] = p4PT[PTE] | (currMainPage & 31)
					p4PT[PTE] = p4PT[PTE] ^ (1 << 5)

					#store the current process and page pointing to main mem
					mainMem[currMainPage] = (4 << 7) | PTE
					
					#replaced page adds to page faults
					totPageFault += 1
					
				if(readWrite == 'W'):
					#check if page is dirty
					if((p4PT[PTE] >> 6) == 1):
						totDiskRef += 1
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p4PT[PTE] = p4PT[PTE] | (1 << 6)
			
			#if translation was valid
			else:
				if(readWrite == 'W'):
					#check if page is dirty
					if((p4PT[PTE] >> 6) == 1):
						totDiskRef += 2
						totDirtyPage += 1
						totPageFault += 1
					else:	
						#set dirty bit to 1
						p4PT[PTE] = p4PT[PTE] | (1 << 6)				
	
							
	print("RANDOM")
	print("Total Page Faults: ", totPageFault)
	print("Total Disk References: ", totDiskRef)
	print("Total Dirty Page Writes: ", totDirtyPage)

	





main()





