import java.util.ArrayList;
import java.util.List;

abstract class MyQueue<T> {
    // ** конструктор **
    // постусловие: создана пустая очередь
    protected MyQueue(){
    }

    // ** команды **
    // постусловие: добавлен новый элемент в хвост очереди
    abstract public void enqueue(T value);

    // предусловие: очередь не пуста;
    // постусловие: удалён элемент из головы очереди
    abstract public void dequeue();

    // ** запросы **
    // предусловие: очередь не пуста
    abstract public T get(); // получить элемент из головы очереди

    abstract public int size(); // текущий размер очереди

    // запросы статусов
    abstract public int get_dequeue_status(); // успешно; очередь пуста
    abstract public int get_get_status(); // успешно; очередь пуста
}

class MyQueueImpl<T> extends MyQueue<T> {
    private List<T> queue;
    private int size;
    private final int DEQUEUE_STATUS_NIL = 0; // удаление элемента ещё не вызывалось
    private final int DEQUEUE_STATUS_OK = 1; // удаление элемента прошло успешно
    private final int DEQUEUE_STATUS_ERR = 2; // очередь пустая
    private final int GET_STATUS_NIL = 0; // запрос элемента из головы ещё не вызывался
    private final int GET_STATUS_OK = 1; //  зарпос из головы прошёл успешно
    private final int GET_STATUS_ERR = 2; // очередь пустая

    private int dequeue_status;
    private int get_status;

    public MyQueueImpl(){
        super();
        queue = new ArrayList<>();
        size = 0;
        dequeue_status = DEQUEUE_STATUS_NIL;
        get_status = GET_STATUS_NIL;
    }

    @Override
    public void enqueue(T value) {
        queue.add(value);
        size++;
    }

    @Override
    public void dequeue() {
        if (queue.isEmpty()) {
            dequeue_status = DEQUEUE_STATUS_ERR;
            return;
        }
        dequeue_status = DEQUEUE_STATUS_OK;
        queue.remove(0);
        size--;
    }

    @Override
    public T get() {
        if (queue.isEmpty()) {
            get_status = GET_STATUS_ERR;
            return null;
        }
        get_status = GET_STATUS_OK;
        return queue.get(0);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public int get_dequeue_status() {
        return dequeue_status;
    }

    @Override
    public int get_get_status() {
        return get_status;
    }
}