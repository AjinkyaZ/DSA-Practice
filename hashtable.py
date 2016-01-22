class hashtable:

    def __init__(self):
        self.size = 100
        self.items = [None]*self.size
        self.data = [None]*self.size

    def insert(self, key, data):
        hashval = self.hashfunction(key, len(self.items))

        if self.items[hashval] == None:
            self.items[hashval] = key
            self.data[hashval] = data
        else:
            if self.items[hashval] == key:
                self.data[hashval] = data  # replace
            else:
                pos_next = self.rehash(hashval, len(self.items))
                while self.items[pos_next] != None and \
                        self.items[pos_next] != key:
                    pos_next = self.rehash(pos_next, len(self.items))

                if self.items[pos_next] == None:
                    self.items[pos_next] = key
                    self.data[pos_next] = data
                else:
                    self.data[pos_next] = data  # replace

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        pos_start = self.hashfunction(key, len(self.items))
        data = None
        stop = False
        found = False
        position = pos_start
        while self.items[position] != None and  \
                not found and not stop:
            if self.items[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.items))
                if position == pos_start:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.insert(key, data)
