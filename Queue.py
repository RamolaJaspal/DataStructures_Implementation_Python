class Queue:
    '''This is custom implementation of Queue Data strcuture'''

    def __init__(self):
       self.__Front=-1
       self.__Rear=-1
       self.__Array=[]
    def dequeue(self):
        if self.__Front==-1:
            raise Exception("No Element in Queue")
        element=self.__Array[self.__Front]
        del self.__Array[self.__Front]
        self.__Front+=1
        if self.__Front > self.__Rear:
            self.__Front=-1
            self.__Rear=-1
        return element
    def enqueue(self,element):
        if self.__Rear==-1:
            self.__Rear=0
            self.__Front=0
            self.__Array.append(element)
        else:
            self.__Rear+=1
            self.__Array.append(element)
    

    def __str__(self):
        return str(self.__Array)