
class Bank:
    def __init__(self,amount):
      self.amount= amount
      self.deposit = 0
      self.amount_withdraw = 0

    def save_data(self):
     with open("data.txt", "w") as f:
        f.write(str(self.amount))
    
    def check_authenticate(self):
       
       self.pass_word = input("enter your 8 digits  pin:")
       if self.pass_word == "27018516":
           print("yeh you have to seccessfully logined ")
           return True
       else:
           print("invalid pin")
           return False

    def _deposit(self):
        self.deposit = int( input("how much money you want to deposit :"))
        self.amount += self.deposit
        self.save_data()
        print(f"you deposited{self.deposit} and you  balance was {self.amount}")
        return self.amount  

    def withdraw (self):
       self.amount_withdraw =int(input("how much money you want to withdraw: "))
       if self.amount >= self.amount_withdraw:
            self.amount  -= self.amount_withdraw
            self.save_data()
            print(f"you withdraw the {self.amount_withdraw}\n remaining balance {self.amount}")
       else:
           print("insufficient funds")

    def run(self):
        if not self.check_authenticate():
            return 
        while True:
            print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit ")
            choice = input("Enter your choice:")
            if  choice == "1":
                self._deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                print(f"{self.amount}")
            elif choice == "4":
                print("Thank you")
                break
            else:
                print("Invalid option ")


s1 = Bank(0)
s1.run()
 