class Heap {
    constructor() {
      this.heap = [];
    }
  
    swap(index1, index2) {
      [this.heap[index1], this.heap[index2]] = 
        [this.heap[index2], this.heap[index1]];
    }
    getParentIndex(index) { return Math.floor((index - 1) / 2); }
    getLeftChildIndex(index) { return index * 2 + 1; }
    getRightChildIndex(index) { return index * 2 + 2; }
  
    getParent(index) { return this.heap[this.getParentIndex(index)]; }
    getLeftChild(index) { return this.heap[this.getLeftChildIndex(index)]; }
    getRightChild(index) { return this.heap[this.getRightChildIndex(index)]; }
  
    peek() { return this.heap[0]; }
    size() { return this.heap.length; }
  }
  
  class MinHeap extends Heap {
    
    heapifyUp() {
      let index = this.heap.length - 1
      while (this.getParent(index) !== undefined
        && this.getParent(index) > this.heap[index]) {
        this.swap(index, this.getParentIndex(index));
        index = this.getLeftChildIndex(index);
      }
    }
  
    heapifyDown() {
      let index = 0;
      while (this.getLeftChild(index) !== undefined 
        && this.getLeftChild(index) < this.heap[index]
        || this.getRightChild(index) < this.heap[index]) {
        let smallerIndex = this.getLeftChildIndex(index);
        if (this.getRightChild(index) !== undefined
          && this.getRightChild(index) < this.heap[smallerIndex]) {
          smallerIndex = this.getRightChildIndex(index);
        }
        this.swap(index, smallerIndex);
        index = smallerIndex;
      }
    }
  
    enqueue(num) {
      this.heap[this.size()] = num;
      this.heapifyUp();
    }
  
    dequeue() {
      let tmp = this.peek();
      this.heap[0] = this.heap[this.size() - 1];
      this.heap.pop();
      this.heapifyDown();
      return tmp;
    }
  
    dequeueMax() {
      const parentIndex = this.getParentIndex(this.size() - 1);
      const lastLeaf = this.heap.slice(parentIndex);
      const max = Math.max(...lastLeaf);
      this.swap(parentIndex + lastLeaf.indexOf(max), this.size() - 1);
      return this.heap.pop();
    }
    
    max() {
      const parentIndex = this.getParentIndex(this.size() - 1);
      const lastLeaf = this.heap.slice(parentIndex);
      return Math.max(...lastLeaf);
    }
  }
  
  function solution(operations) {
    const minHeap = new MinHeap();
    operations.forEach(op => {
      let [command, num] = op.split(' ');
      num = parseInt(num);
      if (command == 'I') {
        minHeap.enqueue(num);
      } else if (num === -1) {
        minHeap.dequeue();
      } else {
        minHeap.dequeueMax();
      }
    })
    
    if (minHeap.size() > 0) {
      return [minHeap.max(), minHeap.peek()];
    }
    return [0, 0]
  }