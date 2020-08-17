import os
import shutil
from datetime import datetime


print(os.getcwd())
print("************************")
print(os.listdir("../"))
print("*" * 30)
print(os.environ["HOME"])

# f = open("practice.txt","w+")
# f.write("I'm exploring os and shutils")
# f.close()

# shutil.move("practice.txt", "../")

dt = datetime.now()
print(dt)
dt = datetime.ctime(datetime.today())
print(dt)