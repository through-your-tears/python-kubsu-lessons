from collections import Counter


def main():
    n = int(input())
    inp = [int(a) for a in input().split()]
    c = dict(Counter(inp))
    count = 0
    answers = []
    while len(c) > 2:
        sorted_keys = sorted(c, key=lambda x: c.get(x))
        c[sorted_keys[-1]] -= 1
        c[sorted_keys[-2]] -= 1
        c[sorted_keys[-3]] -= 1
        answers.append(sorted_keys[-3:])
        keys_for_delete = list(filter(lambda x: c.get(x) == 0, c))
        for key in keys_for_delete:
            c.pop(key)
        count += 1
    print(count)
    for row in answers:
        print(*row)


if __name__ == '__main__':
    main()
