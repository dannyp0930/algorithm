function solution(key, lock) {
    const n = lock.length;
    const m = key.length;
    const rotate = (arr) => {
        const n = arr.length;
        const newArr = Array.from(Array(n), () => Array(n).fill(0));
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                newArr[j][n - i - 1] = arr[i][j]
            }
        }
        return newArr;
    }
    const check = (arr) => {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (arr[i + m][j + m] !== 1) return false;
            }
        }
        return true;
    }
    const arr = Array.from(Array(n + 2 * m), () => Array(n + 2 * m).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (lock[i][j]) arr[i + m][j + m] = 1;
        }
    }
    for (let d = 0; d < 4; d++) {
        for (let i = 0; i <= m + n; i++) {
            for (let j = 0; j <= m + n; j++) {
                const copyArr = arr.map((v) => [...v]);
                for (let k = 0; k < m; k++) {
                    for (let l = 0; l < m; l++) {
                        copyArr[i + k][j + l] += key[k][l];
                    }
                }
                if (check(copyArr)) return true;
            }
        }
        key = rotate(key);
    }
    return false;
}