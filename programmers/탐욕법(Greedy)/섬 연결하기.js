function solution(n, costs) {
    let answer = 0;
    costs.sort((a, b) => a[2] - b[2]);
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        if (parent[x] === x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    const union = (a, b) => {
        a = find(a);
        b = find(b);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }
    for (const [a, b, c] of costs) {
        if (find(a) !== find(b)) {
            answer += c;
            union(a, b);
        }
    }
    return answer;
}