function solution(numbers) {
    const n = numbers.length;
    const answer = Array(n).fill(-1);
    const stack = [0];
    for (let i = 1; i < n; i++) {
        while (stack.length && numbers[stack[stack.length - 1]] < numbers[i]) {
            answer[stack.pop()] = numbers[i];
        }
        stack.push(i);
    }
    return answer;
}