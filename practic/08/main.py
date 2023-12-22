import pymorphy2
from collections import Counter
from translate import Translator

# Чтение текстового файла с диалогом
with open("messages.txt", "r", encoding="utf-8") as file:
    dialog_text = file.read()

morph = pymorphy2.MorphAnalyzer()
normalized_words = [morph.parse(word)[0].normal_form for word in dialog_text.split()]

word_count_dict = Counter(normalized_words)

translator= Translator(to_lang="en", from_lang="ru")
translated_words = {word: translator.translate(word) for word in word_count_dict.keys()}

with open("result.txt", "w", encoding="utf-8") as result_file:
    result_file.write("Исходное слово | Перевод | Количество упоминаний\n")
    for word, count in word_count_dict.most_common():
        translation = translated_words[word]
        result_file.write(f"{word} | {translation} | {count}\n")