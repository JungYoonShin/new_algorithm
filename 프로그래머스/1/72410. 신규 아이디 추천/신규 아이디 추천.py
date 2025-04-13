def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 문자 제거
    valid_chars = ['-', '_', '.']
    answer = ''
    for s in new_id:
        if s.isalnum() or s in valid_chars:
            answer += s
    
    # 3단계: 연속된 마침표를 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계: 처음과 끝의 마침표 제거
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계: 아이디가 비어 있으면 'a'를 대입
    if len(answer) == 0:
        answer += 'a'
    
    # 6단계: 아이디 길이가 16자 이상이면 15자까지 자르고 마지막 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer
