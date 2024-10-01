#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "I'm not superstitious, but I'm a little stitous.",
    "Well well well, how the turntables...",
    "Bears. Beets. Battlestar Galactica.",
    "Boy, have you lost your mind, 'cause I'll help you find it!",
    "I am running away from my responsibilities, and it feels good."
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

#0 8 * * * /workspaces/03-data-structures-rishim3000/01-daily_quote.py >> /workspaces/03-data-structures-rishim3000/01-daily_quote.txt
