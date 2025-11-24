def group_anagrams(strs):
    """
    Группирует анаграммы из списка строк
    """
    groups = {}

    for word in strs:
        # Сортируем буквы слова чтобы получить ключ
        sorted_word = ''.join(sorted(word))

        # Добавляем слово в соответствующую группу
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]

    # Возвращаем все группы
    return list(groups.values())


# Тестируем программу
if __name__ == "__main__":
    # Тестовые примеры
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    test2 = [""]
    test3 = ["a"]

    print("Группировка анаграмм:")
    print("=" * 30)

    print(f"Вход: {test1}")
    print(f"Выход: {group_anagrams(test1)}")
    print()

    print(f"Вход: {test2}")
    print(f"Выход: {group_anagrams(test2)}")
    print()

    print(f"Вход: {test3}")
    print(f"Выход: {group_anagrams(test3)}")