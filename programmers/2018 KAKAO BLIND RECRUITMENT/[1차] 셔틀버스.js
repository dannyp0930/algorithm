function solution(n, t, m, timetable) {
    const timeArr = timetable.map((time) => {
        const [hour, minute] = time.split(":").map((t) => parseInt(t));
        return hour * 60 + minute;
    }).sort((a, b) => a - b);
    let current = 540;
    for (let i = 0; i < n; i++) {
        let queue = timeArr.filter((time) => time <= current).length;
        if (i === n - 1) {
            if (queue >= m) {
                current = timeArr[m - 1] - 1;    
            }
        } else {
            timeArr.splice(0, queue > m ? m : queue);
            current += t;
        }
    }
    const hour = (current / 60) >> 0;
    const minute = current - hour * 60;
    const convertNum = (num) => num.toString().padStart(2, "0");
    return `${convertNum(hour)}:${convertNum(minute)}`
}