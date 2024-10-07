#!/usr/bin/env python3
# Author: Ali Randy Nurudeen
# Author ID: 133455220
# Date Created: 2024/10/07

import sys
import time

# Check if the correct number of arguments is provided
if len(sys.argv) < 2:
    print('Usage: ./lab2f.py <count>')
    sys.exit(1)

# Assign the value of the first command line argument to the timer
timer = int(sys.argv[1])

# While loop that continues until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

# Initialize the timer
timer = 10

# While loop that continues until timer equals 0
while timer > 0:
    print(timer)
    time.sleep(1)  # Sleep for 1 second to create a countdown effect
    timer -= 1

# Print the final message
print("Time's up!")

