import java.util.ArrayList;
import java.util.List;

abstract class ParentQueue<T> {
    // ** конструктор **
    // постусловие: создана пустая очередь
    protected ParentQueue(){
    }

    // ** команды **
    // постусловие: добавлен новый элемент в хвост очереди
    abstract public void add_tail(T value);

    // предусловие: очередь не пуста;
    // постусловие: удалён элемент из головы очереди
    abstract public void remove_front();

    // ** запросы **
    // предусловие: очередь не пуста
    abstract public T get_front(); // получить элемент из головы очереди

    abstract public int size(); // текущий размер очереди

    // запросы статусов
    abstract public int get_remove_front_status(); // успешно, очередь пуста
    abstract public int get_get_front_status(); // успешно, очередь пуста
}

abstract class AbstractQueue<T> extends ParentQueue<T> {
    // ** конструктор **
    // постусловие: создана пустая очередь
    protected AbstractQueue(){
        super();
    }
}

abstract class AbstractDequeue<T> extends ParentQueue<T> {
    // ** конструктор **
    // постусловие: создана пустая очередь
    protected AbstractDequeue(){
        super();
    }

    // ** команды **
    // постусловие: в голову очереди добавлен новый элемент
    abstract public void add_front(T value);

    // предусловие: очередь не пуста
    // постусловие: из хвоста очереди удалён элемент
    abstract public void remove_tail();

    // запросы
    // предусловие: список не пуст
    abstract public T get_tail(); // значение элемента в хвосте очереди

    // запросы статусов (возможные значения статусов)
    abstract public int get_remove_tail_status(); // успешно; очередь пуста
    abstract public int get_get_tail_status(); // успешно; очередь пуста
}

class ParentQueueImpl<T> extends ParentQueue<T> {
    private List<T> queue;
    private int size;
    private final int REMOVE_FRONT_STATUS_NIL = 0; // удаление элемента ещё не вызывалось
    private final int REMOVE_FRONT_STATUS_OK = 1; // удаление элемента прошло успешно
    private final int REMOVE_FRONT_STATUS_ERR = 2; // очередь пустая
    private final int GET_FRONT_STATUS_NIL = 0; // запрос элемента из головы ещё не вызывался
    private final int GET_FRONT_STATUS_OK = 1; //  зарпос из головы прошёл успешно
    private final int GET_FRONT_STATUS_ERR = 2; // очередь пустая

    private int remove_front_status;
    private int get_front_status;

    public ParentQueueImpl(){
        super();
        queue = new ArrayList<>();
        size = 0;
        remove_front_status = REMOVE_FRONT_STATUS_NIL;
        get_front_status = GET_FRONT_STATUS_NIL;
    }

    @Override
    public void add_tail(T value) {
        queue.add(value);
        size++;
    }

    @Override
    public void remove_front() {
        if (queue.isEmpty()) {
            remove_front_status = REMOVE_FRONT_STATUS_ERR;
            return;
        }
        remove_front_status = REMOVE_FRONT_STATUS_OK;
        queue.remove(0);
        size--;
    }

    @Override
    public T get_front() {
        if (queue.isEmpty()) {
            get_front_status = GET_FRONT_STATUS_ERR;
            return null;
        }
        get_front_status = GET_FRONT_STATUS_OK;
        return queue.get(0);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public int get_remove_front_status() {
        return remove_front_status;
    }

    @Override
    public int get_get_front_status() {
        return get_front_status;
    }
}

class QueueImpl<T> extends ParentQueueImpl<T> {
    public QueueImpl(){
        super();
    }
}

class DequeueImpl<T> extends ParentQueueImpl<T> {
    private List<T> dequeue;
    private int size;

    private final int REMOVE_TAIL_STATUS_NIL = 0; // удаление элемента из хвоста ещё не вызывалось
    private final int REMOVE_TAIL_STATUS_OK = 1; // удаление элемента из хвоста прошло успешно
    private final int REMOVE_TAIL_STATUS_ERR = 2; // очередь пустая
    private final int GET_TAIL_STATUS_NIL = 0; // запрос элемента из хвоста ещё не вызывался
    private final int GET_TAIL_STATUS_OK = 1; //  зарпос из хвоста прошёл успешно
    private final int GET_TAIL_STATUS_ERR = 2; // очередь пустая

    public DequeueImpl(){
        super();
        dequeue = new ArrayList<>();
        size = 0;
        remove_tail_status = REMOVE_TAIL_STATUS_NIL;
        get_tail_status = GET_TAIL_STATUS_NIL;
    }

    private int remove_tail_status;
    private int get_tail_status;

    public void add_front(T value) {
        dequeue.add(0, value);
        size++;
    }

    public void remove_tail() {
        if (dequeue.isEmpty()) {
            remove_tail_status = REMOVE_TAIL_STATUS_ERR;
            return;
        }
        dequeue.remove(size - 1);
        size--;
        remove_tail_status = REMOVE_TAIL_STATUS_OK;
    }

    public T get_tail() {
        if (dequeue.isEmpty()) {
            get_tail_status = GET_TAIL_STATUS_ERR;
            return null;
        }
        get_tail_status = GET_TAIL_STATUS_OK;
        return dequeue.get(size - 1);
    }

    public int get_remove_tail_status() {
        return remove_tail_status;
    }

    public int get_get_tail_status() {
        return get_tail_status;
    }
}