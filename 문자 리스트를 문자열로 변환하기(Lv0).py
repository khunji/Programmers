def solution(arr):
    letter = ""
    for i in range(len(arr)):
        letter=letter+arr[i]
    return letter


arr= ["a","b","c"]
result = solution(arr)
print(result)