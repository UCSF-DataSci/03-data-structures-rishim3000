#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string

def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies

    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation)) #imported string package to remove many common punctuation signs in one line
    text = text.replace("\n", " ")#rest of these are other more rare punctuations that I manually removed
    text = text.replace(";", " ")
    text = text.replace("-", " ")
    text = text.replace("—", " ")
    text = text.replace("“", " ")
    text = text.replace("’", " ")
    text = text.replace("”", " ")
    text = text.replace("‘", " ")
    words = text.split()
  
    for word in words: #running dict of word frequencies
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1      
    sorted_frequencies = dict(sorted(frequencies.items()))  #sorted dict alphabetically    
    return sorted_frequencies
# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
           text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        #commented out this piece of given code - i was getting two copies of dict with it
        # Print results
        #for word, count in frequencies.items():
           #print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)