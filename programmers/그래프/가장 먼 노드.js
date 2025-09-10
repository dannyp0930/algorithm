function solution(n, edge) {
    const graph = Array.from(Array(n + 1), () => []);
    for (const e of edge) {
        const [a, b] = e;
        graph[a].push(b);
        graph[b].push(a);
    }
    const visit = Array(n + 1).fill(0);
    const queue = [1];
    visit[1] = 1;
    let maxLength = 0;
    while (queue.length) {
        const v = queue.shift();
        for (const e of graph[v]) {
            if (!visit[e]) {
                visit[e] = visit[v] + 1;
                maxLength = visit[e] > maxLength ? visit[e] : maxLength;
                queue.push(e);
            }
        }
    }
    return visit.reduce((a, b) => a + (b === maxLength ? 1 : 0), 0);
}