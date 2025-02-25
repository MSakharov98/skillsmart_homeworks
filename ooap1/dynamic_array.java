import java.lang.reflect.Array;
import java.util.Arrays;

abstract class DynArray<T> {

    // ** конструктор **
    // постусловие: создан пустой массив
    protected DynArray(Class clz){

    }

    // ** команды **
    // предусловие: индекс находится в допустимых границах
    // постусловие: значение элемента под индексом i изменено
    public abstract void insert(int index, T value);

    // постусловие: в хвост массива добавлен новый элемент
    public abstract void append(T value);

    // предусловие: индекс находится в допустимых границах
    // постусловие: элемент под индексом i удалён
    public abstract void remove(int i);

    // ** запросы **
    // предусловие: индекс находится в допустимых границах
    public abstract  T get(int i); // значение элемента под индексом i
    public abstract  int size(); // текущий размер массива

    // ** запросы статусов **
    public abstract  int get_insert_status();
    public abstract  int get_remove_status();
    public abstract  int get_get_status();
}

class DynamicArrayImpl<T> extends DynArray<T> {
    private T[] array;
    private int count;
    private int capacity;
    private final Class<T> clazz;
    private final int INSERT_STATUS_NIL = 0;
    private final int INSERT_STATUS_OK = 1;
    private final int INSERT_STATUS_ERR = 2;
    private final int REMOVE_STATUS_NIL = 0;
    private final int REMOVE_STATUS_OK = 1;
    private final int REMOVE_STATUS_ERR = 2;
    private final int GET_STATUS_NIL = 0;
    private final int GET_STATUS_OK = 1;
    private final int GET_STATUS_ERR = 2;
    private int insert_status = INSERT_STATUS_NIL;
    private int remove_status = REMOVE_STATUS_NIL;
    private int get_status = GET_STATUS_NIL;

    private void makeArray(int capacity) {
        if (array != null)
            array = Arrays.copyOf(array, capacity);
        else
            array = (T[]) Array.newInstance(clazz, capacity);
        this.capacity = capacity;
    }

    public DynamicArrayImpl(Class clazz) {
        super(clazz);
        this.clazz = clazz;
        this.count = 0;
        makeArray(16);
    }

    @Override
    public void insert(int index, T value) {
        if (index < 0 || index > count) {
            insert_status = INSERT_STATUS_ERR;
            return;
        }
        if (count >= capacity) {
            makeArray(capacity * 2);
        }
        for (int i = count; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = value;
        count++;
        insert_status = INSERT_STATUS_OK;
    }

    @Override
    public void append(T value) {
        if (count == capacity)
            makeArray(capacity * 2);
        array[count] = value;
        count++;
    }

    @Override
    public void remove(int index) {
        if (index < 0 || index >= count) {
            remove_status = REMOVE_STATUS_ERR;
            return;
        }
        for (int i = index; i < this.count; i++) {
            array[i] = array[i + 1];
        }
        count--;
        remove_status = REMOVE_STATUS_OK;
        int odd = capacity % 2;
        int limit = capacity / 2 - 1;
        if (odd != 0)
            limit = capacity / 2;
        if (count == limit && (int) (capacity / 1.5) <= 16)
            makeArray(16);
        else
            makeArray((int) (capacity / 1.5));
    }

    @Override
    public T get(int index) {
        if (index < 0 || index >= count) {
            get_status = GET_STATUS_ERR;
            return null;
        }
        get_status = GET_STATUS_OK;
        return array[index];
    }

    @Override
    public int size() {
        return count;
    }

    @Override
    public int get_insert_status() {
        return insert_status;
    }

    @Override
    public int get_remove_status() {
        return remove_status;
    }

    @Override
    public int get_get_status() {
        return get_status;
    }
}