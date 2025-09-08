def count_words(text):
    words = text.split()
    return len(words)
def count_chars(text):
    chars = {}
    for character in list(text):
        character = character.lower()
        if (character in chars) is False:
            chars[character] = 0
        chars[character] += 1
    return chars
def sort_on(items):
    return items["num"]
def sort_counted_chars(chars):
    output = list({})
    for character in chars:
        output.append({"char": character, "num": chars[character]})
    output.sort(reverse=True, key=sort_on)
    return output