def get_num_words(book_text):
    return len(book_text.split())

def get_count_char(text):
    counts = {}

    for ch in text.lower():
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_list(items):
    result = []
    for ch, count in items.items():
        if ch.isalpha():
            result.append({"char": ch, "num": count})
    result.sort(key=sort_on, reverse=True)

    return result