def snail(snail_map):
    loop_count = int((len(snail_map)+1)/2)
    high_index = len(snail_map)-1
    low_index = 0
    result = []
    if snail_map == [[]]:
        return result
    
    for n in range(loop_count):
        for i in range(low_index, high_index + 1):
            result.append(snail_map[low_index][i])
        for i in range(low_index +1, high_index +1):
            result.append(snail_map[i][high_index])
        for i in range(high_index-1,low_index,-1):
            result.append(snail_map[high_index][i])
        for i in range(high_index, low_index , -1):
            result.append(snail_map[i][low_index])
        low_index += 1
        high_index -= 1
    
    return result