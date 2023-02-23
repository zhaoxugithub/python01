from collections import deque


if __name__ == '__main__':
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")

    print(queue)

    print("-" * 20)

    # pop出左边的那个元素
    result = queue.popleft()
    print(result)

    # pop 右边那个元素
    result = queue.pop()
    print(result)

    # 打印出元素
    print(queue)
