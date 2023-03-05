# python3
# Jiaxin Dai

import sys
import threading

def compute_height(n, parents):
    # izveido listu 
    children = [[] for _ in range(n)]
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
    s = parents.index(-1) # inicializēt koku sakne
    rinda = [(s,1)]
    height = 0 
    while rinda:
        n, l = rinda.pop(0)
        if l > height:
            height = l
        for child in children[n]:
            rinda.append((child, l+1))

    return height



def main():
    # implement input form keyboard and from files
    user = input("'I' for input, 'F' for file: ")
    if user == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    elif user == "F":
        path = './test/'
        fileName = input("File name: ")
        folder = path + fileName
        if 'a' in fileName:
                print("Please don't put letter a in file name")
                return
    # let user input file name to use, don't allow file names with letter a
        try:
            with open(folder, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found")
            return
        except ValueError:
            print("Wrong input")
    else:
        print("Error, Please write with I or F")
        return

    print(compute_height(n,parents))
    return

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
