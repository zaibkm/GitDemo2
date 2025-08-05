#This is out reading and writing to only text files
# always close an openedfile

from fileinput import close

#file = open('test.txt')  #give file path in brackets and store this in a object name file
#print(file.read()) #will read all contents of file and print in output
#print(file.read(5)) #this will read first 5 char of the file

print("Just testing this code for git demo1")
print("Just testing this code for git demo2")

#inorder to read one complete line
#print(file.readline()) #will read first line
#print(file.readline()) #will read second line

#in order to read 100s of lines you need to use a while loop
#line = file.readline()
#while line != "":
 #   print(line)
  #  line = file.readline()

#there is a readlines() method which
#1. reads all the lines
#2. stores each line as an entry of a list, returns them as strings of a list
# [abc, banana, cat, dog, elephant, mouse]
#3. use for loops

#for i in file.readlines():
 #   print(i)

#file.close() #close file


#file = open('test.txt')
#print(file.read(6))
#print(file.readline())


#line = file.readline()

#while line != "":
 #   print(line)
  #  line = file.readline()



#for i in file.readlines():
 #   print(i)

<<<<<<< HEAD
#file.close()
=======
#file.close()


#just testing
>>>>>>> 4fba2847ff394fd74a14a723d844fa6eadf43a9e
