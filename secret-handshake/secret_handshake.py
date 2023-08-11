def commands(binary_str):
    binary_str = list(binary_str)
    actions = []
    a = binary_str.pop()
    if a == "1":
        actions.append("wink")
    b = binary_str.pop()
    if b == "1":
        actions.append("double blink")
    c = binary_str.pop()
    if c == "1":
        actions.append("close your eyes")
    d = binary_str.pop()
    if d == "1":
        actions.append("jump")
    e = binary_str.pop()
    if e == "1":
        actions.reverse()
    return actions
