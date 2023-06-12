# PROJECT WHICH WILL HELP YOU TO LEARN MANY CONCEPTS
import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

#This dictionary symbol_count defines the count of each symbol in the slot machine. The keys are symbols ('A', 'B', 'C', 'D') and the values are the counts.
symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

#This dictionary symbol_value defines the value of each symbol in the slot machine. The keys are symbols ('A', 'B', 'C', 'D') and the values are the corresponding values.
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

#This function check_winning takes in the columns of the slot machine, the number of lines, the bet amount, and the symbol values. It checks if there are any winning combinations and calculates the winnings. It returns a tuple of (winnings, winning_lines).
def check_winning(columns, lines, bets, values):
    winnings = 0  # Fixed variable name typo
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bets
            winning_lines.append(line + 1)

    return winnings, winning_lines  # Return the corrected variable name
      
            
                
#This function slot_machine_spin generates the random combinations of symbols for the slot machine. It takes in the number of rows, columns, and the symbols dictionary. It creates a list all_symbols containing all the symbols based on their counts. Then it generates the columns by randomly choosing symbols from all_symbols and removes the chosen symbols to avoid repetition. It returns the columns of the slot machine.  

def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # Corrected typo from symbols.item() to symbols.items()
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns


#This function print_slot_machine prints the slot machine in a formatted way. It takes in the columns of the slot machine and prints each symbol row by row, separating them with '|'.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end='')  # Update the end parameter to ''
        print()

    
#This function deposit asks the user to enter the amount they want to bet. It repeatedly prompts for input until a valid amount greater than zero is entered. It returns the deposited amount.                          
def deposit():# asking the user to enter the amount he want to bet
    while True:
        amount=int(input('ENTER THE AMOUNT YOU WANT TO DEPOSIT: $'))
        
        if amount>0:
            break
        else:
            raise ValueError('PLEASE ENTER THE AMOUNT GREATER THEN ZERO')
    
    return amount    

#This function get_number_of_lines asks the user to enter the number of lines they want to bet on. It repeatedly prompts for input until a valid number between 1 and MAX_LINES is entered. It returns the number of lines.

def get_number_of_lines():
    while True:
        lines=input("ENTER THE NUMBER OF LINES U WANT TO BET ON:(1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print('PLEASE ENTER A VALID NUMBER:')
        else:
            print('ENTER A NUMBER PLEASE:')
            
    return lines        
          
#This function get_bet asks the user to enter the amount they would like to bet. It repeatedly prompts for input until a valid bet amount between MIN_BET and MAX_BET is entered. It returns the bet amount.      
def get_bet():
    while True:
            amount=input("WHAT WOULD YOU LIKE TO BET? $")
            if amount.isdigit():
                amount=int(amount)
                if MIN_BET<=amount<=MAX_BET:
                   break
                else:
                    print(f'PLEASE ENTER A MINIMUM OF 1 DOLLAR OR MORE(BETWEEN ${MIN_BET} and ${MAX_BET}):')
            else:
                print('ENTER A NUMBER PLEASE:')
            
    return amount    
#this function spin represents a single spin of the slot machine. It takes in the current balance and performs the spin process. It asks the user to enter the number of lines and the bet amount, checks if the total bet is within the balance limit, and calculates the total bet. It then generates the slot machine columns, prints them, checks for any winnings, and prints the winnings. It returns the net winnings (winnings - total_bet).
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print('SORRY YOU DONT HAVE THAT MUCH BALANCE.')
        else:
            break

    print(f"YOU ARE BETTING ${bet} ON {lines} LINES. AND YOUR TOTAL BET IS ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, _ = check_winning(slots, lines, bet, symbol_value)  # Ignore the winning_lines
    print(f'YOU WONNNNN  ${winnings}')
    return winnings - total_bet  # Return only the winnings

#This function main is the main entry point of the program. It starts by asking the user to enter the initial balance. Then it enters a loop where it repeatedly asks the user to spin the slot machine or quit. It calls the spin function and updates the balance accordingly.
def main():
    balance = deposit()
    while True:
        print(f"current balance ${balance}")
        answer = input('press enter to spin (q to quit): ')
        if answer == 'q':
            break
        balance += spin(balance)


main()
