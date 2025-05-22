def inorder(node):
    if len(node) == 1:
        result.append(node[0])
        return

    inorder(tree[node[1]])
    result.append(node[0])

    if len(node) == 3:
        inorder(tree[node[2]])

for test_case in range(1, 11):
    N = int(input())

    tree = {}

    for _ in range(N):
        t = list(input().split())
        tree[t[0]] = t[1:]

    result = []

    inorder(tree["1"])

    result = "".join(result)
    print(f"#{test_case} {result}")