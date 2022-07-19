from abc import ABC
from abc import abstractmethod

class Database(ABC):
    
    _host="127.0.0.1"
    _user="postgres"
    _password="postgres"
    _database="dugking"

    @abstractmethod
    def query(self, *args):
        """
        传入查询数据的SQL语句并执行
        """

    @staticmethod
    @abstractmethod
    def execute(sql_string):
        """
        执行SQL语句
        """

class Component1(Database):
    

    @staticmethod
    def execute(sql_string):
        print(sql_string,Database._user)
        
    def query(self, *args):
        sql_string = "SELECT * FROM User"
        self.execute(sql_string)

class Component2(Database):


    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        
        sql_string = "SELECT * FROM User"
        self.execute(sql_string)

comp1 = Component1()
comp2 = Component2()
comp1.query()
comp2.query()
