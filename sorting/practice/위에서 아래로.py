# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
data = []
for _ in range(n):
    data.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
data.sort(reverse=True)

# 정렬이 수행된 결과를 출력
for i in range(len(data)):
    print(data[i], end=' ')
