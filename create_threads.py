import threading

#Creating threads
def create_threads(list, function):


    threads = []

    for ip in list:
        th = threading.Thread(target = function, args = (ip,))   #args is a tuple with a single element
        th.start()
        threads.append(th)
       # we will use the join method in order to instruct the program to wait for all threads to finish. 
       #this way, our application will be able to read from and configure multiple network devices simultaneously.
    for th in threads:
        th.join()