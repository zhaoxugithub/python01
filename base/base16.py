def ask_ok(message, retires=4, reminder="please try again！"):
    ok = input(message)
    print(ok)
    while True:
        if ok in ("y", 'yes', 'ye'):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False

        retires = retires - 1

        if retires < 0:
            raise ValueError("valid User response")

        print(reminder)



if __name__ == '__main__':
    ask_ok("y")


