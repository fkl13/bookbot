def main():
    book_path = './books/frankenstein.txt'
    file_contents = read_file(book_path)
    num_words = count_words(file_contents)
    print("{num_words} words found in the document")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()