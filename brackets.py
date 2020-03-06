def is_correct(s: str) -> bool:
    """ Function that returns 1 if the sequence of brackets is correct.
    And returns 0 if the sequence of brackets is wrong.
    """
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    open_brackets = set(['{', '[', '('])
    stack = []

    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
            
        # if the stack is not empty and the closing bracket corresponds to the opening at the top of the stack
        elif stack and bracket == brackets[stack[-1]]:
            stack.pop()
        else:
            return False

    return stack == []
