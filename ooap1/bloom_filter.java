public abstract class AbstractBloomFilter<T> {
    // ** конструктор
    // постусловие: создан пустой фильтр Блюма заданного размера
    protected AbstractBloomFilter (int size) {
    }

    protected AbstractBloomFilter(){

    }

    // ** команды **
    // постусловие: в фильтр добавлено новое значение
    public abstract void put(T value);

    // ** запросы **
    // есть ли значение в фильтре (возможны ложноположительные срабатывания)
    public abstract boolean is_value(T value);
}

class BloomFilter<T> extends AbstractBloomFilter<T> {
    private int bitArray = 0;
    private int size = 32;

    public int firstHashFunction(T value) {
        String string = value.toString();
        int result = 0;
        for(int i = 0; i < string.length(); i++) {
            int code = string.charAt(i);
            result = (result * 17 + code) % size;
        }
        return result;
    }
    public int secondHashFunction(T value) {
        String string = value.toString();
        int result = 0;
        for(int i = 0; i < string.length(); i++) {
            int code = string.charAt(i);
            result = (result * 223 + code) % size;
        }
        return result;
    }

    @Override
    public void put(T value) {
        int firstIndex = firstHashFunction(value);
        int secondIndex = secondHashFunction(value);
        bitArray |= (int) Math.pow(2, firstIndex);
        bitArray |= (int) Math.pow(2, secondIndex);
    }

    @Override
    public boolean is_value(T value) {
        int firstIndex = firstHashFunction(value);
        int secondIndex = secondHashFunction(value);
        int firstMask = (int) Math.pow(2, firstIndex);
        int secondMask = (int) Math.pow(2, secondIndex);
        return (bitArray & firstMask) != 0 && (bitArray & secondMask) != 0;
    }

    public BloomFilter(int size){
        this.size = size;
        new BloomFilter<T>();
    }

    public BloomFilter() {

    }
}