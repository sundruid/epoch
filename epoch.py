#!/usr/bin/env python3


import sys
import time


from datetime import datetime, timedelta

# Function to display usage information
def usage():
    print("Usage: {} [@<epoch>] [-beat] [-h]".format(sys.argv[0]))
    print("  If no argument is provided, the current epoch time is printed.")
    print("  If @<epoch> is provided, it will convert the given epoch time to local time.")
    print("  -beat  Print the current Swatch Internet Time (Beat Time).")
    print("  -h     Show this help message.")
    sys.exit(1)

# Function to calculate and print Swatch Internet Time (Beat Time)
def print_beat_time():
    utc_seconds = int(time.time())
    seconds_since_midnight_bmt = (utc_seconds + 3600) % 86400  # Adjust to BMT (UTC+1)
    beat_time = (seconds_since_midnight_bmt * 1000) // 86400  # Calculate beats
    print("@{:03d}".format(beat_time))

# Function to print the current epoch time
def print_epoch_time():
    print(int(time.time()))

# Function to convert epoch to local time
def convert_epoch_to_local(epoch):
    try:
        epoch = int(epoch.lstrip("@"))
        local_time = datetime.utcfromtimestamp(epoch) + timedelta(hours=time.localtime().tm_gmtoff // 3600)
        print(local_time.strftime("%Y-%m-%d %H:%M:%S"))
    except ValueError:
        usage()

# Main program logic
if len(sys.argv) == 1:
    # No argument, print current epoch time
    print_epoch_time()

elif len(sys.argv) == 2:
    arg = sys.argv[1]

    if arg == "-h":
        # Show help message
        usage()

    elif arg == "-beat":
        # Show Swatch Internet Time (Beat Time)
        print_beat_time()

    elif arg.startswith("@"):
        # Convert provided epoch time to local time
        convert_epoch_to_local(arg)

    else:
        # Invalid argument, show usage
        usage()

else:
    # More than one argument provided, show usage
    usage()

    
