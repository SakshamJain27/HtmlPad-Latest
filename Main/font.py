def get():
    return int(open("font.txt", "r").read())

def set(value):
    filename = open("font.txt", "w")
    filename.write(value)