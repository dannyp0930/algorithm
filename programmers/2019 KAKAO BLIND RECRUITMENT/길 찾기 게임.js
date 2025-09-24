class BinaryTree {
    constructor(value, xPos) {
        this.value = value;
        this.xPos = xPos;
        this.left = null;
        this.right = null;
    }
    insert(value, xPos) {
        if (xPos <= this.xPos) {
            this._left(value, xPos);
        } else {
            this._right(value, xPos);
        }
    }
    _left(value, xPos) {
        if (this.left) {
            this.left.insert(value, xPos);
        } else {
            this.left = new BinaryTree(value, xPos);
        }
    }
    _right(value, xPos) {
        if (this.right) {
            this.right.insert(value, xPos);
        } else {
            this.right = new BinaryTree(value, xPos);
        }
    }
    preOrder(node, arr) {
        if (node) {
            arr.push(node.value);
            this.preOrder(node.left, arr);
            this.preOrder(node.right, arr);
        }
    }
    postOrder(node, arr) {
        if (node) {
            this.postOrder(node.left, arr);
            this.postOrder(node.right, arr);
            arr.push(node.value);
        }
    }
}

function solution(nodeinfo) {
    const n = nodeinfo.length;
    const nodes = nodeinfo.map((node, idx) => [ idx + 1, ...node ]).sort((a, b) => b[2] - a[2]);
    const tree = new BinaryTree(nodes[0][0], nodes[0][1]);
    for (let i = 1; i < n; i++) {
        tree.insert(nodes[i][0], nodes[i][1]);
    }
    const preArr = [], postArr = [];
    tree.preOrder(tree, preArr);
    tree.postOrder(tree, postArr);
    return [preArr, postArr];
}