from collections import defaultdict
def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    report_count = defaultdict(int)
    report_status = defaultdict(list)
    reports = set(reports)
    
    #k번 이상 신고 받으면 이용 정지 당함
    for report in reports:
        a, b = report.split(" ")
        report_count[b] += 1
        report_status[a].append(b)
    
    for i in range(len(id_list)):
        for man in report_status[id_list[i]]:
            if report_count[man] >= k:
                answer[i] += 1
    
    return answer