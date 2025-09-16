function solution(triangle) {
    const n = triangle.length;
    for (let i = 1; i < n; i++) {
        const m = triangle[i].length;
        for (let j = 0; j < m; j++) {
            if (j === 0) {
                triangle[i][j] += triangle[i - 1][0];
            } else if (j === m - 1) {
                triangle[i][j] += triangle[i - 1][m - 2];
            } else {
                triangle[i][j] += triangle[i - 1][j - 1] > triangle[i - 1][j] ? triangle[i - 1][j - 1] : triangle[i - 1][j];
            }
        }
    }
    let answer = 0;
    for (let res of triangle[n - 1]) {
        answer = answer > res ? answer : res;
    }
    return answer;
}