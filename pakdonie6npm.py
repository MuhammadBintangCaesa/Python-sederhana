def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

list = [129, 831 ,14]
length = len(list)
i = 0

# Iterating using while loop
while i < length:
    a = list[i]
    print(permute_string(str(a)))
    i += 1;
