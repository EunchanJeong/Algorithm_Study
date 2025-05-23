nums1 = {"ZRO": 0, "ONE": 1 , "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
nums2 = {}

for k, v in nums1.items():
    nums2[v] = k

T = int(input())
for _ in range(1, T+1):
    test_case, length = input().split()

    tmp = [nums1[n] for n in list(input().split())]
    tmp.sort()

    result = []
    for n in tmp:
        result.append(nums2[n])

    print(f"{test_case} {' '.join(result)}")