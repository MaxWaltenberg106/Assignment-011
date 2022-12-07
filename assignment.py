from datetime import datetime
import socket
import sys
import os
from netmiko import ConnectHandler
from pywebcopy import save_webpage
choice = 0
#intialises the choice variable to 0

while(choice < 1 or choice > 5):
#do, while loop to continue looping until the user quits the program
    print("Select an option\n1 - Show date and time\n2 - Show IP address (local computer)\n3 - Show Remote home directory listing\n4 - Backup remote file\n5 - Save web page\nQ - Quit\n")
    #Displays the menu to the user
    num = input()
    if (num == "q" or num == "Q"):
    #quits the program if the user enters Q
        print("Exiting")
        sys.exit()
    else:
        choice = int(num)
    if(choice == 1):
    #code for first option
        now = datetime.now()
        #gets the date and time and assigns it to now variable
        print("The date and time is: ", now)
        print()
        choice = 0
        #resets choice variable to loop through again
    elif(choice == 2):
    #code for second option
        hostname=socket.gethostname()
        IPaddr=socket.gethostbyname(hostname)
        #gets the IP address of the local computer and prints it
        print("Your computer IP Address is: ", IPaddr)
        print()
        choice = 0
    elif(choice == 3):
    #code for third option
        net_connect = ConnectHandler(
            device_type="linux",
            host="127.0.0.1",
            port="5679",
            username="swagboi95", 
            password="swagboi95", 
            )
        #connecting to the remote machine
        command = "ls"
        #sets the command to list the home directory
        output = net_connect.send_command(command)
        print (output)
        print ()
        choice = 0
    elif(choice == 4):
    #code for fourth option
        net_connect = ConnectHandler(
            device_type="linux",
            host="127.0.0.1",
            port="5679",
            username="swagboi95", 
            password="swagboi95", 
            )
        fileToCopy = input("Enter the full path of the file to be backed up\n")
        #Allows the user to enter the file to be backed up
        command = "cp " + fileToCopy + " " + fileToCopy + ".old"
        #sets the command to copy the selected file and add .old suffix
        output = net_connect.send_command(command)
        print(output)
        print()
        print("The file has been copied")
        choice = 0
    elif(choice == 5):
    #code for the fifth option
        pageToSave = input("Enter the full URL of the webpage you want to back up\n")
        #allows the user to enter the URL of the webpage to be backed up
        save_webpage(
            url = "http://" + pageToSave,
            project_folder="/Users/carlwaltenberg/Desktop/testfiles",
            project_name="backup_page",
            bypass_robots=True,
            debug=True,
            open_in_browser=True,
            delay=None,
            threaded=False,
            )
        #code to back up the webpage
        choice = 0
    else:
    #code for if the user enters an invalid input
        print("Invalid input")
        print("Select an option\n1 - Show date and time\n2 - Show IP address (local computer)\n3 - Show Remote home directory listing\n4 - Backup remote file\n5 - Save web page\nQ - Quit\n")
        num = input()
        if (num == "q" or num == "Q"):
            print("Exiting")
            sys.exit()
        else:
            choice = int(num)
        

            
        
    
