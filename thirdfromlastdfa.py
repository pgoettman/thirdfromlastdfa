# This program will read binary strings and print 'accepted' if the third from last number is '1' or 'rejected' if it is a '0'

import sys


def main():
    print(one_in_third_from_last('101100101'))
    print(one_in_third_from_last('10111001'))


def one_in_third_from_last(s):
    # transitions represents our DFA for determining if 1 is the third from last number
    transitions = {('q0', '0'): 'q0', ('q0', '1'): 'q1', ('q1', '0'): 'q10', ('q1', '1'): 'q11',
                   ('q10', '0'): 'q100', ('q10', '1'): 'q101', ('q11', '0'): 'q110', ('q11', '1'): 'q111',
                   ('q100', '0'): 'q0', ('q100', '1'): 'q1', ('q101', '0'): 'q10', ('q101', '1'): 'q11',
                   ('q110', '0'): 'q100', ('q110', '1'): 'q101', ('q111', '0'): 'q110', ('q111', '1'): 'q111'}
    state = 'q0'
    for c in s:
        state = transitions[(state, c)]
    return 'accepted' if state == 'q100' or state == 'q101' or state == 'q110' or state == 'q111' else 'rejected'


if __name__ == '__main__':
    main()
