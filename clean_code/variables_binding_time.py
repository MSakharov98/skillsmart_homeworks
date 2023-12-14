'''

1. во время написания кода:
threadCount = 2

// простой параметр, который не меняется, поэтому не вынесен
// в параметр конфигурации или файл настроек.

2. во время компиляции кода
DEFAULT_THREAD_COUNT = 2
...
processThreadCount = DEFAULT_THREAD_COUNT
// повышение читабильности и гибкости программы
// на другом железе легко изменить работу программы

3. во время выполнения программы
processThreadCount = getThreadCount()

// позднее связывание, настройки вынесены в отдельный файл
// который может генерировать из операционной системы

'''