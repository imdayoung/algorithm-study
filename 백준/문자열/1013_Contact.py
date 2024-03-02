import sys


def is_pattern(string):
    while len(string) > 0:
        if string[:3] == '100':
            string = string[3:]
            while len(string) > 0 and string[0] == '0':
                string = string[1:]

            if len(string) == 0:
                return False
            
            string = string[1:]
            
            while len(string) > 0 and string[0] == '1':
                if len(string) >= 3 and string[1] == '0' and string[2] == '0':
                    break
                else:
                    string = string[1:]
        
        elif string[:2] == '01':
            string = string[2:]
        
        else:
            return False
        
    return True


answers = []
T = int(sys.stdin.readline())
# pattern = "(100+1+ | 01)+"

for _ in range(T):
    wave = input()
    if is_pattern(wave):
        answers.append("YES")
    else:
        answers.append("NO")

for answer in answers:
    print(answer)