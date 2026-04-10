if __name__ == '__main__':
    names_scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name,score])
    scores = sorted(set(score for name, score in names_scores))
    second_lowest = scores[1]
    result=[]
    for name,score in names_scores:
        if score == second_lowest:
            result.append(name)
    result.sort()
    for name in result:
        print(name)
#nastedlist