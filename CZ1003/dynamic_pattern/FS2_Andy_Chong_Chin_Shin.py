#import the time function so time.sleep can be use to "hold" the while loop before it print out the next pattern.
import time


#the user is asked to input the pattern size
#assumption: user input is always integers
n = int (input("input pattern size: "))


#If user entered a value less than 3,
#ask the user to enter a value which is greater than 3 until a value greater than 3 is entered
while n<3:
    print("warning: pattern size should be at least 3!")
    n = int (input("input pattern size: "))


#this is the coordinate that tell when a "x" string is needed to be printed out
firstx = 0
lastx  = n - 1


#initialize the coordinate
#this value will be updated though out the whole process
#this is needed so that selection can be made to print either "x" or "."
col  = 0
row  = 0


#number of pattern,i.e. 1st pattern, 2nd pattern.....
number = 0


#for this code, it is an infinte loops of selection.
#i.e, make a selection in the first loop, make a selection in the second loop and so on.
#so, the while loop need to be always true.
#there are lines to track the values of variables before they are updated.
while True:

    #whether there is a need to go to the next row
    #APPENDIX A
    if col == n:
        #print("firstx: ", firstx,"lastx: ",lastx,"column: ",col,"row: ",row,end="")
        col = 0
        row += 1
        firstx += 1
        lastx -=1
        print()
        


    #whether there is a need to go to the next pattern
    #APPENDIX B
    elif row == n:
        #print("firstx: ", firstx,"lastx: ",lastx,"column: ",col,"row: ",row,end="")
        number += 1
        firstx = 0
        lastx = n - 1
        col = 0
        row = 0
        print()
        time.sleep (0.5)


    #choose whether print x or .
    #APPENDIX C
    elif col == (firstx + number) % n or col == (lastx + number) % n:
        print("x",end="")
        #print("firstx: ", firstx,"lastx: ",lastx,"column: ",col,"row: ",row,end="")
        col += 1
    else:
        print(".",end="")
        #print("firstx: ", firstx,"lastx: ",lastx,"column: ",col,"row: ",row,end="")
        col += 1






        

###################      APPENDIX A      #################################################
#if column is equal to n
#it means the coordinate is out of the n*n pattern
#
#e.g:when n=3
#
#       col=0   col=1   col=2   col=3
#row=0   x        .       x     (here, the coordinate is out of the pattern)
#row=1
#row=2
#row=3
#
#now, the coordinate need to be updated
#column value return to the original value, which is col=0
#add one to current row value, so that coordinate will now located at the next row
#Beside that, there are two "x" in every row, except for the odd value of n
#When the coordinate move to the next row, the coordinate of first and second "x" also change.
#these coordinates need to be update
#by add 1 to first "x" coordinate (because it now move to right)
#and subtract 1 to the second "x" coordinate (because it now move to the left.)
#######################################################################################################


###################      APPENDIX B      #################################################
#else if row is equal to n
#e.g:n=3
#       col=0   col=1   col=2   col=3
#row=0   x        .       x     print()
#row=1   .        x       .     print()
#row=2   x        .       x     print()
#row=3  print()
#a pattern is finish. The next pattern should be printed now
#a print() is included so that there is a space between two pattern.
#a one is plused to number of pattern because it need move on the the next type of pattern.
#the "number" variable will be use in the later part, so that we can "shift" the last row to the first row.
#other variables' value is initialize.
#######################################################################################################


###################      APPENDIX C      #################################################
#there are two condition that are used to choose whether to print 'x' or '.'
#the first condition is 'col == (firstx + number) % n '
#the second condition is 'col == (lastx + number) % n '
#the following example will show how to get these formula
#
#let say I have a long strip of paper that has these patterns
#e.g: n=3 and number=0
#
#
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x   
# . x .   . x .   . x .   . x .   . x .   . x .   . x .   . x .   
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x  
#                       (!!!!!!)
#   (let say this is my first pattern that I wan to print out)
#
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x   
# . x .   . x .   . x .   . x .   . x .   . x .   . x .   . x .   
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x  
#                    (!!!!!!!)
#                    (second pattern)
#
#
#
#
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x   
# . x .   . x .   . x .   . x .   . x .   . x .   . x .   . x .   
# x . x   x . x   x . x   x . x   x . x   x . x   x . x   x . x  
#                     !!!(^)!(^)
#       (original first col) (original last col)
#
#when I want to print out the second pattern, when number = 1
#the first col will move to the middle,
#so (firstx + 1)
#and the last col will move to the first.
#If (lastx + 1) is written, the last row is out of the pattern size,
#that is why a '% n' is added because the value of (lastx + 1) cannot execced or equal to the value of n
#col == (lastx + 1) % n
#In here, lastx = n-1, n = 3
#so (lastx + 1) % n = 0
#this implied that, the 'lastx' now go to the first column.
#
#The general condition that need to print a 'x' is
#col == (firstx + number) % n or  \
#col == (lastx + number) % n
#######################################################################################################





