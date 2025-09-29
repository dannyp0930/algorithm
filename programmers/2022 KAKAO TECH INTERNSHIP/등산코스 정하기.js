class Queue {
    constructor() {
        this.items = {};
        this.first = 0;
        this.last = 0;
    }
    push(item) {
        this.items[this.last] = item;
        this.last++;
    }
    popleft() {
        if (!this.size()) return undefined;
        const item = this.items[this.first];
        delete this.items[this.first];
        this.first++;
        return item;
    }
    size() {
        return this.last - this.first;
    }
}

function solution(n, paths, gates, summits) {
    const graph = Array.from(Array(n + 1), () => []);
    summits.sort((a, b) => a - b);
    for (const [a, b, e] of paths) {
        if (gates.includes(a)) graph[a].push([b, e]);
        else if (gates.includes(b)) graph[b].push([a, e]);
        else if (summits.includes(a)) graph[b].push([a, e]);
        else if (summits.includes(b)) graph[a].push([b, e]);
        else graph[a].push([b, e]), graph[b].push([a, e]);
    }
    const queue = new Queue();
    const intensity = Array(n + 1).fill(Infinity);
    for (const gate of gates) {
        queue.push([gate, 0]);
        intensity[gate] = 0;
    }
    while (queue.size()) {
        const [curNode, curDist] = queue.popleft();
        if (summits.includes(curNode) || intensity[curNode] < curDist) continue;
        for (const [nextNode, nextDist] of graph[curNode]) {
            const dist = nextDist > curDist ? nextDist : curDist;
            if (dist < intensity[nextNode]) {
                intensity[nextNode] = dist;
                queue.push([nextNode, dist]);
            }
        }
    }
    const answer = [0, Infinity];
    for (const summit of summits) {
        if (answer[1] > intensity[summit]) {
            answer[0] = summit;
            answer[1] = intensity[summit];
        }
    }
    return answer;
}