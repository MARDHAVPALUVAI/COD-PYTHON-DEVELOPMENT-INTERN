def count_unique_words(file_path):
    word_count = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?-").').lower()
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
        for word, count in word_count.items():
            print(f'{word}: {count}')

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
file_path ='sample.'
count_unique_words(file_path)
