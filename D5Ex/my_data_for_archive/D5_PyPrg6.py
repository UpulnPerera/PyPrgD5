import time
import threading

def short_task_threaded():
    print("Long task: Starting ... (This will take 3 seconds.)")
    time.sleep(3) # Simulate a 3 second delay
    print("Long task: Finished!")

def long_task_threaded():
    print("Short task: Running quickly.")
    time.sleep(0.5) # Simulate a small delay
    print("Short task: Finished!")

print("--- Program WITH Threads ---")

# 1. Create a new tread to run our long task
background_thread = threading.Thread(target=long_task_threaded)

# 2. Start the new tread. It begins running CONCURRENTLY! 
background_thread.start()

# 3. Meanwhile, the main program contrinues running other things
short_task_threaded()
short_task_threaded() # Run it agin to show it's not blocked

# 4. Wait for the background thread to finidsh before the main program
background_thread.join()



print("--- Program WITH Threads Done ---")