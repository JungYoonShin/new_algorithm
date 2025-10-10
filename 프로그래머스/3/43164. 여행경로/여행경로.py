
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
def solution(tickets):

    answer = []
    tickets.sort()  # 티켓을 사전순으로 정렬

    path = ["ICN"]  # 경로 저장 리스트
    visited = [False] * len(tickets)


    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, (src, dst) in enumerate(tickets):
            if src == start and not visited[idx]:
                visited[idx] = True
                dfs(dst, path+[dst])
                visited[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()

    return answer[0]