from collections import defaultdict
# 갯수만 구하면 되기 때문에 알파벳을 구분할 필요는 없다.
# 그냥 중복되는 갯수를 없애면 됨.
def minDeletions(s: str) -> int:
    num_of_alpha = defaultdict(int)

    for ch in s:
        num_of_alpha[ch] += 1

    duplicated_set = set()
    answer = 0
    for num in sorted(num_of_alpha.values()):
        while (num in duplicated_set) and num > 0:
            num -= 1
            answer += 1
        duplicated_set.add(num)

    return answer


# print(minDeletions('ceabaacb'))  # 2
# print(minDeletions('aaabbbcc'))  # 2
print(minDeletions('bbcebab'))  # 2
# print(minDeletions("abababe"))  # 1
