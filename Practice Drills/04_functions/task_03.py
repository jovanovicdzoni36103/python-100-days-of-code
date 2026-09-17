"""
TASK 03 - Connect two functions into a mini pipeline             [Level 3]

Create two functions:
- clean_text(text) - returns text with trimmed whitespace, converted to lowercase
- word_count(text) - returns the number of words in text

Given: raw = "  This Is A Sample Review  "

Pass raw through clean_text(), then pass the result through word_count().
Print the cleaned text and the word count.

AI/ML: A real text processing pipeline (for NLP) is a series of small functions called one after another: cleaning, tokenization, counting, etc.
"""

raw = "  This Is A Sample Review  "

def clean_text(text):
    return text.strip().lower()

def word_count(text):
    words = text.split()
    return len(words)

cleaned_text = clean_text(raw)
count = word_count(cleaned_text)

print(f"Očišćen tekst: '{cleaned_text}'")
print(f"Broj reči: {count}")