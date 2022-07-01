def solution(priorities, location):
    ans =[]
    pr_total =[]
    for i in range(len(priorities)):
        pr_total.append((priorities[i],i))
        
    x = pr_total.pop(0)
    while pr_total:
        for i in range(len(pr_total)):
            if x[0] < pr_total[i][0]:
                pr_total.append(x)
                x = pr_total.pop(0)
                break
        else:
            ans.append(x)
            x = pr_total.pop(0)
    ans.append(x)
    for i in range(len(ans)):
        if location == ans[i][1]:
            return i+1