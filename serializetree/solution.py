from typing import Tuple


class Node:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


__SEP = ','
__WRP = '"'


# TODO: Check finite machine approach to make parsing more readable
def serialize_plain(tree: Node) -> str:
    return __SEP.join([
        __WRP + __escape_plain(tree.val) + __WRP,
        "" if tree.left is None else serialize_plain(tree.left),
        "" if tree.right is None else serialize_plain(tree.right)
    ])


def deserialize_plain(s: str) -> Node:
    size = len(s)
    result, ends_at = __deserialize_plain(s, size, 0)
    if ends_at != size - 1:
        raise Exception("Failed to deserialize Node from `" + s + "`. Inconsistent branches after " + str(ends_at))
    return result


def __deserialize_plain(s: str, size: int, value_starts_at: int) -> Tuple[Node, int]:
    if s[value_starts_at] != __WRP or value_starts_at + 1 == size:
        raise Exception("Failed to parse Node from `" + s + "`. Illegal value start")

    value_ends = value_starts_at + 1
    for j in range(value_starts_at + 2, size):
        if s[j] == __WRP and s[j - 1] != '\\':
            value_ends = j
            break
    value = __restore_plain(s[value_starts_at + 1:value_ends])

    l_branch_sep_at = value_ends + 1
    if l_branch_sep_at == size or s[l_branch_sep_at] != __SEP:
        raise Exception("Failed to parse Node from `" + s + "`. Can't find left branch separator")

    left_node, right_starts_at = __parse_left(s, size, l_branch_sep_at + 1)
    right_node, root_ends_at = __parse_right(s, size, right_starts_at)

    return Node(value, left_node, right_node), root_ends_at


def __parse_left(s: str, size: int, left_starts_at: int) -> Tuple[Node, int]:
    if left_starts_at == size:
        raise Exception("Failed to parse Node from `" + s + "`. Can't find left branch start")
    elif s[left_starts_at] == __SEP:
        left_node, right_starts = None, left_starts_at + 1
    else:
        left_node, left_ends = __deserialize_plain(s, size, left_starts_at)
        if left_ends + 1 == size or s[left_ends + 1] != __SEP:
            raise Exception("Failed to parse Node from `" + s + "`. Can't find right branch separator")
        right_starts = left_ends + 2

    return left_node, right_starts


def __parse_right(s: str, size: int, right_starts_at: int) -> Tuple[Node, int]:
    if right_starts_at == size:
        right_node, ends_at = None, size - 1
    elif s[right_starts_at] == __SEP:
        right_node, ends_at = None, right_starts_at - 1
    else:
        right_node, ends_at = __deserialize_plain(s, size, right_starts_at)

    return right_node, ends_at


def __escape_plain(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def __restore_plain(s: str) -> str:
    return s.replace('\\"', '"').replace("\\\\", "\\")


# Less efficient space-wise but more readable format
def serialize(tree: Node) -> str:
    values = [
        __escape(tree.val),
        "" if tree.left is None else serialize(tree.left),
        "" if tree.right is None else serialize(tree.right)
    ]
    return "(" + ",".join(values) + ")"


def deserialize(raw: str) -> Node:
    size = len(raw)
    return __deserialize(raw, size, 0, size - 1)


def __deserialize(raw: str, size: int, li: int, ri: int) -> Node:
    if size < 3 or raw[li] != "(" or raw[ri] != ")":
        raise Exception("Failed to parse Node from " + raw)

    li = li + 1
    ri = ri - 1

    value_end = __find_value_splitter(raw, li, ri)
    if value_end == -1:
        raise Exception("Failed to parse Node from " + raw)

    left_start = value_end + 1
    left_delim = __find_branch_splitter(raw, left_start, ri)
    if left_delim == -1:
        raise Exception("Failed to parse Node from " + raw)

    left_size = left_delim - 1 - left_start
    right_start = left_delim + 1
    right_size = ri - right_start

    return Node(
        __unescape(raw[li:value_end]),
        None if left_size <= 0 else __deserialize(raw, left_size, left_start, left_delim - 1),
        None if right_size <= 0 else __deserialize(raw, right_size, right_start, ri)
    )


def __find_value_splitter(escaped: str, li: int, ri: int) -> int:
    if ri - li < 1:
        return -1

    for i in range(li, ri + 1):
        if escaped[i] == "," and\
                (escaped[i + 1] == "," or escaped[i + 1] == "(") and\
                (i == 0 or escaped[i - 1] != "\\"):
            return i

    return -1


def __find_branch_splitter(escaped: str, li: int, ri: int) -> int:
    if escaped[li] == ",":
        return li

    if escaped[li] == "(":
        opened_braces = 1
        for i in range(li + 1, ri):
            if escaped[i] == "(":
                opened_braces += 1
            elif escaped[i] == ")":
                opened_braces -= 1
                if opened_braces == 0 and escaped[i + 1] == ",":
                    return i + 1

    return -1


def __escape(raw: str) -> str:
    return raw.replace("\\", "\\\\").replace(",", "\\,")


def __unescape(escaped: str) -> str:
    return escaped.replace("\\,", ",").replace("\\\\", "\\")
