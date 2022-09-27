class Person:
    def GetPerson(self):
        self.__name=input("Enter Name: ")
        self.__age=int(input("Enter Age: "))
    def PutPerson(self):
        print(self.__name,self.__age)

    def __gt__(self, T):
      if (self.__age > T.__age):
        return True
      else:
        return False

    def __lt__(self, T):
        if (self.__age < T.__age):
            return True
        else:
            return False


P1=Person()
P2=Person()

P1.GetPerson()
P2.GetPerson()


if(P1>P2):
    print("Elder Person: ")
    P1.PutPerson()
elif(P1<P2):
    print("Elder Person: ")
    P2.PutPerson()
else:
    print("Both Are Equal: ")
    P1.PutPerson()
    P2.PutPerson()
