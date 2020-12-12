
correct_str = "(())"
incorrect_str = "(()()))"


def ifNestedParenthese(string):

    count_open = 0
    for i in string:
        if i == "(":
            count_open += 1
        elif i == ")":
            count_open -= 1
            if count_open < 0:
                return False
    return count_open == 0

print(ifNestedParenthese(correct_str))
print(ifNestedParenthese(incorrect_str))
