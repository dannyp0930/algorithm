class Queue {
    constructor() {
        this.items = {};
        this.frontIndex = 0;
        this.backIndex = 0;
      }

    enqueue(item) {
        this.items[this.backIndex] = item;
        this.backIndex++;
    }

    dequeue() {
        if (this.isEmpty()) return undefined;
        const item = this.items[this.frontIndex];
        delete this.items[this.frontIndex];
        this.frontIndex++;
        return item;
    }

    peek() {
        return this.items[this.frontIndex];
    }

    isEmpty() {
        return this.backIndex - this.frontIndex === 0;
    }

    size() {
        return this.backIndex - this.frontIndex;
    }
}

function solution(players, m, k) {
    let ans = 0;
    let server = 0;
    let queue = new Queue();
    for (let i = 0; i < players.length; i++) {
        if (queue.size() && queue.peek()[0] === i) {
            server -= queue.peek()[1];
            queue.dequeue();
        }
        if (m <= players[i]) {
            const required = parseInt(players[i] / m);
            if (required > server) {
                const newServer = required - server;
                server += newServer;
                ans += newServer;
                queue.enqueue([i + k, newServer]);
            }
        }
    }
    return ans;
}