# Can you change the self-parameter inside a class to something else (say“asta”). 
# Try changing self to “slf” or “asta” and see the effects. Use Q no.5.


from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(asta, fro, to):
        print(f"Ticket is booked in train no: {asta.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")

# We can use slf, asta or any other name but for convenience we use self