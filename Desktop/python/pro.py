import commands
import os
import string

program = raw_input("Enter process: ")

try:
    
    output = commands.getoutput("ps -f|grep " + program)
    proginfo = string.split(output)

    print "\n\
    Full path:\t\t", proginfo[5], "\n\
    Owner:\t\t", proginfo[0], "\n\
    Process ID:\t\t", proginfo[1], "\n\
    Parent process ID:\t", proginfo[2], "\n\
    Time started:\t", proginfo[4] 

    print "Complete! \n" 

except:
    print "Failed"
