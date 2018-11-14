import random as r
from itertools import product

class DFAError(Exception):
        pass

class DFA():
    def __init__(self, data=None):
        self.transitions = []
        self.accepting = []
        self.starting = 0
        self.as_str = ""
        self.pending_update = True
        
        if data == None:
            return
        if type(data) is str:
            self.set_state(data)
        elif type(data) is int:
            self.transitions = [[i, i] for i in range(data)]
            self.accepting = [False for i in range(data)]
        else:
            raise DFAError(f"Bad value given in initalization: Expected type str or int, got {type(data)} instead")
        
    def __repr__(self):
        self.update_as_str()
        return self.as_str

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.transitions)

    def __eq__(self, other):
        self.update_as_str()
        if type(other) is DFA:
            return self.as_str == other.as_str
        else:
            return NotImplemented

    def __hash__(self):
        self.update_as_str()
        return hash(self.as_str)

    def change(self, transition=None, accepting=None, starting=None):
        if transition != None:
            if type(transition) is tuple and len(transition) == 3:
                self.transitions[transition[0]][transition[1]] = transition[2]
            else:
                raise DFAError(f"Bad value in change(): transition should be a len 3 tuple, not {transition}")

        if accepting != None:
            if type(accepting) is list:
                self.accepting = [True if i in accepting else False for i in range(len(self))]
            elif type(accepting) is int:
                self.accepting[accepting] = not self.accepting[accepting]
            else:
                raise DFAError(f"Bad value in change(): accepting should be an int or a list, not {accepting}")

        if starting != None:
            if type(starting) is int and starting >= 0 and starting < len(self):
                self.starting = starting
            else:
                raise DFAError(f"Bad value in change(): starting should be an int within range, not {starting}")

        if transition == None and accepting == None and starting == None:
            return
        self.pending_update = True

    def test_str(self, s):
        cur_state = self.starting
        for c in s:
            cur_state = self.transitions[cur_state][int(c)]
        return self.accepting[cur_state]

    def set_state(self, str_val):
        if self.error_check(str_val):
            raise DFAError(f"Bad input given: {str_val}")
        self.as_str = str_val
        str_val = str_val.split(";")
        self.accepting = [True if i[0] == "*" else False for i in str_val]
        self.starting = [i for i, j in enumerate(str_val) if j[-1] == "-"][0]
        self.transitions = [[int(value.strip("*-")) for value in states.split(",")] for states in str_val]
        self.pending_update = False

    def error_check(self, s):
        for item in s.split(";"):
            if item.count(",") != 1:
                return True
            for c in item:
                if c not in "1234567890,;*-":
                    return True
                if c == "*" and item[0] != c:
                    return True
                if c == "-" and item[-1] != c:
                    return True

    def update_as_str(self):
        if not self.pending_update:
            return
        self.as_str = ";".join(["{}{},{}{}" \
        .format('*' if self.accepting[s] else '', i[0], i[1], '-' if self.starting == s else '') \
        for s, i in enumerate(self.transitions)])

    def formatted_string(self):
        return f"Starting state: {self.starting}\n" \
        f"Accepting states: {[i for i, j in enumerate(self.accepting) if j]}\n" \
        f"Transition table:\n{chr(10).join([f'{s}: {i}' for s, i in enumerate(self.transitions)])}"

    @staticmethod
    def all_strings(sigma, w):
        iterator = product(sigma, repeat=w)
        for item in iterator:
            yield "".join(item)

    @staticmethod
    def random(n):
        if type(n) is not int:
            raise DFAError(f"Expected int as parameter for random(), not {n}")
        rand_state = lambda: r.randrange(0, n)

        m = DFA(n)
        m.starting = rand_state()
        m.accepting = [True if r.randint(0, 1) else False for i in range(n)]
        m.transitions = [[rand_state(), rand_state()] for i in range(n)]
        return m


# m1 = DFA("*1,2;3,0;3,1-;0,0")
# print(m1)
# m1.change(transition=(0, 0, 0), accepting=[0, 1], starting=1)
# print(m1)

# m2 = DFA(4)
# print(m2.formatted_string())
# print(m2)

# m3 = DFA.random(4)
# print(m3.formatted_string())
# print(m3)

# m4 = DFA(4)
# m4.change(accepting=0)
# s = "0101010101100101100"
# print(m4.test_str(s))

# m5 = DFA.random(4)
# print(m5)
# m5.change(accepting=[2, 3])
# print(m5)
# m5.change(accepting=[])
# print(m5)

# print(list(DFA.all_strings(["0", "1"], 5)))