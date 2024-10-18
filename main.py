# YOUR CODE HERE
def summation(list1, list2):
    updated_list = [0] * len(list1)
    for i in range(len(list1)):
        updated_list[i] = list1[i] + list2[i] 
    return updated_list

def find_min_max(list_):
    return min(list_), max(list_)

len_list = int(input())

result_list = summation([int(input()) for _ in range(len_list)], [int(input()) for _ in range(len_list)])
print(result_list)
print(find_min_max(result_list))
