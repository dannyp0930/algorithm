function solution(info, edges) {
    let answer = 0;
    const n = info.length;
    const graph = Array.from({ length: n }, () => Array());
    for (const [a, b] of edges) {
        graph[a].push(b);
    }
    const visit = Array(n).fill(false);
    const dfs = (node, sheep, wolf, next) => {   
        if (info[node]) {
            wolf++;
        } else {
            sheep++;
        }
        if (wolf >= sheep) {
            return;
        }
        answer = sheep > answer ? sheep : answer;
        for (const v of next) {
            dfs(v, sheep, wolf, [...next.filter((a) => a !== v), ...graph[v]]);
        }
    }
    dfs(0, 0, 0, graph[0]);
    return answer;
}