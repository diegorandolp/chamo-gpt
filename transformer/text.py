with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("[Length]", len(text))
print("[Text]")
print(text[:500])

chars = sorted(list(set(text)))
vocab_size = len(chars)
print("Vocabulary", ''.join(chars))

