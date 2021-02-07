import os
import time

os.system("python -m venv venv")
os.system("venv/Scripts/activate.bat")
os.system("pip install -r requirements.txt")
while True:
	os.system("python priceCollect.py")
	x = input("Continue (y/n)? ")
	if x == "n" or x == "N": break

print("\n\n\n Closing...")
time.sleep(10)
