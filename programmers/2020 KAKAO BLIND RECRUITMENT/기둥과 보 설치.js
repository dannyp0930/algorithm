function solution(n, build_frame) {
    const answer = [];
    const checkPillar = (arr, x, y) => {
        if (!y) return true;
        if (arr.find(([i, j, k]) => i === x && j === y - 1 && !k)) return true;
        if (arr.find(([i, j, k]) => i === x && j === y && k)) return true;
        if (arr.find(([i, j, k]) => i === x - 1 && j === y && k)) return true;
        return false;
    }
    const checkBeam = (arr, x, y) => {
        if (arr.find(([i, j, k]) => i === x && j === y - 1 && !k)) return true;
        if (arr.find(([i, j, k]) => i === x + 1 && j === y - 1 && !k)) return true;
        if (arr.find(([i, j, k]) => i === x + 1 && j === y && k) && 
            arr.find(([i, j, k]) => i === x - 1 && j === y && k)) return true;
        return false;
    }
    const handleCreate = (x, y, a) => {
        if (a && checkBeam(answer, x, y)) answer.push([x, y, a]);
        else if (!a && checkPillar(answer, x, y)) answer.push([x, y, a]);
    }
    const handleDelete = (x, y, a) => {
        const newArr = answer.filter(([i, j, k]) => i !== x || j !== y || k !== a);
        const idx = answer.findIndex(([i, j, k]) => i === x && j === y && k === a);
        for (const [i, j, k] of newArr) {
            if ((k && !checkBeam(newArr, i, j, k)) || (!k && !checkPillar(newArr, i, j, k))) return;
        }
        answer.splice(idx, 1);
    }
    for (const [x, y, a, b] of build_frame) {
        if (b) handleCreate(x, y, a);
        else handleDelete(x, y, a);
    }
    return answer.sort((a, b) => a[0] === b[0] ? (a[1] === b[1] ? a[2] - b[2] : a[1] - b[1]) : a[0] - b[0]);
}