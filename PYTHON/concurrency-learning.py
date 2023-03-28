import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # # Example 1
    #submit method schedule the function to be executed and return a future object. 
    # The second argument 1 is the param to the function
    f1 = executor.submit(do_something, 1)    
    # result method will be executed when the function completed and return the result
    print(f1.result())

    # # Example 2 of creating multiple threads for a function
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]
    #asCompleted method will return an iterator that we can loop over to get the future objects of the completed thread
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # # Example 3. Using map to create mutiple threads
    secs = [5,4,3,2,1]
    # map will run the functions with every values in the secs list
    # return results instead of the future objects
    results = executor.map(do_something, secs)
    # result will be returned in the order of the list secs. 
    # Even though some of the thread might be finished earlier, it will still wait for the first to finish before printing the next one
    for result in results:
        print(result)



# threads = []
# for _ in range(10):
#     #creating thread, second argument is only needed if your function needs argument
#     #arguments will be in a list, just fill in all your arguments in order
#     t = threading.Thread(target=do_something, args=[1.5])
#     #starting thread
#     t.start()
#     threads.append(t)

# for thread in threads:
#     #thread.join joins the thread with the main thread. Basically similar to await
#     thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')