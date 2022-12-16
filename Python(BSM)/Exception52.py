# This is Exception Program

try:
    fh = open("testfile", "r")
    fh.write("This is demo testfile")
    print("Written succesfully")
except IOError:
    print("Error : can't find file")
else:
    print("Successfully")