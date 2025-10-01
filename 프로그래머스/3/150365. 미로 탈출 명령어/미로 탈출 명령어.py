from collections import deque
import copy
import sys
sys.setrecursionlimit(10**8)

answer = ''
def solution(n, m, x, y, r, c, k):
    
    x -=1 
    y -= 1
    r -= 1
    c -= 1
    
    #이동거리 총 k여야함, 그리고 같은 격자 2번 이상 방문 가능, 모든 경로중 문자열 사전 순으로 가장 빠른 경로
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    def dfs(start_x, start_y, depth, move):
        global answer
        if depth == k:
            if start_x == r and start_y == c:
                return move

        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                remain = k - (depth + 1)
                dist = abs(nx - r) + abs(ny - c)
                if dist > remain or (remain - dist) % 2 == 1:
                    continue
                                    
                res = dfs(nx, ny, depth+1, move+str(i)) 
                if res is not None:
                    return res
    
    mm = dfs(x, y, 0, "")
    if mm is None:
        return "impossible"
    mm = mm.replace('0', "d").replace('1', "l").replace('2', "r").replace('3', "u")
    return mm