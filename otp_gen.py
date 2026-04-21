import random

def opt_generator():
    return f"{random.randint(0, 999999):06d}"

def main():
    otp_store = {"otp":opt_generator()}
    max_attempts = 3
    print("your otp is: ",otp_store["otp"] )
    print ("Enter the otp for verify it ")

    for attempts in range(1, max_attempts+1):
        user_otp = input(f"attempts {attempts}/{max_attempts} Enter otp: ").strip()
    try:     
        if user_otp == otp_store["otp"]:
            print("Otp is verified successfully :")
            otp_store.clear()
            return
    
       
        remaining = max_attempts - attempts
        if  remaining > 0:
           print(f"Incorrect OTP you have left the {remaining} attempts:")

        else :
         print("otp verification is failed , maximum attempts was reached ")
        otp_store.clear()
    except Exception as e:
            print("Error occurred:", e)

if __name__ == "__main__":

 main()