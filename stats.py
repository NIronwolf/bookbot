def sort_on(items):
    return items["cnt"]


def get_num_words(text):
    return len(text.split())


def get_character_count(text):
    counts_dict = {}
    for char in text:
        char = char.lower()
        counts_dict[char] = counts_dict.get(char, 0) + 1

    list_of_counts = [{"char": x, "cnt": y} for x, y in counts_dict.items()]
    list_of_counts.sort(reverse=True, key=sort_on)
    return list_of_counts
