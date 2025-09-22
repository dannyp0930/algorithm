class Node {
    constructor(val, prev, next) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

function solution(n, k, cmd) {
    const answer = Array(n).fill("O");
    const node = Array.from({ length: n }, (_, idx) => new Node(idx, idx ? idx - 1 :null, idx < n - 1 ? idx + 1 : null));
    const stack = [];
    for (const c of cmd) {
        const arr = c.split(" ");
        const command = arr[0];
        let num = Number(arr[1]);
        switch (command) {
            case "U": {
                while (num) {
                    k = node[k].prev;
                    num--;
                }
                break;
            }
            case "D": {
                while (num) {
                    k = node[k].next;
                    num--;
                }
                break;
            }
            case "C": {
                const { prev, next } = node[k];
                stack.push(node[k]);
                if (node[prev]) node[prev].next = next;
                if (node[next]) node[next].prev = prev;
                k = next ? next : prev;
                break;
            }
            case "Z": {
                const { val, prev, next } = stack.pop();
                if (node[prev]) node[prev].next = val;
                if (node[next]) node[next].prev = val;
            }
        }
    }
    for (let s of stack) {
        answer[s.val] = "X";
    }
    return answer.join("");
}