#Problem 103

from functools import reduce

def sss_ineq(cur_list):
    n, j = len(cur_list), 1
    while j+1 <= n-j:
        if sum(cur_list[0:j+1]) <= sum(cur_list[n-j:n]): return False
        j += 1
    return True

def list_to_str(l):
    return reduce(lambda u, v: str(u) + str(v), l)

def compute_min(list_length, max_sum, cur_list, cur_sums):
    if len(cur_list) == list_length:
        print("long list!")
        if not sss_ineq(cur_list): return False
        return cur_list
    
    this_sum  = sum(cur_list)
    if len(cur_list) > 0:
        range_min = cur_list[-1] + 1
    else:
        range_min = 1
    range_max = 1 + (max_sum - this_sum)//(list_length - len(cur_list))
    
    if len(cur_list) > 1 and cur_list[0] + cur_list[1] < range_max:
        range_max = cur_list[0] + cur_list[1]
    for j in range(range_min, range_max):
        new_sums = []
        for u in cur_sums:
            if j + u in cur_sums:
                break
            new_sums.append(j+u)
        if len(cur_sums) == len(new_sums):
            #print("made it here")
            new_list = compute_min(list_length, max_sum, cur_list + [j], cur_sums + new_sums)
            if new_list: return new_list
    return False
            

MAXLISTLEN, n, min_sss, min_sums = 7, 1, [1], [0,1]
print(n, list_to_str(min_sss), sum(min_sss))

while n < MAXLISTLEN:
    n += 1
    midpt     = len(min_sss)//2
    print('beginning ' + str(n))
    print('our guess is ' + str(min_sss[midpt:midpt+1] + [min_sss[midpt] + u for u in min_sss]))
    
    guess_sum = sum(min_sss[midpt:midpt+1] + [min_sss[midpt] + u for u in min_sss])

    min_sss   = compute_min(n, guess_sum, [], [0])
    print(n, list_to_str(min_sss), sum(min_sss))
