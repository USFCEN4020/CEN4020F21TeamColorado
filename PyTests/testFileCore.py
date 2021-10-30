import builtins

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs

def makeMultiInput(inputs, idx=0):
    'inputs a collection of strings, to be returned one at a time'

   # closure on inputs and index
    def next_input(message=""):
        # nonlocal only in python3 similar to global but
        # for non local non global variables
        nonlocal idx
        if idx < len(inputs):
            idx = idx + 1
            return inputs[idx - 1]
        else:
            return ""

    return next_input