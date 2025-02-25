public abstract class LinkedList<T> {

    // ** статусы **
    private final int HEAD_NIL = 0; // head() ещё не вызывалась
    private final int HEAD_OK = 1; // последняя head() отработала нормально
    private final int HEAD_ERR = 2; // связанный список пустой

    private final int TAIL_NIL = 0; // tail() ещё не вызывалась
    private final int TAIL_OK = 1; // последняя tail() отработала нормально
    private final int TAIL_ERR = 2; // связанный список пустой

    private final int RIGHT_NIL = 0; // right() ещё не вызывалась
    private final int RIGHT_OK = 1; // последняя right() отработала нормально
    private final int RIGHT_ERR = 2; // связанный список пустой

    private final int PUT_RIGHT_NIL = 0; // put_right() ещё не вызывалась
    private final int PUT_RIGHT_OK = 1; // последняя put_right() отработала нормально
    private final int PUT_RIGHT_ERR = 2; // связанный список пустой

    private final int PUT_LEFT_NIL = 0; // put_left() ещё не вызывалась
    private final int PUT_LEFT_OK = 1; // последняя put_left() отработала нормально
    private final int PUT_LEFT_ERR = 2; // связанный список пустой

    private final int REMOVE_NIL = 0; // remove() ещё не вызывалась
    private final int REMOVE_OK = 1; // последняя remove() отработала нормально
    private final int REMOVE_ERR = 2; // связанный список пустой

    private final int REPLACE_NIL = 0; // replace() ещё не вызывалась
    private final int REPLACE_OK = 1; // последняя replace() отработала нормально
    private final int REPLACE_ERR = 2; // связанный список пустой

    private final int FIND_NIL = 0; // find() ещё не вызывалась
    private final int FIND_OK = 1; // последняя find() отработала нормально
    private final int FIND_ERR = 2; // связанный список пустой

    private final int REMOVE_ALL_NIL = 0; // remove_all() ещё не вызывалась
    private final int REMOVE_ALL_OK = 1; // последняя remove_all() отработала нормально
    private final int REMOVE_ALL_ERR = 2; // связанный список пустой

    private final int GET_NIL = 0; // get() ещё не вызывалась
    private final int GET_OK = 1; // последняя get() отработала нормально
    private final int GET_ERR = 2; // связанный список пустой

    // ** конструктор **
    // постусловие: создан новый пустой список
    protected LinkedList(){
    }

    // ** команды **
    // предусловие: список не пустой
    // постусловие: курсор находится на первом узле списка
    abstract void head();

    // предусловие: список не пустой
    // постусловие: курсор находится на последнем узле списка
    abstract void tail();

    // предусловие: у курсора есть элемент
    // постусловие: курсор перемещён на один узел вправо
    abstract void right();

    // предусловие: список не пустой
    // постусловие: за текущим узлом добавлен новый узел с заданным значением
    abstract void put_right(T value);

    // предусловие: список не пустой
    // постусловие: перед текущим узлом добавлен новый узел с заданным значением
    abstract void put_left(T value);

    // предусловие: список не пустой
    /* постусловие: текущий узел удалён, курсор смещён к правому соседнему узлу, если он есть,
       если нет, то курсор смещён к левому соседнему узлу, если он есть */
    abstract void remove();

    // постусловие: список очищен от всех узлов
    abstract void clear();

    // постусловие: новый узел добавлен в хвост списка
    abstract void add_tail(T value);

    // постусловие: из списка удалены все узлы с заданным значением
    abstract void remove_all(T value);

    // предусловие: список не пустой
    // постусловие: значение текущего узла заменено на новое
    abstract void replace(T value);

    // постусловие: курсор находится на узле с требуемым значением, если такой узел был найден
    abstract void find(T value);

    // ** запросы **
    // предусловие: список не пустой
    abstract T get();
    abstract int size();
    abstract boolean is_head();
    abstract boolean is_tail();
    abstract boolean is_value();

    // ** дополнительные запросы **
    abstract int get_head_status(); // возвращает значение HEAD_*
    abstract int get_tail_status(); // возвращает значение TAIL_*
    abstract int get_right_status(); // возвращает значение RIGHT_*
    abstract int get_put_right_status(); // возвращает значение PUT_RIGHT_*
    abstract int get_put_left_status(); // возвращает значение PUT_LEFT_*
    abstract int get_remove_status(); // возвращает значение REMOVE_*
    abstract int get_replace_status(); // возвращает значение REPLACE_*
    abstract int get_find_status(); // возвращает значение FIND_*
    abstract int get_remove_all_status(); // возвращает значение REMOVE_ALL_*
    abstract int get_get_status(); // возвращает значение GET_*
}

/*
2.2. Почему операция tail не сводима к другим операциям (если исходить из эффективной реализации)?
- поскольку эффективная реализация такой структуры должна предпологать хранение "указателей" на первый и последний элементы,
это в свою очередь позволит операции tail выполняться сразу за О(1) не прибегая к другим операциям.

2.3. Операция поиска всех узлов с заданным значением, выдающая список таких узлов, уже не нужна. Почему?
- у нас теперь операция find, которая позволит последовательно получить все искомые элементы.
 */