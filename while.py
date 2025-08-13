number=59


i=3

while i>0:
    guess_no=int(input("GUess a number between 1 to 100"))
    if guess_no<1 or guess_no>100:
        print("Please enter a valid number")
        continue
    else:
        if number==guess_no:
            print("you guessed the correct number")
            break
        else:
         print("YOur guess is not correct")
         i=i-1
    