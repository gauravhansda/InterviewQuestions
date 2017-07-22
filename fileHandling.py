class FILEHANDLING():

    def __init__(self):
        self.file_name = "file.txt"

    # Remove blank lines from the file
    def remBlanks(self):
        with open(self.file_name, 'r') as inp:
            lines = inp.readlines()
        print lines
        with open("out.txt", 'w') as out:
            for line in lines:
                if not line.isspace():
                    out.writelines(line)



if __name__ == '__main__':
    fh = FILEHANDLING()
    fh.remBlanks()

