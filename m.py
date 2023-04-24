import lottery
import os

Lottery = lottery.lottery()


# print(f"\t{Lottery.getAward()}")


looping = True

while looping == True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\t------------------------------ Lottery ------------------------------")

    tickets = input(f"\n\tHow many tickets do you want? 3 max:")

    try: 
        int_tickets = int(tickets)
        i = 0

        

        if (int_tickets < 4):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\t------------------------------ Lottery ------------------------------")
            print(f"\tCongats! You have won:")

            while i < int_tickets:

                print(f"\t\t{Lottery.getAward()}")
                i = i + 1
            

        elif (int_tickets > 3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\t------------------------------ Lottery ------------------------------")

            print(f"\n\t\tToo many tickets!")
        
        


    except ValueError or tickets > 3:
        print("\t\tInvalid input, please try again")



    play_again = input("\n\n\tDo you want to play again? y/N")

    if (play_again == "n"):
        break
    elif (play_again == "y"):
        print("temp")
    else: 
        break


    