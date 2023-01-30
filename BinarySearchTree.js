class Node {
    constructor(value) {
        this.left = null;
        this.right = null;
        this.value = value;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(value) {
        //  Check if value is smaller or greater than node,then go down right and left respectively.
        //   if is empty, assign there, if not, continue the same processing
        if (this.root.value == null) {
            this.root.value = value
            return;
        }
        let curr = this.root
        while (true) {
            if (value < curr.value) {
                if (curr.left) {
                    curr = curr.left
                } else {
                    curr.left = new Node(value)
                    return;
                }
            } else {
                if (curr.right) {
                    curr = curr.right
                } else {
                    curr.right = new Node(value)
                    return;
                }
            }


        }
    }

    lookup(value) {
        //Code here
    }

    // remove
}

const tree = new BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
JSON.stringify(traverse(tree.root))

//     9
//  4     20
//1  6  15  170

function traverse(node) {
    const tree = {value: node.value};
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}





