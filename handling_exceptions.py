from text_file import TextFileHandling

file_path = "oder.txt"


class Exceptions:
    def __init__(self, file_path, text_storage="none"):
        self.file_path = file_path
        self.text_storage = text_storage

    def palyingwithexceptions(self):
        try:
            file = open(file_path, "r")
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            print("i am in the else clause")
            self.text_storage = file.read()
            file.close()
        finally:
            print("this will always run")
            return self.text_storage

    def raiseException(self):
        while True:
            try:
                name = str(input("enter you name"))
                if len(name) == 0:
                    raise ValueError
                return print(name)
            except ValueError:
                print("please enter a valid name")




    def raiseException2(self):
        try:
            name = (input("Enter your name: "))
            if len(name) == 0:
                raise Exception("sorry we dont take empty names")
        except Exception:
            self.raiseException2()
        else:
            print("Thank you for giving your name {}".format(name))





a = Exceptions(file_path)

a.raiseException2()
