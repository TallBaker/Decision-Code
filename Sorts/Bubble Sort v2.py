# Bubble sorter v2

# Importing necessary libraries
import random
import time

# The list creator
# random list, number list, edge list, ascending / descending
def list_creator():
    # Creating the random? variable
    rand = input("Create random list? (Y/N): ")

    # Loop to get the correct input for rand
    while rand != "Y" and rand != "N":
        rand = input("Create random list? (Y/N): ")
    
    # If the list is random
    if rand == "Y":
        rang = input("Enter the range (0-?): ")

        # While the range is not an integer
        while not rang.isdigit():
            print("Enter a valid range!")
            rang = input("Enter the range (0-?): ")

        rang = int(rang)

        length = input("Enter the list length: ")

        # While the length is not an integer
        while not length.isdigit():
            print("Enter a valid list length!")
            length = input("Enter the list length: ")
        
        length = int(length)

        # List creator
        un_num = []

        for count in range(0,length):
            un_num.append(random.randint(0,rang))
        
    # If the list is not random
    else:
        edges = input("Input and edge list? (Y/N): ")

        # Loop to get correct input for edge
        while edges != "Y" and edges != "N":
            edges = input("Input and edge list? (Y/N): ")

        # If there is no edge list wanted
        if edges == "N":
            count = 1

            # List inputter
            un_num = []

            num = input(f"Enter #{count}: ")

            # While the number is not empty
            while num != "":
                # If the number is a number
                if num.isnumeric():
                    un_num.append(num)
                    count += 1
                else:
                    print("Enter a valid number")
        
        # If an edge list is wanted
        else:   
            


list_creator()