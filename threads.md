Name:Mounika Madireddy

Date:04/08/2016

M20227730


1ans) In thread1.py both the threads A&B are accessing a shared  resource and all the instructions are atomic(operation carried out in single step without any chance that another gets controll over it). 

In thread2.py  the run() function increments a Counter instance, increment operation is done in three steps :
                          
                    sharedCounter += 1

i.First the interpreter fetches the current value of the counter.

ii.Calculates the new value.

iii.Rewrites the new value back to variable.

Meanwhile,if one thread gets control after the current thread has fetched the variable,increment it and write back to the current thread the same thing,possibility of missing a change to the value attribute.

2ans)Inorder to order to overcome mis changing a value attribute we need to synchronize threads.In thread3.py we have made a syncronization between threads by using Lock().At any time, a lock can be held by a single thread, or by no thread at all. If a thread attempts to hold a lock that’s already held by some other thread, execution of the first thread is halted until the lock is released.For each shared resource, create a Lock object. When you need to access the resource, call acquire to hold the lock (this will wait for the lock to be released, if necessary), and call release to release it.

3ans)If we do not use join(),in thread2.py then the main thread terminates first before the termination of its child threads (Thread A&Thread B). This join() blocks the calling thread until the thread whose join() method is called terminates, either normally or through an unhandled exception,or until the optional timeout occurs.

4ans)Pressing **Ctrl + c** while a python program is running will cause python to raise a KeyboardInterupt exception.If the except part of the try-except block doesn't specify which exceptions it should catch, it will catch all exceptions including the KeyboardInterupt that you just caused. If you press ctrl+c rapidly then it terminates the execution of a program.

5ans)In thread4.py the bizarre behavior of both the threads is a lock has been called on a shared resource and none among the threads are calling acquire() method to access the resource .so anyone among the threads can use the shared resource.


6ans)In thread4.py the bizarre behavior of both the threads is a lock has been called on a shared resource and none among the threads are calling acquire() method to access the resource .so anyone among the threads can use the shared resource.

          global sharedNumber
        for k in range(10000000):
          
            sharedNumber = 1
            if sharedNumber != 1:
                print ("A: that was weird")
            
        print ("Goodbye from thread A")


6ans)The problem in question5 can be overcomed by using synchronism of two threads to ensure they execute in the order specified,  if we use lock.acquire()method for a specific thread then that particular thread access the resource and uses it,after its usage if we call release() so that any other thread can access the same source if needed.


          global sharedNumber
        for k in range(10000000):
         self.lock.acquire()
          
            sharedNumber = 1
            if sharedNumber != 1:
                print ("A: that was weird")
                 self.lock.release()
            
        print ("Goodbye from thread A")

