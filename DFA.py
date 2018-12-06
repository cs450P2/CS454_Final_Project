import random as r
from itertools import product
from math import factorial

FILENO = 0
SFILENO = 0

T = [[[[], []], [[], []]], [[[], []], [[], []]]]

class DFAError(Exception):
        pass

class DFA():
    def __init__(self, data=None):
        self.transitions = []
        self.accepting = []
        self.starting = 0
        self.as_str = ""
        self.pending_update = True
        self.T =[for]
        
        
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
    
            
    # Correct function to help get the score of the DFA
    def Correct(self, k)
        T1 = int
        T2 = int
        T3 = int
        T4 = int
        # L1 = { w | #1s(w) > #0s(w) }
        for f in self.accepting:
            for m in range(1,k+1):
                p = self.transitions[self.starting][0]
                q = f
                l = k-1
                T1 += T[p, q, l-1, m-1] + T[p, q, l, m+1]
        for a not in self.accepting:
            for m in range(0,-k-1):
                p = self.transitions[self.starting][0]
                q = a
                l = k-1
                T2 += T[p, q, l-1, -(m-1)] + T[p, q, l, -(m+1)]
        # L2 = { w | #1s(w) == #0s(w) }
        for f in self.accepting:
            p = self.transitions[self.starting][1]
            q = f
            l = k-1
            T3 += T[p, q, l, -1]
        for a not in self.accepting:
            p = self.transitions[self.starting][0]
            q = a
            l = k-1
            T4 += T[p, q, l, 1]
        # Sum of the two languages
        return T1+T2+T3+T4
        

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

# Generate T table
def GenT():
    choose = lambda p,q: (factorial(p)) / ((factorial(q)) / (factorial(p-q)))
    for a in range(0, (k/2)+1): # base case for m
        m = k - (2 * a)
        T[p,q,l,m] = choose(k, a)
        T[p,q,l,-m] = choose(k, a)

    

# Get the two DFAs with format (original DFA M and locally changed DFA N) & compare them
#def CorrectState(M, L, K):
#   Get the scores of the two DFAs, M & L, via Correct(DFA, # number of states)/ 2^k
#   With M being the original DFA and L being the DFA with local change
#   if ( (M.Correct(k)) <= (L.Correct(k))):
#   | if (Score of state in M <= Score of state in L):
#       L.CopyDFA(M) copy over M into L
#       return L
#   else return M
#   OR
#   if (file with DFA M score <= file with DFA L score):
#       L.CopyDFA(M)
#   else return



# Reading in input from STDIN piped until /n
# for lines in sys.stdin
#     stripped = lines.strip()
#     if not stripped: break
#     result.append(stripped)
# m1 = DFA(result)

# OR

# list(DFA.all_strings(["0", "1"], 5))
# m1 = DFA(list[random int here])

# m2.CopyDFA(m1)
# m2.change(do local change at the start)
# loop here for automated change:
#   m3 = Compare(m1, m2, k) -> k being the length of the string
#   if m3.DfaChecker(m1): // m3 == m1
#       m2.CopyDFA(m3)
#       m2.change(advance to next state and change it)
#   else: // m3 == m2
#       m1.CopyDFA(m3)
#       m2.change(advance to next state and change it)
#
# print()

m1 = DFA("*1,2;3,0;3,1-;0,0")
print(m1)
print(m1.formatted_string())
m1.change(transition=(0, 0, 0), accepting=[0, 1], starting=1)
print(m1)

#-- Creates a DFA with 4 states that loop on each other
#   has 0 as the start state, but has no accepting state
# m2 = DFA(4)
# print(m2.formatted_string())
# print(m2)

#-- Randomly generate DFA with 4 states do 7
#m3 = DFA.random(4)
#print(m3.formatted_string())
#print(m3)

#-- Check if a given string is valid in the DFA
# m4 = DFA(4)
# m4.change(accepting=0)
# s = "0101010101100101100"
# print(m4.test_str(s))

#-- Randomly generate a DFA with 4 states and change the accepting state
# m5 = DFA.random(4)
# print(m5)
# m5.change(accepting=[2, 3])
# print(m5)
# m5.change(accepting=[])
# print(m5)

# print(list(DFA.all_strings(["0", "1"], 5)))
