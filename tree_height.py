# python3
# Jiaxin Dai

import sys
import threading
#bibliotēka

def compute_height(n, parents):
    children = [[] for _ in range(n)] # izveido jauna listu
    for child, parent in enumerate(parents): 
        if parent != -1:
        #ja parent nav -1, 
            children[parent].append(child)
            #tad paņem child uz listu "children"
 
    
    def get_height(p):
        if not children[p]:
        #ja pašlaik punktā vēl nav children, tad augstuma ir 1
            return 1
        

        else:
            return 1 + max(get_height(child) for child in children[p])
            # ja punktā ir children, tad  rekursīvi aprēķina katra child augstumu, un tad +1
    

    s = parents.index(-1) # meklēt saknes punkti, kuri vēl nav parent
    return get_height(s)  # call the function
    


def main():
   # implement input form keyboard and from file
    user = input("'I' for input, 'F' for file: ")
    
    # ja user izvēlas manuāla ievadīt datus
    if "I" in user:
        n = int(input()) #ņemsim punktus sk. un parent katra punktā no user
        parents = list(map(int, input().split()))
    
    #ja user izvēlas ievadīt datus no fialā
    elif "F" in user:
    # noteikt failu ceļu un nosaukmus uz mapē
        path = './test/' 
        fileName = input("File name: ")
        folder = path + fileName
    # let user input file name to use, don't allow file names with letter a
        if 'a' in fileName:
            print("File can not contain letter 'a' ")
            return
        
       # meģināt atvert filu un nolasīt punktus un parents sk.  
        try:
            with open(folder, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
                
                
      # noradīt ja failu neatrada vai nepareiz ievada         
        except FileNotFoundError:
            print("File not Found")
            return
        except ValueError:
            print("Wrong input")
            return
        
        
        
     # call the function and output it's result   
    else:
        print("Type 'I' or 'F': ")
        return 
    print(compute_height(n, parents)) #izvade

 
   
    
    
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

