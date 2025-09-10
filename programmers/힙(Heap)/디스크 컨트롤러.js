class Heap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    push(value) {
        this.data.push(value);
        let i = this.size() - 1;
        let p = ((i - 1) / 2) >> 0;
        while (i > 0 && this.data[i][1] < this.data[p][1]) {
            this._swap(i, p);
            i = p;
            p = ((i - 1) / 2) >> 0;
        }
    }
    pop() {
        if (!this.size()) return undefined;
        const top = this.data[0];
        if (this.data.length <= 1) {
            this.data = [];
        } else {
            this.data[0] = this.data.pop();    
        }
        let p = 0;
        while (true) {
            let l = p * 2 + 1;
            let r = p * 2 + 2;
            if (l >= this.size()) break;
            let c = l;
            if (r < this.size() && this.data[r][1] < this.data[l][1]) c = r;
            if (this.data[c][1] < this.data[p][1]) {
                this._swap(p, c);
                p = c;
            } else {
                break;
            }
        }
        return top;
    }
    _swap(a, b) {
        [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
    }
}

function solution(jobs) {
    const n = jobs.length;
    const minHeap = new Heap();
    jobs.sort((a, b) => a[0] - b[0]);
    let time = 0, complete = 0, tot = 0;
    while (jobs.length || minHeap.size()) {
        while (jobs.length) {
            if (jobs[0][0] === time) {
                minHeap.push(jobs.shift());
            } else break;
        }
        if (minHeap.size() && time >= complete) {
            const job = minHeap.pop();
            complete = job[1] + time;
            tot += complete - job[0];
        }
        time++;
    }
    return tot / n >> 0;
}