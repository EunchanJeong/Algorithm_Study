def convert(num):

    result = ""
    while num != 1.0:
        if str(num)[0] == "1":
            num = float("0" + str(num)[1:])
            
        num = num * 2
        result += str(num)[0]

        if len(result) > 12:
            return "overflow"

    return result


T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    result = convert(N)

    print(f"#{test_case} {result}")
