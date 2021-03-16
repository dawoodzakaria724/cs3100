
class SLDictionary:
    def __init__(self, arr):
        # sorts array, initializes dictionary, initializes _size
        arr.sort()
        self._dict_list = arr
        self._size = len(arr)
        self.head = None
        self.tail = None

    def __len__(self):
        # returns the size, so init must be completed
        return self._size

    # Dawood
    def __contains__(self, key):

        # same as assign 4, but _find must be figured out

        return not self._find(key) is None

    def _find(self, key):  # uses a for loop to search for a given key, returns that key if found
        randStr = ""
        for x in self._dict_list:
            if x[0] == key:
                return randStr + " " + str(x[0]) + " " + str(x[1])
            else:
                return -1

    def __getitem__(self, key):  # this works!

        # calls _find, confirms if a certain key exists.

        index = self._find(key)

        if index is None:
            raise KeyError("Item does not exist in list")
        else:
            return index

    def __setitem__(self, key, value):  # this works!
        self._insert(key, value)
        self._size += 1

    def _insert(self, key, value):  # this works!

        testBool = False

        for x in self._dict_list:
            if x[0] == key:
                x[1] = value
                testBool = True
                break

        if not testBool:
            self._dict_list.append([key, value])
            self._dict_list.sort()

    def pop(self, key):  # this works!
        for x in self._dict_list:
            if x[0] == key:
                # print("Popdebug")
                self._dict_list.remove(x)

    def __str__(self):  # print_dict
        testStr = ""
        for x in self._dict_list:
            # print(x)
            testStr = testStr + " " + str(x[0]) + " " + str(x[1])
        return testStr


# old version of str, new version is print_dict

# def __str__(self):

# return str(self.key) + ": " + str(self.data)


def main():
    # array initialized
    arr = []

    dict = SLDictionary(arr)
    # array initialized with 1000 entries
    for i in range(1, 1000):
        dict[i] = "Tom"

    # assigning key and value to results
    results = dict[1]

    # testing print function
    print(results)

    # testing __str__ function
    print(dict)

    # testing _insert function
    dict[1] = "Test"

    results = dict[1]

    print(results)

    print(dict)

    # testing pop function
    dict.pop(1)

    print(dict)

    dict[7] = "Last"

    print(dict)

    # testing the __contains__ function
    if "Tom" in dict:
        print("yes")
    else:
        print("no")

    # testing __len__ function
    print(len(dict))


if __name__ == "__main__":
    main()
