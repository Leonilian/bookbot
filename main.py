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

print(count_words("books/frankenstein.txt"))