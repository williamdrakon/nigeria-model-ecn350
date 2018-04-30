import os,sys

try:
	profile = raw_input("Profile name: ")
except NameError:
	#this is done in case the user is running 3.6
	profile = input("Profile name: ")

with open("profile-log.txt", "a") as f:
	f.write(profile + "\n")
	print(sys.path[0])
	os.system("start excel.exe model-master.xlsm")