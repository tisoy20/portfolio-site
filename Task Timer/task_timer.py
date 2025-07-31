import time  # this library helps us track elapsed time

# Step 1: Ask the user what they’re working on
task = input("🕒 What task are you starting? ")

print(f"Starting timer for: {task}")
start_time = time.time()  # stores the current time when you started

input("⏹️ Press Enter to stop the timer... ")  # waits for user to stop

end_time = time.time()  # stores the time when you stopped
elapsed_time = end_time - start_time  # calculates total time spent in seconds

# Step 2: Convert to minutes and seconds
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"✅ You worked on '{task}' for {minutes} minutes and {seconds} seconds.")