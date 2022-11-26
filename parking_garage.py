class ParkingGarage:
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def takeTicket(self):
        if len(self.parkingSpaces) == 0:
            print("Parking Garage is full!")
        else:
            self.tickets.remove(self.tickets[-1])
            self.parkingSpaces.remove(self.parkingSpaces[-1])
            print("There are",len(self.tickets),"tickets and",len(self.parkingSpaces),"parking spaces left.")

    def payForParking(self):
        payment = input("Enter 5 to pay for your parking: ")

        if payment == '5':
            self.currentTicket['Paid'] = True
            print("You paid for your parking, you have 15 minutes to leave.")
        else:
            self.currentTicket['Paid'] = False
            print(payment)




    def leaveGarage(self):
        if self.currentTicket['Paid'] == True:
            print("Thank you, have a good day.\n")
            self.currentTicket['Paid'] = True
            self.tickets.append(self.tickets[-1]+1)
            self.parkingSpaces.append(self.parkingSpaces[-1]+1)
            print("There are now",len(self.tickets),"tickets and",len(self.parkingSpaces),"parking spaces left.")

        elif self.currentTicket['Paid'] == False:
            payment = input("Enter 5 to pay for your parking: ")
            if payment == '5':
                self.currentTicket['Paid'] = True
                self.tickets.append(self.tickets[-1]+1)
                self.parkingSpaces.append(self.parkingSpaces[-1]+1)
                print("You paid for your parking, you have 15 minutes to leave.\nThank you, have a good day.\n")
                print("There are now",len(self.tickets),"tickets and",len(self.parkingSpaces),"parking spaces left.")

            
            
                

def Run():
    
    car = ParkingGarage()
    print("\nWelcome to Cota's Parking Garage!\n")

    print("Please take a ticket.")

    printedTicket = input("Enter T to take ticket: ")

    if printedTicket.upper() == 'T':
        car.takeTicket()
        car.payForParking()
        car.leaveGarage()
    

    else:
        print('Error')

Run()