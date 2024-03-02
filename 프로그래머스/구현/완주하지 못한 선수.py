from collections import Counter

def solution(participant, completion):
    participant_count, completion_count = Counter(participant), Counter(completion)
    
    for i in participant_count:
        if participant_count[i] != completion_count[i]:
            return i