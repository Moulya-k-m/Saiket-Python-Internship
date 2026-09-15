filename = input("Enter the text file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    words = text.split()
    lines = text.splitlines()

    word_count = {}

    for word in words:
        word = word.lower().strip(".,!?;:\"'()[]")

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\n===== File Analysis =====")
    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", len(text))

    print("\nMost Common Words:")

    remaining_words = word_count.copy()

    for i in range(10):
        if len(remaining_words) == 0:
            break

        most_common_word = ""
        highest_count = 0

        for word in remaining_words:
            if remaining_words[word] > highest_count:
                most_common_word = word
                highest_count = remaining_words[word]

        print(most_common_word, ":", highest_count)

        del remaining_words[most_common_word]

except FileNotFoundError:
    print("File not found.")

