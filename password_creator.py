
def create_pass_word():
     pass_word =  input("create your password :")
     with open("pass_word,txt","w") as f:
      f.write(pass_word)

def login_():
    max_attempts = 3
    for attempts in range(1, max_attempts + 1):
     login = input("enter your pass word: ")
     with open("pass_word,txt","r") as f:
      saved_pass = f.read()
     if login == saved_pass:
        print(" You Enter A Correct Pass_Word :")
        break
     else:
         remaining = max_attempts - attempts

         print (f" incorrect {remaining} Attempts left , Enter:")
    else:      
      print("invalid you reach the maximum option:")


create_pass_word()
login_()
