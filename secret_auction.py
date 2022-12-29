"""
This script implements a basic secret auction program
"""
from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#Get first bid
print(art.logo)
print("Welcome to the secret auction program.")
name = input("What is your name?")
bid = input("What is your bid?")
others = input("Are there any other bidders?").lower()
bid_dict = {name:bid}

#Bidding function
def morebids():
  if others == "yes":
    clear()
    name_oth = input("What is your name?")
    bid_oth = input("What is your bid?")
    others_oth = input("Are there any other bidders?").lower()
    bid_dict[name_oth] = bid_oth
    if others_oth == "yes":
      morebids()
    elif others_oth == "no":
      highest_name = max(bid_dict, key=bid_dict.get)
      highest_bid = bid_dict[highest_name]
      print(f"The winnder is {highest_name} with a bid of {highest_bid}")
  elif others == "no":
      highest_name = max(bid_dict, key=bid_dict.get)
      highest_bid = bid_dict[highest_name]
      print(f"The winnder is {highest_name} with a bid of {highest_bid}")

#Driver
morebids()

  