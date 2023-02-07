def solution(today, terms, privacies):
    answer = []

    yy, mm, dd = map(int, today.split("."))
    days_now = yy * 12 * 28 + mm * 28 + dd

    for j in range(len(privacies)):
        date, now_term = privacies[j].split()
        year, month, day = map(int, date.split("."))
        days_past = year * 12 * 28 + month * 28 + day
        time = days_now - days_past + 1
        print("\ntime :", time)
        for i in range(len(terms)):
            term, months = terms[i].split()
            valid_time = int(months) * 28
            if term == now_term:
                print(term, months, valid_time, end=" ")
                if valid_time < time:
                    answer.append(j + 1)

    return answer
