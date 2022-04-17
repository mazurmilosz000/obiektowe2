from Rectangle import *
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def getdata(line):
        data = line.split(" ")
        print(data)
        if data[0] == '1':
            if len(data) != 3:
                raise ValueError("nieprawidlowa dlugosc")
            print("gitara")
        elif data[0] == '2':
            if len(data) != 4:
                raise ValueError("nieprawidlowo bracie")
            print("git")
if __name__ == '__main__':
    with open("file.txt", "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data]

        print(data)

    for line in data:
        try:
            obj = getdata(line)



