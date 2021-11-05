import datetime, time
import os
n1 = datetime.datetime.now()

print(n1)

os.system('ls')

n2 = datetime.datetime.now()
print(n2)

n3 = n2 - n1
print(n3)