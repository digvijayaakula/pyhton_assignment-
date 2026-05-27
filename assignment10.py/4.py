class DatabaseConnection:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def connect(self):
        print("connected to database")

class MySQLDatabase(DatabaseConnection):
    def __init__(self,host,port,username,password):
        super().__init__(host,port)
        self.username=username
        self.password=password

    def details(self):
        print(self.host)
        print(self.port)
        print(self.username)
        print(self.password)

host=input("enter host : ")
port=int(input("enter port : "))
username=input("enter username : ")
password=input("enter password : ")

obj=MySQLDatabase(host,port,username,password)
obj.connect()
obj.details()