def solution(today, terms, privacies):
    answer = []
    
    t_y, t_m, t_d = map(int, today.split("."))
    term_dict = {}
    
    for term in terms:
        type, m = term.split(' ')
        term_dict[type] = int(m)
        
    
    #약관에 따라 유효기간이 지난 개인정보를 구함
    for i, privacy in enumerate(privacies):
        date, type = privacy.split(" ")
        year, month, day = map(int, date.split("."))
        
        today_total = t_y * 12 * 28 + t_m * 28 + t_d
        privacy_total = year * 12 * 28 + month * 28 + day
        
        if privacy_total + 28 * term_dict[type] <= today_total:
            answer.append(i+1)
        
    
    return answer