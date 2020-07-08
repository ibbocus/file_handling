class TextFileHandling:
    def __init__(self, file_path, text_storage = None):
        self.file_path = file_path
        self.text_storage = text_storage

    # Going to read in two ways and write in two ways

    def readtextfile(self):
        #open file
        #read the file
        #close the file
        try:
            file = open(self.file_path, 'r') #try = put the code you think will raise an error
        except Exception as e: # except - catches the thrown exception
            print(e)
        else: # if the exception is not thrown then run the code as normal. You can add a finally clause that will perform regardless of whether an excpetion is thrown or no
            # self.text_storage = file.read(3) # this reads 3 characters in  the text file
            self.text_storage = file.readline()
            self.text_storage = file.readline()
            print(file.tell()) # outputs the location of the pointer, after read lines the pointer moves to the end of what has been read
            file.seek(0) # file.seek moves the pointer to the character stated. 1 is current postion, 3 is distance?
            self.text_storage = file.readlines()
            file.close()
        return self.text_storage

    def writetextfile(self):
        file = open("writer.txt", 'w')
        file.write("my first python created file\n")
        file.close()
        file = open("writer.txt", "a+") # a+ means append and read
        file.write("adding to txt file")
        file.seek(0)
        self.text_storage = file.read()
        file.close()
        return self.text_storage

    def readtextfilesusingwith(self):
        # reduces the overhead of closing files
        # just opens it and closes it
        # automatically closes the file and also closes it during the times of execution
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def writetextfilesusingwith(self):
        with open("writer.txt", "w+") as file:
            file.write("using writer with with")
            file.seek(0)
            self.text_storage = file.read()
            return self.text_storage

    def playingwithpythonosmodule(self):
        import os
        print(os.getcwd(), "is the current folder") # cwd = current window
        # os.remove("writer.txt")
        print(os.listdir()) # if empty, will return a list of the files in cwd
        # os.chdir("C:\Users\Ib_Bo\PycharmProjects\Com_1")
        # os.mkdir("Ayb")
        os.rmdir("Ayb") # this will remove the directory stated



