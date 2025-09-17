import random
import re


class Position:
    """Представляет позицию на игровом поле"""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """Делает объект Position хэшируемым для использования в set"""
        return hash((self.row, self.col))

    def __str__(self):
        return f"({self.row}, {self.col})"

    def is_valid(self, grid_size: int = 8):
        """Проверяет, находится ли позиция в пределах поля"""
        return 0 <= self.row < grid_size and 0 <= self.col < grid_size

    def get_adjacent(self):
        """Возвращает соседние позиции (вверх, вниз, влево, вправо)"""
        return [
            Position(self.row - 1, self.col),  # вверх
            Position(self.row + 1, self.col),  # вниз
            Position(self.row, self.col - 1),  # влево
            Position(self.row, self.col + 1)  # вправо
        ]


class Element:
    """Представляет игровой элемент на поле"""
    TYPES = ['A', 'B', 'C', 'D', 'E']

    def __init__(self, element_type: str = None):
        if element_type is None:
            self.type = random.choice(self.TYPES)
        else:
            self.type = element_type if element_type in self.TYPES else 'A'

    def __str__(self):
        return self.type

    def __eq__(self, other):
        return isinstance(other, Element) and self.type == other.type

    def matches(self, other):
        """Проверяет, совпадает ли с другим элементом"""
        return self == other


class GameGrid:
    """Управляет игровым полем"""

    def __init__(self, size: int = 8):
        self.size = size
        self.grid = []
        self._initialize_grid()

    def _initialize_grid(self):
        """Инициализирует поле случайными элементами"""
        for row in range(self.size):
            grid_row = []
            for col in range(self.size):
                grid_row.append(Element())
            self.grid.append(grid_row)

    def get_element(self, position: Position):
        """Получает элемент в заданной позиции"""
        if position.is_valid(self.size):
            return self.grid[position.row][position.col]
        return None

    def set_element(self, position: Position, element: Element):
        """Устанавливает элемент в заданную позицию"""
        if position.is_valid(self.size):
            self.grid[position.row][position.col] = element

    def swap_elements(self, pos1: Position, pos2: Position):
        """Меняет местами два элемента"""
        if not (pos1.is_valid(self.size) and pos2.is_valid(self.size)):
            return False

        element1 = self.get_element(pos1)
        element2 = self.get_element(pos2)

        self.set_element(pos1, element2)
        self.set_element(pos2, element1)
        return True

    def find_matches(self):
        """Находит все совпадения на поле"""
        matches = set()

        # Проверяем горизонтальные совпадения
        for row in range(self.size):
            count = 1
            current_element = self.grid[row][0]
            for col in range(1, self.size):
                if self.grid[row][col].matches(current_element):
                    count += 1
                else:
                    if count >= 3:
                        for i in range(col - count, col):
                            matches.add(Position(row, i))
                    count = 1
                    current_element = self.grid[row][col]

            if count >= 3:
                for i in range(self.size - count, self.size):
                    matches.add(Position(row, i))

        # Проверяем вертикальные совпадения
        for col in range(self.size):
            count = 1
            current_element = self.grid[0][col]
            for row in range(1, self.size):
                if self.grid[row][col].matches(current_element):
                    count += 1
                else:
                    if count >= 3:
                        for i in range(row - count, row):
                            matches.add(Position(i, col))
                    count = 1
                    current_element = self.grid[row][col]

            if count >= 3:
                for i in range(self.size - count, self.size):
                    matches.add(Position(i, col))

        return matches

    def remove_matches(self, matches: set):
        """Удаляет совпавшие элементы с поля"""
        for position in matches:
            self.set_element(position, None)

    def drop_elements(self):
        """Опускает элементы вниз после удаления совпадений"""
        for col in range(self.size):
            # Собираем все непустые элементы в колонке
            elements = []
            for row in range(self.size - 1, -1, -1):
                element = self.grid[row][col]
                if element is not None:
                    elements.append(element)

            # Заполняем колонку снизу вверх
            for row in range(self.size - 1, -1, -1):
                if len(elements) > 0:
                    self.grid[row][col] = elements.pop(0)
                else:
                    self.grid[row][col] = Element()  # Новый случайный элемент

    def display(self):
        """Отображает текущее состояние поля"""
        print("\n  ", end="")
        for col in range(self.size):
            print(f" {col} ", end="")
        print()

        for row in range(self.size):
            print(f"{row} |", end="")
            for col in range(self.size):
                print(f" {self.grid[row][col]} ", end="")
            print("|")
        print()


class ScoreKeeper:
    """Отслеживает очки и статистику игры"""

    def __init__(self):
        self.score = 0
        self.moves = 0
        self.matches_history = []

    def add_match_score(self, match_count: int):
        """Добавляет очки за совпадение"""
        if match_count == 3:
            points = 30
        elif match_count == 4:
            points = 60
        elif match_count >= 5:
            points = 100
        else:
            points = 10 * match_count

        self.score += points
        self.matches_history.append((match_count, points))

    def add_move(self):
        """Увеличивает счетчик ходов"""
        self.moves += 1

    def get_statistics(self):
        """Возвращает статистику игры"""
        return {
            'score': self.score,
            'moves': self.moves,
            'matches': len(self.matches_history)
        }


class InputHandler:
    """Обрабатывает пользовательский ввод"""

    @staticmethod
    def parse_move(input_str: str):
        """Парсит ввод пользователя для хода"""
        # Ожидаем формат "1,2 1,3" или "A1 A2"
        pattern = r'(\d+)[,\s]*(\d+)\s+(\d+)[,\s]*(\d+)'
        match = re.match(pattern, input_str.strip())

        if match:
            row1, col1, row2, col2 = map(int, match.groups())
            pos1 = Position(row1, col1)
            pos2 = Position(row2, col2)
            return pos1, pos2

        return None, None

    @staticmethod
    def is_adjacent(pos1: Position, pos2: Position):
        """Проверяет, являются ли позиции соседними"""
        row_diff = abs(pos1.row - pos2.row)
        col_diff = abs(pos1.col - pos2.col)
        return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)


class GameEngine:
    """Основной движок игры"""

    def __init__(self):
        self.grid = GameGrid()
        self.score_keeper = ScoreKeeper()
        self.input_handler = InputHandler()
        self.game_over = False

    def process_turn(self, pos1: Position, pos2: Position):
        """Обрабатывает один ход игрока"""
        if not self.input_handler.is_adjacent(pos1, pos2):
            return False, "Позиции должны быть соседними!"

        # Пробуем поменять местами
        if not self.grid.swap_elements(pos1, pos2):
            return False, "Некорректные позиции!"

        # Проверяем, есть ли совпадения после обмена
        matches = self.grid.find_matches()
        if not matches:
            # Возвращаем элементы обратно, если нет совпадений
            self.grid.swap_elements(pos1, pos2)
            return False, "Ход не создает совпадений!"

        self.score_keeper.add_move()
        self._process_matches()
        return True, "Ход выполнен успешно!"

    def _process_matches(self):
        """Обрабатывает все совпадения и их последствия"""
        total_removed = 0

        while True:
            matches = self.grid.find_matches()
            if not matches:
                break

            # Подсчитываем очки
            match_groups = self._group_matches(matches)
            for group in match_groups:
                self.score_keeper.add_match_score(len(group))

            total_removed += len(matches)
            self.grid.remove_matches(matches)
            self.grid.drop_elements()

        if total_removed > 0:
            print(f"Удалено элементов: {total_removed}")

    def _group_matches(self, matches: set):
        """Группирует совпадения по связанным областям"""
        # Простая реализация - каждое совпадение как отдельная группа
        # В более сложной версии можно группировать связанные области
        return [[match] for match in matches]

    def display_game_state(self):
        """Отображает текущее состояние игры"""
        self.grid.display()
        stats = self.score_keeper.get_statistics()
        print(f"Очки: {stats['score']} | Ходы: {stats['moves']} | Совпадений: {stats['matches']}")

    def check_possible_moves(self):
        """Проверяет, есть ли возможные ходы"""
        for row in range(self.grid.size):
            for col in range(self.grid.size):
                pos1 = Position(row, col)
                for adjacent in pos1.get_adjacent():
                    if adjacent.is_valid(self.grid.size):
                        # Пробуем обмен
                        self.grid.swap_elements(pos1, adjacent)
                        matches = self.grid.find_matches()
                        # Возвращаем обратно
                        self.grid.swap_elements(pos1, adjacent)

                        if matches:
                            return True
        return False


class Game:
    """Главный класс игры"""

    def __init__(self):
        self.engine = GameEngine()

    def run(self):
        """Запускает главный цикл игры"""
        print("=== ИГРА ТРИ-В-РЯД ===")
        print("Формат ввода: 'row1,col1 row2,col2' (например: '2,3 2,4')")
        print("Команды: 'quit' - выход, 'restart' - перезапуск")

        while not self.engine.game_over:
            print("\n" + "=" * 40)
            self.engine.display_game_state()

            if not self.engine.check_possible_moves():
                print("\nНет доступных ходов! Игра окончена.")
                break

            user_input = input("\nВведите ход: ").strip().lower()

            if user_input == 'quit':
                break
            elif user_input == 'restart':
                self.engine = GameEngine()
                print("Игра перезапущена!")
                continue

            pos1, pos2 = self.engine.input_handler.parse_move(user_input)
            if pos1 is None or pos2 is None:
                print("Некорректный формат ввода!")
                continue

            success, message = self.engine.process_turn(pos1, pos2)
            print(message)

            if success:
                # Показываем результат после обработки совпадений
                print("\nСостояние после хода:")
                self.engine.display_game_state()

        # Финальная статистика
        self._show_final_stats()

    def _show_final_stats(self):
        """Показывает финальную статистику"""
        print("\n" + "=" * 40)
        print("ИГРА ЗАВЕРШЕНА!")
        stats = self.engine.score_keeper.get_statistics()
        print(f"Итоговые очки: {stats['score']}")
        print(f"Сделано ходов: {stats['moves']}")
        print(f"Найдено совпадений: {stats['matches']}")

        if stats['moves'] > 0:
            avg_score = stats['score'] // stats['moves']
            print(f"Средние очки за ход: {avg_score}")


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()