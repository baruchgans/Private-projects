class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    peek() {
        return this.first
    }

    enqueue(value) {
        let newNode = new Node(value);
        if (this.length === 0) {
            this.first = this.last = newNode
        } else {
            this.last.next = newNode
            this.last = newNode
        }
        this.length++;
        return this;
    }

    dequeue() {
        if (this.length === 0) {
            return this;
        }
        if (this.length === 1) {
            this.last = null;
        }
        this.first = this.first.next;
        this.length--;
        return this
    }

    //isEmpty;
}

const myQueue = new Queue();
myQueue.enqueue("Joy")
myQueue.enqueue("Matt")
myQueue.enqueue("Pavel")
myQueue.enqueue("Samir")

myQueue.dequeue()
myQueue.dequeue()

//Joy
//Matt
//Pavel
//Samir

