import threading
import time

# Set this global variable to maximum number of threads you want to execute
MAX_THREAD_COUNT = 30

#Sample program which will run in thread. This is place holder. Add your code to this program, to be executed in the thread
def sampleThreadProgram():
    time.sleep(1)

#main program
def main():
    #Sample loop, replace it with your loop to execute threads. Currently it 
    #will execute 1000 times the above placeholder function in multiple 
    #threads, in parallel of MAX_THREAD_COUNT threads

    for x in range(1000):
        print('x is ' + str(x))
        
        #Sleep and wait for 1 second and wait while some of the running threads
        #in MAX_THREAD_COUNT range are completed before raising new threads
        while len(threading.enumerate())>=MAX_THREAD_COUNT:
            print('running threads are' + str(len(threading.enumerate())))
            time.sleep(1)
        
        # Start new thread since now number of threads are less than MAX_THREAD_COUNT
        t1 = threading.Thread(target=sampleThreadProgram, args=())
        t1.start()

main()