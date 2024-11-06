import re

def main():
    # Sample text to search
    text = "Python is a powerful programming language. It was created by Guido van Rossum and first released in 1991."

    # Example 1: Match words that start with 'P'
    pattern = r'\bP\w+'  # '\b' is a word boundary, and '\w+' matches one or more word characters
    matches = re.findall(pattern, text)
    print("Words that start with 'P':", matches)

    # Example 2: Search for the word 'language'
    if re.search(r'\blanguage\b', text):
        print("The word 'language' was found in the text.")
    else:
        print("The word 'language' was not found in the text.")

    # Example 3: Extract all years (four-digit numbers)
    years = re.findall(r'\b\d{4}\b', text)
    print("Years found in the text:", years)

    # Example 4: Replace 'Python' with 'Java'
    modified_text = re.sub(r'\bPython\b', 'Java', text)
    print("Modified text:", modified_text)

    # Example 5: Split the text into sentences using period as the delimiter
    sentences = re.split(r'\. ', text)
    print("Sentences in the text:", sentences)

if __name__ == "__main__":
    main()
