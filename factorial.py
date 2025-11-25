class NumFactorial:
    def __init__(self,number):
        self.number=number

    def factorial(self):
        counter=self.number
        fact=1
        while counter > 0:
            fact *= counter
            counter -= 1
        return fact

somefact=NumFactorial(4)
print(somefact.factorial())

#fixed code EJPN

