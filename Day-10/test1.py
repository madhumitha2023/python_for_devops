import sys
import os

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# result = num1 + num2
# print(result)

#in command line check for the list of environment variables already available type env
#type export password = "madhu"

name = os.getenv("password")
print(name)

