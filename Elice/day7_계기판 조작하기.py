def find_min_number(N, K):
  """
  N보다 크고 서로 다른 K개의 숫자로 이루어진 수의 최솟값을 찾는 함수

  Args:
    N: 주어진 수 (1 <= N <= 10^7)
    K: 사용할 숫자 개수 (1 <= K <= 10)

  Returns:
    N보다 크고 서로 다른 K개의 숫자로 이루어진 수의 최솟값
  """

  # N보다 큰 K개의 숫자를 저장할 리스트
  digits = []

  # N의 각 자리수를 리스트에 추가
  for num in str(N):
    digits.append(int(num))

  # 리스트를 오름차순으로 정렬
  digits.sort()

  # 최솟값을 만들기 위해 가장 작은 숫자를 제외하고 K개의 숫자를 선택
  for i in range(1, K):
    digits.append(digits[i] + 1)

  # digits 리스트를 문자열로 변환하여 최종 숫자를 만들어 반환
  return int("".join(map(str, digits)))

# 예시 입력값
N = 100000
K = 3

# 함수 실행 및 결과 출력
min_number = find_min_number(N, K)
print(min_number)
