#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

print("Users older than 25 in batches of 50:")
try:
    for batch in processing.batch_processing(50):
        for user in batch:
            print(user)
except BrokenPipeError:
    sys.stderr.close()
