
class Stack:
    '''This class is to implement 
    the stack data structure'''
    Number_of_Stacks=0
    def __init__(self):
        Stack.Number_of_Stacks+=1
        self.__Array=list()
        self.__top=-1
    def push(self,element):
        self.__Array.append(element)
        self.__top==self.__top+1
    def pop(self):
        last_element=self.__Array[self.__top]
        del self.__Array[self.__top]
        return last_element
    def peek(self):
        return self.__Array[self.__top]
    
    def __str__(self):
        return str(self.__Array)
