'''
Задание 4

Исправление имен констант с указанием контекста.

keyCode -> ARROW_UP
// конкретное название клавиши

url -> SITE_URL
// формат и подробное описание

textColor -> TEXT_COLOR
// формат

DOMAIN -> DOMAIN_FOR_DOWNLOADS
// подробное описание

app_root -> APP_ROOT_PATH
// формат и подробное описание

int[10][10] -> int[MATRIX_ROWS][MATRIX_COLUMNS]
// убираем магические числа

status = "ok" -> status = STATUS_MESSAGE_OK
// убираем магические числа

3.14 * R ** 2 -> MATH_PI * R ** 2
// убираем магические числа

for (int i = 0; i < 7; i++) -> for (int i = 0; i < DAYS_IN_WEEK; i++)
// параметризуем программу

if (i < 1024) -> if (i < FILE_SIZE_UPLOAD)
// параметризуем программу

if ("debug") -> if (DEBUG)
// параметризуем программу

SECONDS_PER_DAY = 86400
// параметризуем программу

'''