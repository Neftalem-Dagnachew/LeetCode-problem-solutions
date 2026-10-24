
def Number_Trick_Master():
    print("Welcom to Number trick GAME")

    first_ges = int(input("Enter 3 digit num: "))

    sume_num = 0

    if first_ges and len(first_ges) == 3:
        if first_ges[2] >= 2:
            for i in first_ges:
                if i >= len(first_ges):
                    print("good")
        else:
            print("Tray again")
    else:
        print("Envalid")

Number_Trick_Master()