def arithmetic_arranger(arithmetic_problems, answers=False):
    if len(arithmetic_problems) <= 5:
        if testsequence(arithmetic_problems):
            calculate(arithmetic_problems, answers)
    else:
        print("Error: Too many problems.")


def test_operand(teststring):
    counter = 0
    for string in teststring:
        if string.split()[1] in "+-":
            counter += 1
        else:
            print("Error: Operator must be '+' or '-'.")
    return len(teststring) == counter


def test_for_number(teststrings):
    counter = 0
    for teststring in teststrings:
        if teststring.split()[0].isnumeric() and teststring.split(
        )[2].isnumeric():
            counter += 1
        else:
            print("Error: Numbers must only contain digits.")
    if len(teststrings) == counter:
        return True
    else:
        return False


def test_for_lenght(teststrings):
    counter = 0
    for teststring in teststrings:
        if len(teststring.split()[0]) <= 4 and len(teststring.split()[2]) <= 4:
            counter += 1
        else:
            print("Error: Numbers cannot be more than four digits.")
    return len(teststrings) == counter


def testsequence(teststrings):
    return test_operand(teststrings) and test_for_number(
        teststrings) and test_for_lenght(teststrings)


def calculate(problems, answers):
    first_line = ''
    second_line = ''
    underscore = ''
    solution = ''
    delimiter = ' '
    under_characters = '-'

    for value in makedata(problems):
        space = value['length'] - len(value['first'])
        tmp_value = value['first']
        first_line += f'{space * delimiter}{tmp_value}{4 * delimiter}'

        operation = value['operation']
        tmp_value = value['second']
        space = value['length'] - len(value['second']) - 1
        second_line += f'{operation}{space * delimiter}{tmp_value}{4 * delimiter}'

        underscore_lenght = value['length']
        underscore += f'{underscore_lenght * under_characters}{4 * delimiter}'

        if answers:
            first = int(value['first'])
            second = int(value['second'])
            if value['operation'] == '+':
                answer = int(first) + int(second)
            else:
                answer = int(first) - int(second)
            answer_len = len(str(answer))
            space = value['length'] - answer_len
            solution += f'{space * delimiter}{answer}{4 * delimiter}'
    print(first_line)
    print(second_line)
    print(underscore)
    print(solution)


def makedata(problems):
    data_array = []
    for problem in problems:
        data = problem.split()
        data_value = {
            'first': data[0],
            'second': data[2],
            'operation': data[1],
            'length': find_longer(data)
        }
        data_array.append(data_value)
    return data_array


def find_longer(data):
    longer = len(data[0]) + 2 if len(data[0]) > len(
        data[2]) else len(data[2]) + 2
    return longer
