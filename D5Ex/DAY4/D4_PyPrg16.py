import datetime

# import pytz # You would need to install pytz: pip install pytz

# Creating a timesone-aware datetime object (using timezone classfor fixedd of)
# UTC offset +5:30 (for Sri Lanka, though daylight saving rules are simplified)

sri_lanka_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now_sri_lanka = datetime.datetime.now(sri_lanka_offset)
print(f"Current datetime in Sri Lanka: {now_sri_lanka}")

# You can convert between timezones using .astimezone()
# If you had pytz installed:
