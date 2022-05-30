from LinkenListsStacksDict import LinkedList

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dictionary:   
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets
        
    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
        if not found_key:
            self.buckets[index].append(Entry(key, value))
            self.length += 1


    def get_value(self, key):
        index = self._get_index(key)
        for entry in self.buckets[index]:
            if entry.key == key:
                return entry.value
        raise KeyError(key)
    
    def delete(self, key):
        index = self._get_index(key)
        new_bucket = LinkedList()
        for entry in self.buckets[index]:
            if entry.key != key:
                new_bucket.append(entry)
        if len(new_bucket) < len(self.buckets[index]):
            self.length -= 1
        self.buckets[index] = new_bucket

    def __getitem__(self, key):
        return self.get_value(key)
    def __setitem__(self, key, value):
        return self.put(key, value)
    def __len__(self):
        return self.length

    