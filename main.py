import time


scoope = int(input('Enter an int number : '))
start = time.time()
max_n = scoope ** 2
def spacefill(max:int , number:int):
    max_length = len(str(max))
    n_lenght = len(str(number))
    m = (max_length - n_lenght + 1) * " "
    return f'{number}{m}'
    


    
def JadvalZarb(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(spacefill(max_n,i * j) , end = '')
        print()
JadvalZarb(scoope)
end = time.time()
print('Time elapsed : ', end - start)
input("press any key to finish program ...")
