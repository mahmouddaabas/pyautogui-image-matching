#import scripts from ./scripts/
import scripts.fletching.fletch_and_burn_logs as fletch_burn

#ask user for input to determine what script to run
input = input("What script would you like to start?")

#parse input to int and run the chosen script
choice = int(input)
match choice:
    case 1:
        fletch_burn.main()