######################################################

# python3

# removed global index

def are_matching(left, right):
    # this function checks if both left and right brackets are matching
    # returns true if they are matching and false if they are not

    if left == '(':
        if right != ")":
            return False
    else:
        return True
    if left == '{':
        if right != "}":
            return False
    else:
        return True
    if left == '[':
        if right != "]":
            return False
    else:
        return True


def find_match(text):

    bracket_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # when you encounter an open bracket, push it to your stack
            bracket_stack.append(next)

        if next in ")]}":
            # checks if right bracket with no left
            if len(bracket_stack) == 0:
                return i
            # bracket_stack[-1] replaced with bracket_stack.pop()
            elif are_matching(bracket_stack.pop(), next):
                pass
            else:
                return i

    if len(bracket_stack) == 0:
        return "Success"
    else:
        return False

        # When you encounter a right bracket,
        # you need to compare and see if it has a matching left bracket
        # return the index when you encounter the error
        # take into consideration the special cases: right bracket with no
        # left brackets encountered before, or the input was processed and
        # the stack is not empty


def main():
    text = input()

    # Forces user to input something
    while not text:
        print("please enter any character to continue:")
        text = input()

    # If there is no error, print success
    # if there is an error, print the index return from the above function
    print(find_match(text))

if __name__ == "__main__":
    main()
########################################################
