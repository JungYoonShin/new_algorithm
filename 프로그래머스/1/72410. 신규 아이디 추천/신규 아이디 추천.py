def solution(new_id):
    answer = ''
    
    #1단계 소문자로 치환
    new_id = new_id.lower()
    
    #2단계 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    new = ''
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in['-', '_', '.']:
            new += s
    
    #3단계 .가 2번 연속 이상인 부분을 .로 치환
    for i in range(len(new)):
        new = new.replace('..', '.')
    
    #4단계 .가 처음이나 끝에 위치하면 제거
    if new and new[0] == '.':
        new = new[1:]
    if new and new[-1] == '.':
        new = new[0:len(new)-1]
        
    #5단계 빈 문자열이라면 a를 대입
    if not new:
        new = 'a'
    
    #6단계 16자 이상이면 15개만 남기고 제거, 제거 후 마침표가 마지막에 오면 제거
    if len(new) >= 16:
        new = new[0:15]
        if new[-1] == '.':
            new = new[0:14]
    
    #7단계 길이가 2자 이하라면 마지막 문자를 길이 3이 될때까지 붙이기
    if len(new) <= 2:
        while len(new) <= 2:
            new += new[-1]
    # print(new)
    return new