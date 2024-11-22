def read_book():
    with open("/Users/rewc/workspace/github.com/Crumb-1/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for i in words:
        count += 1
    print (count)

def main():

    file_contents = read_book()
    count_words(file_contents)

if __name__ == "__main__":
    main()