text = input("Введи текст:")

words = text.split()
sentences = text.split(".")


def print_stat(words_count=0, letters_count=0, sentences_count=0):
    if words_count:
        if words_count == 1:
            print("В тесте всего одно слово")
        else:
            print(f"Количество слов: {words_count}")
    if letters_count:
        print(f"Количество букв: {letters_count}")
    if sentences_count:
        print(f"Количество предложений: {sentences_count}")


print_stat(words_count=len(words), letters_count=len(text), sentences_count=len(sentences) - 1)


