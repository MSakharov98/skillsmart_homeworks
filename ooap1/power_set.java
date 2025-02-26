public abstract class AbstractPowerSet<T> extends AbstractHashTable<T>{
    // ** конструктор **
    // постусловие: создано пустое множество с максимальным количеством элементов size
    protected AbstractPowerSet(int size){}

    // ** запросы **
    // возвращает пересечение текущего множества с множеством other
    public abstract AbstractPowerSet<T> intersection(AbstractPowerSet<T> other);

    // возвращает объединение текущего множества и множества other
    public abstract AbstractPowerSet<T> union(AbstractPowerSet<T> other);

    // возвращает разницу между текущим множеством и множеством other
    public abstract AbstractPowerSet<T> difference(AbstractPowerSet<T> other);

    // проверка, является ли other подмножеством текущего множества
    public abstract boolean isSubset(AbstractPowerSet<T> other);
}

class PowerSet<T> extends HashTable<T> {
    PowerSet(int size){
        super(size);
    }

    public PowerSet<T> intersection(PowerSet<T> other) {
        PowerSet<T> newSet = new PowerSet<>(this.capacity);
        for (T slot : this.slots) {
            if (slot != null && other.contains(slot))
                newSet.put(slot);
        }
        return newSet;
    }

    public PowerSet<T> union(PowerSet<T> other) {
        PowerSet<T> newSet = new PowerSet<>(this.capacity + other.capacity);
        for (T slot : this.slots) {
            if (slot != null && !other.contains(slot))
                newSet.put(slot);
        }
        for (T slot : other.slots) {
            if (slot != null && !this.contains(slot))
                newSet.put(slot);
        }
        return newSet;
    }

    public PowerSet<T> difference(PowerSet<T> other){
        PowerSet<T> newSet = new PowerSet<>(this.capacity);
        for (T slot : this.slots) {
            if (slot != null && !other.contains(slot))
                newSet.put(slot);
        }
        return newSet;
    }

    public boolean isSubset(PowerSet<T> other) {
        for (T slot : other.slots)
            if (slot != null && !this.contains(slot))
                return false;
        return true;
    }
}