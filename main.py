def main():
    book_path = './books/frankenstein.txt'
    file_contents = read_file(book_path)
    num_words = count_words(file_contents)
    print("{num_words} words found in the document")
    num_chars = count_characters(file_contents)
    print(num_chars)
    print_report(book_path, num_words, num_chars)

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
        if lowered in map:
            map[lowered] += 1
        else:
            map[lowered]=1
    return map

def print_report(path, word_count, char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    chars = []
    for k,v in char_count.items():
        chars.append({'key': k, 'value':v})

    sort_on = lambda d: d['value']    
    chars.sort(reverse=True, key=sort_on)
    for c in chars:
        k = c['key']
        if not k.isalpha():
            continue
        v = c['value']
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

main()