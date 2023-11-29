'''
Задание № 7

Для некоторых пунктов домашнего задания смоделированы ситуации в силу отсутствия
столь большого количества написанного ранее кода, подходящего для примеров.

7.1. Примеры правильного именования булевых переменных:

- Было: `flag`, Стало: `is_valid`.
- Было: `status`, Стало: `has_error`.
- Было: `result`, Стало: `operation_successful`.
- Было: `enable`, Стало: `is_enabled`.
- Было: `check`, Стало: `needs_verification`.

7.2. Случаи использования булевых переменных:

- Проверка условий: `is_validated`, `has_permission`, `is_authenticated`.
- Управление функциональностью: `enable_logging`, `show_notification`.
- Обработка ошибок: `has_error`, `is_critical_error'.

7.3. Правильное именование индексов циклов:

Вместо `i`, `j`, `k` можно использовать более выразительные имена, например:

for index_customer, customer in enumerate(customers):
    pass

for step_number, step in enumerate(steps):
    pass

7.4. Пары имен-антонимов:

- Было: `start`, `end`, Стало: `beginning`, `completion`
- Было: `open`, `close`, Стало: `unlock`, `lock`

7.5. Выразительные имена для временных переменных:

- Было: `temp`, Стало: `temporary_data`
- Было: `x`, `y`, Стало: `coordinate_x`, `coordinate_y`
- Было: `result`, Стало: `calculation_result`

'''