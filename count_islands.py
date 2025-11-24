def num_islands(grid):
    """
    Подсчитывает количество островов на карте
    """
    if not grid:
        return 0

    count = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i, j):
        # Выход за границы или вода
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            return

        # Помечаем как посещенную
        grid[i][j] = "0"

        # Проверяем соседей
        dfs(i + 1, j)  # вниз
        dfs(i - 1, j)  # вверх
        dfs(i, j + 1)  # вправо
        dfs(i, j - 1)  # влево

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count


# Тестируем программу
if __name__ == "__main__":
    # Тестовые примеры
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("Подсчет островов:")
    print("=" * 20)

    print("Пример 1:")
    for row in grid1:
        print(" ", row)
    print(f"Островов: {num_islands([row[:] for row in grid1])}")
    print()

    print("Пример 2:")
    for row in grid2:
        print(" ", row)
    print(f"Островов: {num_islands([row[:] for row in grid2])}")