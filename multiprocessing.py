import time
import multiprocessing
result=[]

def square(numbers):
    global result
    for i in numbers:
        
        result.append(i*i)
    print('result:'+ str(result))
    
if __name__=="main":

    arr=[1,2,3]

    p1=multiprocessing.process(target=square,arg=(arr,))
    p1.start()
    p1.join()
    print("result:",+str(result))
    
    
        
