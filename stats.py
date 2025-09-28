def word_count(text):
    return len(text.split())


def count_chars(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_char_counts(counts):
    items = []
    for ch, n in counts.items():
        items.append({"char": ch, "num": n})
    items.sort(key=sort_on, reverse=True)
    return items

def sort_on(item):
    return item["num"]