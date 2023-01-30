class Stack {
    constructor() {
        this.items = [];
    }

    peek() {
        return this.items[this.items.length-1]
    }

    push(value) {
        this.items.push(value)
    }

    pop() {
        this.items.pop()
    }

}

const myStack = new Stack();
myStack.push("Discord")
myStack.push("Udemy")
myStack.push("google")
console.log(myStack)

console.log(myStack.pop())
console.log(myStack)

console.log(myStack.pop())
console.log(myStack.pop())

console.log(myStack)
// console.log(myStack.peek())

//Discord
//Udemy
//google