# Absolute File Path:
with open("/home/moazzam/Desktop/NCTP/name.txt", mode="r+") as file:
    test = file.read()
    print(test)

# Relative File Path:
with open("./../../../../../NCTP/name.txt", mode="r+") as file:
    test1 = file.read()
    print(test1)

