user_input = input().split()
word_count = {}

for word in user_input:
    word_lowercase = word.lower()
    word_count[word_lowercase] = word_count.get(word_lowercase, 0) + 1

for key, value in word_count.items():
    print(f"{key} {value}")
