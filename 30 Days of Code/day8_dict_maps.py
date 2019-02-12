import time


def find_key(dictionary):
    '''
        Returns key and value if key is exist in dictionary else 
        not found. 
    '''
    while True: # takes as much as input until there is no input 
        try:
            name = input()
            if name in dictionary:
                print("{}={}".format(name, dictionary[name]))
            else:
                print("Not found")
        except:
            break
    
    
        

  
  
if __name__ == "__main__":
    start_time = time.time()


    dict_lenght = int(input())
    phone_book = dict(input().split() for _ in range(dict_lenght))
    find_key(phone_book)
    
    print(f"----{time.time() - start_time} seconds-----")


    
