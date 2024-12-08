import re

def read_file(file_name):
    """Читає текстовий файл і повертає його вміст."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка під час читання файлу: {e}")
        return None

def get_first_sentence(text):
    """Повертає перше речення з тексту."""
    sentences = re.split(r'[.!?]', text.strip())
    return sentences[0] if sentences else ""

def sort_words(text):
    """Повертає відсортовані українські та англійські слова."""
    words = re.findall(r'\b[а-яА-ЯёЁіІїЇєЄa-zA-Z]+\b', text)
    uk_words = sorted([word for word in words if re.match(r'^[а-яА-ЯёЁіІїЇєЄ]+$', word)], key=str.lower)
    en_words = sorted([word for word in words if re.match(r'^[a-zA-Z]+$', word)], key=str.lower)
    return uk_words, en_words

def main():
    file_name = 'input.txt'
    text = read_file(file_name)
    if text is None:
        return

    # Вивід першого речення
    first_sentence = get_first_sentence(text)
    print(f"Перше речення:\n{first_sentence}\n")

    # Сортування слів
    uk_words, en_words = sort_words(text)
    all_words = uk_words + en_words
    print("Відсортовані українські слова:")
    print(", ".join(uk_words))
    print("\nВідсортовані англійські слова:")
    print(", ".join(en_words))
    print(f"\nЗагальна кількість слів: {len(all_words)}")

if __name__ == '__main__':
    main()
