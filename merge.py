import os

list = open("list", "wb")
def merge(a):
	for i in os.listdir(a):
		try:
			list.write(open(a + "/" + i, "rb").read())
			print(a + "/" + i)
		except IsADirectoryError:
			merge(a + "/" + i)

merge("./filterlist")
list.close()

os.system("LANG=iso-8859-1 sed -i 's/[\d128-\d255]//g' list")

