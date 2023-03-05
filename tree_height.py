# python3
# Jiaxin Dai

import sys
import threading

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
    
    def get_height(p):
        if not children[p]:
            return 1
        




        else:
            return 1 + max(get_height(child) for child in children[p])
    

    s = parents.index(-1)
    return get_height(s)
    


def main():
    user = input("'I' for input, 'F' for file: ")
    if user == "I":
        n = int(input())
        parents = list(map(int, input().split()))

    elif user == "F":
        path = './test/'
        fileName = input("File name: ")
        folder = path + fileName
    
        if 'a' in fileName:
            print("File can not contain letter 'a' ")
            return
        
        
        try:
            with open(folder, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
                
                
                
        except FileNotFoundError:
            print("File not found")
            return
        except ValueError:
            print("Invalid input format")
            return
        
        
        
        
    else:
        print("Type 'I' or 'F': ")
        return 
    print(compute_height(n, parents))

    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

