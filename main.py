import random

Symbols = ['🍒', '🍉', '🍋', '🏁', '⭐']

def spin_row(symbols: list[str]):
    return [random.choice (Symbols) for _ in range(3)]

     
def print_row(row):
    print("*" * 15)
    print(" | ".join(row))
    print("*" * 15)


def get_payout(row,bet):
    if row[0] == row [1] == row[2]:
        if row [0] == '🍒':
            return bet * 3
        elif row [0] == '🍉':
            return bet * 4
        elif row [0] == '🍋':
            return bet * 6
        elif row [0] == '🏁':
            return bet * 7
        elif row [0] == '⭐':
            return bet * 10
    return 0
        


def main():
    balance = 100 
    print("*" * 24)
    print("welcome to python slots")
    print("Symbols:  🍒 🍉 🍋 🏁 ⭐")
    print("*" * 24)

    while balance > 0:
        print(f"Current balance: ${balance}")


        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("please enter an amount not a word")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row(Symbols)
        print("spinning....\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0 :
            print(f"you've won  $ {payout}")
        else:
            print("oop's u've lost this round")

        balance += payout


        while True:

         play_again = input("Do you wanna play again? (Y/N): ").upper()

         if play_again in ['Y','N']:
           break
         print("please enter Yes (Y) or No (N).")
       
        if play_again != 'Y':
            break

    print("********************************************")
    print(f"Game over! Your Final balance is ${balance}\n")
    print("thanks for playing, see you later!")
    print("********************************************")


if __name__ == '__main__':
    main()