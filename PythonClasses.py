class fauna:
    legs:int
    wings:int
    tail:bool
    featers:bool
    def __init__(self):
        self.legs=4
        self.wings=2
        self.tail=1
        self.featers=1
        #print("My name is :"+str(self.__getattribute__("")))
        print("I belong to the class: fauna"+str(self.__class__))
        
        
        
class animal(fauna):
    
    
   
    def __init__(self):
        self.legs=4
        self.wings=0
        self.tail=1
        self.featers=0
        print(" I belong to fauna's sub class "+str(self.__class__))
        
def main():
    x=fauna()
    y=animal()
    
    
if __name__=="__main__":
    main()