# 1. Accept from the user some text.Ensure user enters something else raise an exception.
# After that write that text to a file and then read from this file to write to another file simultaneously
# 2. Reading an image to writing to another file simultaneously
import os

from PIL import Image




order_text = 'order.txt'
writer_text = "writer.txt"

class EmptyChecker:
    def __init__(self, file_path):
        self.file_path = file_path


    def emptycheck(self):
        # reduces the overhead of closing files
        # just opens it and closes it
        # automatically closes the file and also closes it during the times of execution
        with open(order_text, "w+") as file:
            try:
                if os.stat(order_text).st_size == 0: # check if size of file is 0
                    raise ValueError
            except ValueError as e:
                print(e)
            else:
                print('File is not empty')



    def raiseExceptionifempty(self):
        with open(order_text, "w+") as file:
            try:
                file_input = (input("Enter your file input:"))
                if len(file_input) == 0:
                    raise Exception("sorry we dont take empty names")
            except Exception:
                print("you did not enteer anything")
                self.raiseExceptionifempty()
            else:
                file.write(file_input)
            finally:
                print(file.read())

    def writetextfilesusingwith(self):
        with open(order_text, "w+") as file, open(writer_text, "w+") as file2:
            try:
                file_input = input("Enter your file input:")
                if len(file_input) == 0:
                    raise Exception
            except Exception:
                print("you did not enter anything")
                self.writetextfilesusingwith()
            else:
                file.write(file_input)
            file.seek(0)
            file2.write(file.read())


# this is how andrew did it
    def write_and_read_to_file(self):
        try:
            text = input("Please add your text here: ")
            if len(text) == 0:
                raise Exception
        except Exception:
            print("Sorry we don't take empty text...")
            self.write_and_read_to_file()
        else:
            with open("homework.txt", "w+") as file:
                file.write(text)
                file.seek(0)
                self.text_storage = file.read()
            with open("second_homework.txt", "w") as file:
                file.write(self.text_storage)
                return self.text_storage

    def read_image_write_file(self):
        with open('lol.png', 'rb') as f,  open('picture_out.png', 'wb') as f2:
            f2.write(f.read())
            Image.open('picture_out.png').show()

a = EmptyChecker(order_text)
a.read_image_write_file()


