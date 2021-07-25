from silent_auction_art import logo

def collect_bids():
    while True:
        print(logo)
        name = input("What is your name?: ")
        amount = int(input("What is your bid?: $"))
        bids[name] = amount

        again = input("Is there another bidder? Enter yes or no: ")

        if again.lower() == "no":
            break


def find_winner():
    max = 0
    winner = [""]
    for name in bids:
        amount = bids[name]
        if amount > max:
            max = amount
            winner[0] = name
        elif amount == max:
            winner.append(name)
    if len(winner) == 1:
        return f"The winner of this auction is {winner[0]}."
    elif len(winner) == 2:
        return f"This auction tied between {winner[0]} and {winner[1]}."
    else:
        return "No winner, multiple bidders tied!"


bids = {}
collect_bids()
winner = find_winner()
print(winner)

