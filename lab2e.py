#!/usr/bin/env python3
# Author: Ali Randy Nurudeen
# Author ID: 133455220
# Date Created: 2024/10/07

import sys
import time

# Initialize the timer
timer = 10

# While loop that continues until timer equals 0
while timer > 0:
    print(timer)
    time.sleep(1)  # Sleep for 1 second to create a countdown effect
    timer -= 1

# Print the final message
print("Time's up!")

