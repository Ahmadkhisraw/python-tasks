def remove_separators(string):
    words = string.split()
    cleaned_words = [word for word in words if word.isalpha()]
    return ' '.join(cleaned_words)

def read_file_data_word_by_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read()
        words = remove_separators(words)
        words = words.split()
    return words

def write_list_to_file(file_name, lst):
    with open(file_name, 'w') as file:
        file.write("number of unique words: " + str(len(lst)) + '\n')
        file.write("==========================\n")
        for word in lst:
            file.write(word + '\n')

def sort_words_in_alphabetical_order(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

words = read_file_data_word_by_word('data.txt')
words = sort_words_in_alphabetical_order(words)
words = remove_duplicates(words)
write_list_to_file('sorted_data.txt', words)