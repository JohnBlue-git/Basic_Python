# Auther: John Blue
# Time: 2023/2
# Object: display how to use thread, mutex, and conditional variable

#
# library
#
import threading
#import time
#time.sleep(0.001)

#
# mutex
#
# create a lock
#lock = threading.Lock()
# acquire the lock
#lock.acquire()
# release the lock
#lock.release()

#
# conditional variable
#
cond = threading.Condition()


it = 0;
def count_in_order(id):
    global it
    
    #
    # critical section
    #
    # conditional wait
    cond.acquire()
    while id != it: cond.wait()
    
    print("thread id: ", id, ", i = ", it);
    it += 1;
    
    # conditional signal
    cond.notify_all();#cond.notify_one();
    
    cond.release()
    #
    # critical section end
    #


if __name__ == "__main__":
    ths = []
    for i in range(9):
        th = threading.Thread(target = count_in_order, args = (i,))
        th.start()
        ths.append(th)
    
    for th in ths:
        th.join()


# .start() VS .run()
# when call start() method a new Thread is created
# when call run() method directly no new Thread is created and code inside run() will execute on current Thread
#https://javarevisited.blogspot.com/2012/03/difference-between-start-and-run-method.html#ixzz7sbjD03pb
