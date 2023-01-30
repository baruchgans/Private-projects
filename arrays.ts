function reverse(str) {
    let reversedStr = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversedStr += str[i];
    }
    return reversedStr;
}


let str1 = "Hi, my name is Bob";
console.log(reverse(str1));


function mergeSortedArrays(numbers1, numbers2) {
    let numbers1Pointer = 0;
    let numbers2Pointer = 0;
    let mergedArr = []
    while (numbers1Pointer < numbers1.length || numbers2Pointer < numbers2.length) {
        if (numbers1Pointer == numbers1.length) {
            mergedArr.concat(numbers2.slice(numbers2Pointer, numbers2.length - 1));
            break
        } else if (numbers2Pointer == numbers2.length) {
            mergedArr.concat(numbers1.slice(numbers1Pointer, numbers1.length - 1))
            break
        } else {
            if (numbers1[numbers1Pointer] < numbers2[numbers2Pointer]) {
                mergedArr.push(numbers1[numbers1Pointer]);
                numbers1Pointer++
            } else {
                mergedArr.push(numbers2[numbers2Pointer]);
                numbers2Pointer++
            }
        }
    }
    return mergedArr
}

mergeSortedArrays([0, 3, 4, 31], [3, 4, 6, 30]);

class MyNode {
    val: any;
    next: any;

    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    head: MyNode;

    constructor(head: MyNode = null) {
        this.head = head;
    }

    getLastNode() {
        let curr = this.head;
        while (curr.next) {
            curr = curr.next;
        }
        return curr;
    }
}

class HashTable {
    data: any[];

    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    get(key) {
        const idx = this._hash(key);
        let curr = this.data[idx];
        while (curr && curr.val) {
            if (curr.val[0] == key) {
                console.log(curr.val[1]);
                return;
            }
            curr = curr.next;
        }
        console.log('not found');
    }

    set(key, val) {
        const idx = this._hash(key);
        if (!this.data[idx]) {
            this.data[idx] = new MyNode([key, val]);
        } else {
            let curr = this.data[idx];
            while (curr.next) {
                if (curr.val[0] == key) {
                    curr.val[1] = val;
                    return;
                }
            }
            if (curr.val[0] == key) {
                curr.val[1] = val;
                return;
            }
            curr.next = new MyNode([key, val]);
        }
    }
}

const myHashTable = new HashTable(50);

myHashTable.set('grapes', 10000);
myHashTable.get('grapes');
myHashTable.set('apples', 9);
myHashTable.get('apples');
myHashTable.set('apples', 150);
myHashTable.get('apples');
myHashTable.get('applefs');
