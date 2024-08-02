def main():
    book_path = './books/frankenstein.txt'
    file_contents = read_file(book_path)
    print(file_contents)

def read_file(path):
    with open(path) as f:
        return f.read()

main()