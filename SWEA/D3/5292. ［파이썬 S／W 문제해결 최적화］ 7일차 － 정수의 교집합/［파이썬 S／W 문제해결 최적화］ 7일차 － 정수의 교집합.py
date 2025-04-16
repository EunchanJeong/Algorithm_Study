T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    nums1 = set(map(int, input().split()))
    nums2 = set(map(int, input().split()))
    
    print(f'#{test_case} {len(nums1 & nums2)}')