import os,sys

prefix = "profiles_"
ext = ".csv"

profile = raw_input("Profile name: ")

fullfile = prefix + profile + ext

with open(fullfile, "w"):
	os.system("start excel.exe model-master.xlsm")