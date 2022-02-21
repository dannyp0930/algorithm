from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    report_dict = defaultdict(set)
    banned_cnt = defaultdict(int)
    banned = []

    for r in report:
        do_report, be_reported = r.split()

        banned_cnt[be_reported] += 1
        report_dict[do_report].add(be_reported)

        if banned_cnt[be_reported] == k:
            banned.append(be_reported)

    for b in banned:
        for i in range(len(id_list)):
            if b in report_dict[id_list[i]]:
                answer[i] += 1

    return answer
