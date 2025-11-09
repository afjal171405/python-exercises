# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

fileExtension = input("enter file name with extension ")

fname = fileExtension.split(".")

print("the extension of file is : " + repr(fname[-1]))