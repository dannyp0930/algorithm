function solution(numbers) {
    const answer = [];
    const binarySearch = (str, s, e) => {
        if (s === e) return true;
        const m = (s + e) / 2 >> 0;
        const l = (s + m - 1) / 2 >> 0;
        const r = (m + e + 1) / 2 >> 0;
        if (str[m] === '0' && (str[l] === '1' || str[r] === '1')) return false;
        return binarySearch(str, s, m - 1) && binarySearch(str, m + 1, e);
    }
    for (const number of numbers) {
        const biNum = number.toString(2);
        const n = biNum.length.toString(2).length;
        const cbt = biNum.padStart(2 ** n - 1, '0')
        answer.push(binarySearch(cbt, 0, 2 ** n - 2) ? 1 : 0);
    }
    return answer;
}