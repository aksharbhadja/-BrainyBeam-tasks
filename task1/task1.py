import os
import re

def count_paragraphs(text):
    # characters Split by two or more newline characters to get paragraphs
    paragraphs = text.split('\n\n')
    return len([para for para in paragraphs if para.strip()])  # Count non-empty paragraphs

def count_sentences(text):
    # I used regex to split sentences by common sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.!?]+', text)
    return len([sentence for sentence in sentences if sentence.strip()])  # Count non-empty sentences

def count_words(text):
    # Using regex to split by any non-word character
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def get_doc_size(file_path):
    # To Get the size of the document in bytes
    return os.path.getsize(file_path)

def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    paragraphs_count = count_paragraphs(text)
    sentences_count = count_sentences(text)
    words_count = count_words(text)
    doc_size = get_doc_size(file_path)

    # Display the results
    print(f"Number of paragraphs: {paragraphs_count}")
    print(f"Number of sentences: {sentences_count}")
    print(f"Number of words: {words_count}")
    print(f"Document size: {doc_size} bytes")


file_path = 'C:/Users/parul/Desktop/internship/task1/test.txt'  # we can replace this path according to our use
analyze_text_file(file_path)    #function call
