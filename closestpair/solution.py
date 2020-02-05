from typing import Sequence, Tuple
import math

Point = Tuple[int, int]
ClosestPoints = Tuple[Point, Point]


def find(points: Sequence[Point]) -> Tuple[float, ClosestPoints]:
    sorted_points = sorted(points, key=lambda x: x[0])
    return __find_rec(sorted_points, len(sorted_points))


def __find_rec(points: Sequence[Point], size: int) -> Tuple[float, ClosestPoints]:
    if size <= 3:
        return __find_brut_force(points, size)

    mid = size // 2
    min_lt = __find_rec(points[:mid], mid)
    min_rt = __find_rec(points[mid:], size - mid)
    (min_d, min_r) = min(min_lt, min_rt, key=lambda x: x[0])

    mid_x = points[mid][0] - (points[mid][0] - points[mid - 1][0]) / 2
    strip = __collect_strip(points[:mid], mid_x - min_d, 0, -1) + __collect_strip(points[mid:], mid_x + min_d, 0, 1)

    strip_size = len(strip)
    if strip_size == 0:
        return min_d, min_r

    return __find_stripped(strip, strip_size, min_d)


def __find_brut_force(points: Sequence[Point], size: int) -> Tuple[float, ClosestPoints]:
    product = [
        (__distance(points[i], points[j]), (points[i], points[j])) for i in range(size) for j in range(i + 1, size)
    ]
    return min(product, key=lambda x: x[0])


def __find_stripped(points: Sequence[Point], size: int, min_d: float) -> Tuple[float, ClosestPoints]:
    by_y = sorted(points, key=lambda x: x[1])

    product = []
    for i in range(size):
        for j in range(i + 1, size):
            if i != j and (by_y[j][1] - by_y[i][1]) < min_d:
                product.append((__distance(by_y[j], by_y[i]), (by_y[i], by_y[j])))

    return min(product, key=lambda x: x[0])


def __collect_strip(points: Sequence[Point], limit: float, coordinate: int, direction: int) -> list:
    collected = list()

    for p in points[::direction]:
        if direction < 0 and p[coordinate] < limit:
            return collected
        if direction > 0 and p[coordinate] > limit:
            return collected
        collected.append(p)

    return collected


def __distance(p1: Point, p2: Point) -> float:
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
