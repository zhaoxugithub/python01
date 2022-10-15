from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter your choice of 'red','blue' or 'green'\n"))

match color:
    case Color.RED:
        print("I see red!")
    case Color.BLUE:
        print("I see blue")
    case Color.GREEN:
        print("I'm feeling the blues:(")
