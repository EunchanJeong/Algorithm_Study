from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        q = deque()
        q.append([begin, 0])

        while q:
            now, step = q.popleft()

            if now == target:
                return step

            for word in words:
                count = 0
                for i in range(len(now)):
                    if now[i] != word[i]:
                        count += 1
                if count == 1:
                    q.append([word, step+1])
  