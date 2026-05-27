class FileLogger:
    def log(self,message):
        print("file :",message)

class ConsoleLogger:
    def log(self,message):
        print("console :",message)

def logger(logger,message):
    logger.log(message)

choice=input("file or console : ")
message=input("enter message : ")

if choice=="file":
    obj=FileLogger()
elif choice=="console":
    obj=ConsoleLogger()
else:
    obj=None

if obj!=None:
    logger(obj,message)
else:
    print("invalid choice")