import time
import random

def list_input(): 
    unsorted_number_list = []
    unsorted_edge_list = []
    combined_list = []
    random_ = "Hello World"
    while random_ != "Y" and random_ != "N":
        random_ = input("Create a random list? (Y/N): ")
        if random_ == "Y":
            while True:
                fault = False
                try:
                    range_ = int(input("Enter the range (0-?): "))
                except:
                    print("Enter a valid range!")
                    fault = True
                if not fault:
                    try:
                        num_of_numbers = int(input("Enter the list length: "))
                        break
                    except:
                        print("Enter a valid length!")
    if random_ == "N":
        count = 1
        edges = "Hello World"
        while edges != "Y" and edges != "N":
            edges = input("Enter edges list as well? (Y/N): ")
        if edges == "Y":
            while True:
                edge = input(f"Enter edge #{count}: ")
                if edge == "":
                    break
                elif len(edge) == 2 and edge.isalpha():
                    unsorted_edge_list.append(edge)
                    while True:
                        number = input(f"Enter weight {edge}: ")
                        try:
                            number = float(number)
                            unsorted_number_list.append(number)
                            count += 1
                            break
                        except:
                            print("Enter a valid edge weight!")
                else:
                    print("Enter a valid edge!")
            for count in range(0,len(unsorted_edge_list)):
                combined_list.append(f"{unsorted_edge_list[count]}({unsorted_number_list[count]})")
            print(f"\n\nUnsorted list:\n\n{combined_list}")
        else:
            while True:
                number = input(f"Enter #{count}: ")
                if number == "":
                    break
                try: 
                    number = float(number)
                    unsorted_number_list.append(number)
                    count += 1
                except: 
                    print("Enter a valid number!")
            print(f"\n\nUnsorted list:\n\n{unsorted_number_list}")
    else:
        count = 0
        while count < num_of_numbers:
            number = random.randint(0,range_)
            unsorted_number_list.append(number)
            count += 1
        print(f"\n\nUnsorted list:\n\n{unsorted_number_list}")
    return unsorted_number_list, unsorted_edge_list, combined_list
    
def bubble_sorter(unsorted_number_list, unsorted_edge_list, combined_list):
    length = len(unsorted_number_list) 
    comparisons = 0
    swaps = 1
    pass_num = 1
    sorting_type = "Hello World"
    each_pass = "Hello World"
    while sorting_type != "A" and sorting_type != "D":
        sorting_type = input("\nAscending or descending order? (A/D): ")
    while each_pass != "Y" and each_pass != "N":
        each_pass = input("Show every pass? (Y/N): ")
    if len(unsorted_edge_list) == 0:
        if sorting_type == "A":
            if each_pass == "Y":
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] > unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                swaps += 1
                    length -= 1
                    print(f"\nPass {pass_num}:")
                    print(f"\n{unsorted_number_list}")
                    pass_num += 1

            else:
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] > unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                swaps += 1
                    length -= 1
        else:
            if each_pass == "Y":
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] < unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                swaps += 1
                    length -= 1
                    print(f"\nPass {pass_num}:")
                    print(f"\n{unsorted_number_list}")
                    pass_num += 1
            else:
                while swaps != 0: 
                    start_time = time.time()
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] < unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                swaps += 1
                    length -= 1
    else:
        if sorting_type == "A":
            if each_pass == "Y":
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] > unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                unsorted_edge_list[count], unsorted_edge_list[count + 1] = unsorted_edge_list[count + 1], unsorted_edge_list[count]
                                combined_list[count], combined_list[count + 1] = combined_list[count + 1], combined_list[count]
                                swaps += 1
                    length -= 1
                    print(f"\nPass {pass_num}:")
                    print(f"\n{combined_list}")
                    pass_num += 1
            else:
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] > unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                unsorted_edge_list[count], unsorted_edge_list[count + 1] = unsorted_edge_list[count + 1], unsorted_edge_list[count]
                                swaps += 1
                    length -= 1
        else:
            start_time = time.time()
            if each_pass == "Y":
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] < unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                unsorted_edge_list[count], unsorted_edge_list[count + 1] = unsorted_edge_list[count + 1], unsorted_edge_list[count]
                                combined_list[count], combined_list[count + 1] = combined_list[count + 1], combined_list[count]
                                swaps += 1
                    length -= 1
                    print(f"\nPass {pass_num}:")
                    print(f"\n{combined_list}")
                    pass_num += 1
            else:
                start_time = time.time()
                while swaps != 0: 
                    swaps = 0
                    for count in range(0,length-1):
                        comparisons += 1
                        if unsorted_number_list[count] < unsorted_number_list[count + 1]: 
                                unsorted_number_list[count], unsorted_number_list[count + 1] = unsorted_number_list[count + 1], unsorted_number_list[count] 
                                unsorted_edge_list[count], unsorted_edge_list[count + 1] = unsorted_edge_list[count + 1], unsorted_edge_list[count]
                                swaps += 1
                    length -= 1

    sorted_number_list = unsorted_number_list
    sorted_edge_list = unsorted_edge_list
    execution_time = time.time() - start_time
    return sorted_number_list, sorted_edge_list, combined_list, execution_time, comparisons



unsorted_number_list, unsorted_edge_list, combined_list = list_input()
sorted_number_list, sorted_edge_list, combined_list, execution_time, comparisons = bubble_sorter(unsorted_number_list, unsorted_edge_list, combined_list)
if len(sorted_edge_list) != 0:
    print(f"\n\nSorted list:\n\n{combined_list}")
else:
    print(f"\n\nSorted list:\n\n{sorted_number_list}")
print(f"\nComparisons: {comparisons}")
print(f"Time: {execution_time} s\n")