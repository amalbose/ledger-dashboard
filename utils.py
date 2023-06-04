def get_cur():
    return "₹"


def format_INR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)


def format_cur(val):
    sign = ""
    if val < 0:
        sign = "-"
    return get_cur() + " " + sign + format_INR(abs(val))
