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
def count_charachters(file_contents):
    lowered_string = file_contents.lower()
    character_list = [x for x in lowered_string]
    count_dict ={}

    for i in character_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    print (count_dict)

def main():

    file_contents = read_book()
    count_words(file_contents)
    count_charachters(file_contents)

if __name__ == "__main__":
    main()