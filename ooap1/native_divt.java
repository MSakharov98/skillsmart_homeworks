package OOAP1;

import java.lang.reflect.Array;
import java.util.Optional;

public abstract class AbstractNativeDictionary<T> {
    // ** конструктор **
    // постусловие: создан пустой словарь
    protected AbstractNativeDictionary() {
    }

    // ** команды **
    // предусловие: в словаре есть слот с ключём или слот пустой
    // постусловие: в словаре добавлено новое значение
    public abstract void put(String key, T value);

    // предусловие: в словаре имеется слот с ключём
    // постусловие: из словаря удалено значение по ключу
    public abstract void remove(String key);

    // предусловие: в словаре имеется слот с ключём
    // постусловие: из словаря читается значение value по ключу
    public abstract Optional<T> get(String key);

    // ** запросы **
    public abstract boolean contains(String key); // содержится ли ключ в словаре
    public abstract int size(); // количество элементов в словаре

    // ** запросы статусов **
    public abstract int get_put_status();
    public abstract int get_remove_status();
    public abstract int get_get_status();
}

class NativeDictionary<T> extends AbstractNativeDictionary<T> {
    private int size = 0;
    private int capacity;
    private String[] keys;
    private T[] values;
    private Class<T> clazz;

    private final int PUT_STATUS_NIL = 0; // команда put ещё не вызывалась
    private final int PUT_STATUS_OK = 1; // вставка элемента прошла успешно
    private final int PUT_STATUS_ERR = 2; // лимит коллизий исчерпан
    private final int REMOVE_STATUS_NIL = 0; // команда remove ещё не вызывалась
    private final int REMOVE_STATUS_OK = 1; // удаление элемента прошло успешно
    private final int REMOVE_STATUS_ERR = 2; // нет такого ключа в словаре
    private final int GET_STATUS_NIL = 0; // команда get ещё не вызывалась
    private final int GET_STATUS_OK = 1; // получение значение элемента прошло успешно
    private final int GET_STATUS_ERR = 2; // искомый ключ отсутсвует в словаре

    private int put_status;
    private int remove_status;
    private int get_status;

    public NativeDictionary(int capacity){
        this.capacity = capacity;
        keys = new String[capacity];
        values = (T[]) Array.newInstance(clazz, capacity);
        put_status = PUT_STATUS_NIL;
        remove_status = REMOVE_STATUS_NIL;
        get_status = GET_STATUS_NIL;
    }

    @Override
    public void put(String key, T value) {
        int index = index(key);
        if (!keys[index].equals(key)) {
            put_status = PUT_STATUS_ERR;
        } else {
            put_status = PUT_STATUS_OK;
            values[index] = value;
            size++;
        }
    }

    @Override
    public void remove(String key) {
        int index = index(key);
        if (!keys[index].equals(key)) {
            remove_status = REMOVE_STATUS_ERR;
        } else {
            remove_status = REMOVE_STATUS_OK;
            keys[index] = null;
            values[index] = null;
            size--;
        }
    }

    @Override
    public Optional<T> get(String key) {
        int index = index(key);
        if (!keys[index].equals(key)) {
            get_status = GET_STATUS_ERR;
            return Optional.empty();
        }
        get_status = GET_STATUS_OK;
        return Optional.of(values[index]);
    }

    @Override
    public boolean contains(String key) {
        int index = index(key);
        return keys[index].equals(key);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public int get_put_status() {
        return put_status;
    }

    @Override
    public int get_remove_status() {
        return remove_status;
    }

    @Override
    public int get_get_status() {
        return get_status;
    }

    private int index(String key) {
        int asNumber = key.chars().sum();
        return asNumber % capacity;
    }
}