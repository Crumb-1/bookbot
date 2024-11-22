def read_book():
    file_path = ("/Users/rewc/workspace/github.com/Crumb-1/bookbot/books/frankenstein.txt")
    print (f"\n--Book bot initiating for {file_path}--", end = "\n")
    
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for i in words:
        count += 1
    print (f"\nThere were {count} words found in this file" , end="\n \n")
def count_charachters(file_contents):
    lowered_string = file_contents.lower()
    character_list = [x for x in lowered_string if x.isalpha()]
    count_dict ={}
    
    for i in character_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    sorted_characters = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_characters:
        print(f"{char} was found {count} times ", end="\n")

    print("\n--End Report--")
def main():

    file_contents = read_book()
    count_words(file_contents)
    count_charachters(file_contents)

if __name__ == "__main__":
    main()