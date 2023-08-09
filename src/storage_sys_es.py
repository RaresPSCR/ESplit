class Variable:
    def __init__(self) -> None:
        self.var={}
    def add_variable(self,name,value):
        self.var[name]=value
    #fast search
    #remove variables