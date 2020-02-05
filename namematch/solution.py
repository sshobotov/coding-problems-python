def solve(possible_names, needle):
    normalized_needle = needle.lower()
    return [elem for elem in possible_names if __matches(elem.lower(), normalized_needle)]


def __matches(proposition, needle, memo=set()):
    if proposition != "" and len(proposition) >= len(needle):
        if needle == "":
            return True

        memo_value = (needle, proposition)
        if memo_value not in memo:
            head, tail = needle[0], needle[1:]
            start_at = 0
            while True:
                found_at = proposition.find(head, start_at)
                if found_at == -1:
                    break
                if __matches(proposition[found_at + 1:], tail, memo):
                    return True
                else:
                    start_at = found_at + 1

            memo.add(memo_value)

    return False
