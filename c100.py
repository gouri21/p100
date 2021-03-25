class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def check_balance(self):
        print("your balance is 50,000")
    def withdrawal(self,amount):
        new_amount = 50000-amount
        print("you have withdrawn"+str(amount)+"your remaining balance is"+str(new_amount))  
def main():
    cardnumber = input("enter ur cardnumber")
    pin = input("enter ur pin")     
    new_user = Atm(cardnumber,pin)
    print("1.balanceenguiry 2.withdrawal")
    activity = int(input("enter activity number"))
    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("enter the amount"))
        new_user.withdrawal(amount)
    else:
        print("enter a valid number")
if __name__ == "__main__":
    main()                     