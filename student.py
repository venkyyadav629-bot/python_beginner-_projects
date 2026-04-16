class Student:
    roll_number = 50
    def __init__(self,elgibility):
        
        self.elgibility= elgibility
    def check (self): 
        score = int(input("enter your score:"))
        if score  <= self.elgibility :
            print("Congrates your are elgible for this collge \n let move to next step " )
            print("grand welcome to our siddartha  institue of engineeringa and technology")
            return True
        else:
            print("you are not eligibil for this university try to move with other one ")
            return False

    def branch_select(self):
        self.user_branch = input ("enter which branch are you willing to study here:").upper()
        branch={ 'ECE':50000, 'EEE':48000,'MECH':45000,'CIVIL':44000,}
        if self.user_branch in branch:
            self.fees = branch[self.user_branch]
            print(f"you choose {self.user_branch} and it fees was {self.fees}")
            return True
        else:
            print("please enter a valid branch \n you enter invalid branch ")
            return False

    def _details_entering(self):
        Student.roll_number +=1 
        self.roll_no = Student.roll_number
        self.name = input("Enter your name :").upper()
        self.date_of_birth = input("enter your date of birth:")

        print("your registration was successfully completed")
        
    def id_details(self):
        print("<<< ID DETAILS >>>\n")
        print(f"NAME = {self.name}")
        print(f"BRANCH = {self.user_branch}")
        print(f"DOB = {self.date_of_birth}")
        print(f"ROLL.NO={self.roll_no}")
               
               

s1= Student(500)
if s1.check():
 if s1.branch_select():
   s1._details_entering()
   s1.id_details()


