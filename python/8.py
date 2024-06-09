"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    n = int(input("정수 n을 입력하세요: "))

    # 1부터 n까지의 합 구하기
    sum_of_integers = sum(range(1, n + 1))
    print(sum_of_integers)

    # n! 구하기
    factorial_result = factorial(n)
    print(factorial_result)

    # 이곳에 코드를 작성해주세요!


if __name__ == '__main__':
    main()
