def get_contents(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def count_words(filepath):
    content = get_contents(filepath)
    counter = 0
    words = content.split()
    for word in words:
        counter +=1
    return counter

def count_letters(filepath):
    content = get_contents(filepath)
    lettercounts = {}
    lowercontent=content.lower()
    for word in lowercontent:
        for letter in word:
            if letter.isalpha():
                if letter in lettercounts:
                    lettercounts[letter] += 1
                else:
                    lettercounts[letter] = 1
    sorted_letters = dict(sorted(lettercounts.items()))
    return sorted_letters
                    


print(count_words("books/frankenstein.txt"))
print(count_letters("books/frankenstein.txt"))