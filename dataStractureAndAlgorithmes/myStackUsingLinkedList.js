class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        return this.top
    }

    push(value) {
        let newNode = new Node(value, null)
        if (this.isEmpty()) {
            this.bottom = newNode
            this.top = newNode
        } else {
            let prevYop = this.top
            this.top = newNode
            this.top.next = prevYop;
        }
        this.length++;
    }

    pop() {
        if (this.isEmpty) {
            return
        }
        let toRemove = this.top
        if(this.length === 1){
            this.top = this.bottom = null
        }
        else{
           this.top = this.top.next;
        }
        this.length--;
        return toRemove;
    }

    isEmpty() {
        return this.length === 0;
    }
}

const myStackUsingLinkedList = new Stack();
myStackUsingLinkedList.push("Discord")
myStackUsingLinkedList.push("Udemy")
myStackUsingLinkedList.push("google")
console.log(myStackUsingLinkedList.pop())
console.log(myStackUsingLinkedList.pop())
console.log(myStackUsingLinkedList.pop())
console.log(myStackUsingLinkedList.pop())
console.log(myStackUsingLinkedList)
// console.log(myStackUsingLinkedList.peek())

//Discord
//Udemy
//google