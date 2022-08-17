import lib
import art

print(art.logo)
auction = True
bids = {}
while auction:
    name = input("Please enter the name: ")
    bid = int(input("Please enter the bid: $"))
    bids[name]=bid
    more_bids = input("Are there any other users who want to bid? (Yes or No)").lower()
    if more_bids != "yes":
        auction = False
    lib.clear()

highest_bid = max(bids, key=bids.get)

print(f"The winner is {highest_bid} with a bid of ${bids[highest_bid]}")