function solution(edges) {
    const answer = [0, 0, 0, 0];
    const graph = new Map();
    edges.forEach((edge) => {
        const [a, b] = edge.map(Number);
       if (graph.has(a)) {
           graph.get(a)[0]++;
           if (graph.has(b)) {
               graph.get(b)[1]++;
           } else {
               graph.set(b, [0, 1]);
           }
       } else {
           graph.set(a, [1, 0]);
           if (graph.has(b)) {
               graph.get(b)[1]++;
           } else {
               graph.set(b, [0, 1]);
           }
       }
    });
    for (const [k, v] of graph) {
        if (v[0] > 1 && !v[1]) {
            answer[0] = k;
        } else if (!v[0] && v[1]) {
            answer[2]++;
        } else if (v[0] === 2 && v[1] >= 2) {
            answer[3]++;
        }
    }
    answer[1] = graph.get(answer[0])[0] - answer[2] - answer[3];
    return answer;
}