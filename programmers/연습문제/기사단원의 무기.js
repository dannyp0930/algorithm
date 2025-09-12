function solution(number, limit, power) {
    var answer = 0;
    const getCnt = (num) => {
        let res = 0;
        for (let i = 1; i <= Math.sqrt(num); i++){
            if (!(num % i)) {
                if (i === num / i) {
                    res++;
                } else {
                    res += 2;
                }
            }
        }
        return res;
    }
    for (let i = 1; i <= number; i++) {
        const cnt = getCnt(i);
        if (cnt > limit) {
            answer += power;
        } else {
            answer += cnt;
        }
    }
    return answer;
}