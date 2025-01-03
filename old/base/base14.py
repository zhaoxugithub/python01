import dataclasses


def http_error(status):
    match status:
        case 400:
            print("400")
        case 404:
            print("404")
        case 418:
            print("418")
        case 401 | 402 | 405:
            print("401,402,405")
        case _:
            print("other")


def point_error(point):
    match point:
        case (0, 0):
            print("origin")
        case (0, y):
            print(f'y = {y}')
        case (x, 0):
            print(f'x ={x}')
        case (x, y):
            print(f'x={x},y={y}')
        case _:
            raise ValueError("Not a point")


@dataclasses
class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


def where_is_points(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")


def where_is_point_if(point):
    match point:
        case Point(x, y) if x == y:
            print("y==x at [X]")
        case Point(x, y):
            print(f'Not on the diagonal')

        case _:
            print("bbbbbbbbbb")


if __name__ == '__main__':
    http_error(401)
    http_error("fdsfadf")
    point_error((8, 9))

    where_is_points([])

    where_is_point_if(Point(3, 3))
