import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures = sorted(lectures, key = lambda x:(x[0], x[1]))

room = []
heapq.heappush(room, lectures[0][1])
for i in range(1, N):
    # 3시(시작 5시 종료) 수업들어가야돼 -> 가장 먼저 끝나는 강의가 2시 -> 이 강의실 사용 가능
    if lectures[i][0] >= room[0]:
        heapq.heappop(room)

    # 3시(시작 5시 종료) 수업들어가야돼 -> 가장 먼저 끝나는 강의가 6시 -> 이 강의실 사용 불가
    heapq.heappush(room, lectures[i][1])

print(len(room))


# # 시간 초과
# N = int(input())
# lectures = [list(map(int, input().split())) for _ in range(N)]
# lectures = sorted(lectures, key = lambda x:(x[0], x[1]))
# print(lectures)

# answer = 1
# end_times = [0] # 각 강의실의 마지막 수업이 끝나는 시간 저장

# for start_time, end_time in lectures:
#     # 모든 강의실의 수업이 끝나는 시간보다 현재 수업이 시작하는 시간이 더 빠르면 새 강의실 필요
#     if start_time < min(end_times):
#         end_times.append(end_time)
#         answer += 1
#     # 현재 수업이 시작하는 시간보다는 이전 강의의 끝나는 시간이 빠르고 그 중 최대한 늦게 끝나는 강의실 찾으면 좋을 듯
#     else:
#         for i in range(len(end_times)):
#             if start_time >= end_times[i]:
#                 end_times[i] = end_time
#                 break

# print(answer)