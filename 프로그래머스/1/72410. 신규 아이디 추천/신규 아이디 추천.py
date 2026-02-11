def solution(new_id):
    answer = ''
    
    able = set(('-', '_', '.'))
    
    #1단계
    new_id = new_id.lower()
    
    #2단계
    new = ''
    for id in new_id:
        if id.isdigit() or id.isalpha() or id in able:
            new += id
    
    #3단계
    while '..' in new:
        new = new.replace('..', '.')
    
    #4단계
    if new and new[0] == '.':
        new = new[1:]
    if new and new[-1] == '.':
        new = new[0:len(new)-1]
    
    #5단계
    if not new:
        new += 'a'
    
    #6단계
    if len(new) >= 16:
        new = new[0:15]
    
    if new and new[-1] == '.':
        new = new[0:len(new)-1]
    
    if len(new) <= 2:
        last = new[-1]
        while len(new) < 3:
            new += last
    return new