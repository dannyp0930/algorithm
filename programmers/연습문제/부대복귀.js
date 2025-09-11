function solution(n, roads, sources, destination) {
    const graph = Array.from(Array(n + 1), () => Array());
    const visit = Array(n + 1).fill(0);
    roads.forEach(([a, b]) => {
        graph[b].push(a);
        graph[a].push(b);
    });
    const queue = new Queue();
    queue.push(destination);
    visit[destination] = 1;
    while (queue.size()) {
        const n = queue.pop();
        for (const v of graph[n]) {
            if (!visit[v]) {
                visit[v] += visit[n] + 1;
                queue.push(v);
            }
        }
    }
    return sources.map((source) => visit[source] - 1);
}

class Queue {
    constructor() {
        this.data = [];
        this.first = 0;
        this.last = 0;
    }
    size() {
        return this.last - this.first;
    }
    push(item) {
        this.data.push(item);
        this.last++;
    }
    pop() {
        if (!this.size()) return undefined;
        const item = this.data[this.first];
        delete this.data[this.first];
        this.first++;
        return item;
    }
    
}