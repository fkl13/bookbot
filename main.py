def main():
    book_path = './books/frankenstein.txt'
    file_contents = read_file(book_path)
    num_words = count_words(file_contents)
    print("{num_words} words found in the document")
    num_chars = count_characters(file_contents)
    print(num_chars)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    map = {}
    for c in text:
        lowered = c.lower()
        if c in map:
            map[c] += 1
        else:
            map[c]=1
    return map

main()