function solution(s) {
    const answer = [];
    for (let str of s) {
        const stack = [];
        let cnt = 0;
        for (let char of str) {
            stack.push(char);
            if (stack.length >= 3 && 
                stack[stack.length - 3] === '1' && 
                stack[stack.length - 2] === '1' && 
                stack[stack.length - 1] === '0') {
                stack.pop();
                stack.pop();
                stack.pop();
                cnt++;
            }
        }
        let insertPos = -1;
        for (let i = stack.length - 1; i >= 0; i--) {
            if (stack[i] === '0') {
                insertPos = i;
                break;
            }
        }
        const result = [];
        for (let i = 0; i <= insertPos; i++) {
            result.push(stack[i]);
        }
        for (let i = 0; i < cnt; i++) {
            result.push('1', '1', '0');
        }
        for (let i = insertPos + 1; i < stack.length; i++) {
            result.push(stack[i]);
        }
        answer.push(result.join(''));
    }
    return answer;
}