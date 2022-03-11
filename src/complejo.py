class Complejo:

    def __init__(self, e, i):

        self.__pEntera = e
        self.__pImaginaria = i

    
    def getParteEntera(self):

        return self.__pEntera

    
    def getParteImaginaria(self):
        
        return self.__pImaginaria

    
    def setParteEntera(self, num):

        self.__pEntera = num

    
    def setParteImaginaria(self, num):
        
        self.__pImaginaria = num

    
    def __str__(self):

        if self.getParteImaginaria() > 0:
            return "(" + str(self.getParteEntera()) + " + " + str(self.getParteImaginaria()) + "i" + ")"
        else:
            return "(" + str(self.getParteEntera()) + " " + str(self.getParteImaginaria()) + "i" + ")"


    def __add__(self, numComplejo):

        totalEntera = self.getParteEntera() + numComplejo.getParteEntera()
        totalImaginaria = self.getParteImaginaria() + numComplejo.getParteImaginaria()  
        
        return Complejo(totalEntera, totalImaginaria)

    
    def __mul__(self, numComplejo):

        totalEntera = (self.getParteEntera() * numComplejo.getParteEntera()) - (self.getParteImaginaria() * numComplejo.getParteImaginaria())
        totalImaginaria = (self.getParteEntera() * numComplejo.getParteImaginaria()) + (self.getParteImaginaria() * numComplejo.getParteEntera()) 

        return Complejo(totalEntera, totalImaginaria)