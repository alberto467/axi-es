def min_num_cd(d: list[int], d_max: int):
    n = [0]
    sum_d = d[0]

    for i in range(1, len(d)):
        if (sum_d + d[i] > d_max):
            n.append(i-1)
            sum_d = d[i]
        else:
            sum_d += d[i]
        
    n.append(len(d))

    return n

print(min_num_cd([1,5,3,7,4,2,6,8,7,5,4,9,7,5,2,7,6,4,2,1,8,6,5,3], 24))