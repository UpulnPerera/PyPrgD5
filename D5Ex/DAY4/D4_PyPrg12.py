import datetime

# Get the current date and time
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Get only the current date
today = datetime.date.today()
print(f"Current date: {today}")

# Get only the current time (oftrn extracted from a datetime object)
current_time = now.time()
print(f"Current time: {current_time}")
