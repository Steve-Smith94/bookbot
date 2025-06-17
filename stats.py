#counts how many words are in the book
def count (the_book):
    count_list = the_book.split()
    return len(count_list)

#counts how many times each character occurs in the string
def char_count (the_book):
    ch_count = {}
    for char in the_book:
        char = char.lower()
        if char in ch_count:
            ch_count[char] = ch_count[char] + 1
        else:
            ch_count[char] = 1
    return ch_count

#sorter helper function 
def sort_on(dict):
    return dict["num"]

#takes the dictionary of characters and their counts and returns a sorted list of dicts
def sorted_counts (the_book):
    sort_count = []
    for char, num in the_book.items():
        if char.isalpha():
            sort_count.append({"char": char, "num": num})
    sort_count.sort(reverse=True, key=sort_on)
    return sort_count

