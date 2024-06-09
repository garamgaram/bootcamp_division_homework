"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    while True:
        n = int(input("양의 정수 n을 입력하세요: "))
        
        if n > 0:
            break
        else:
            print("양의 정수를 입력해야 합니다. 다시 입력하세요.")

    sum_of_integers = sum(range(1, n + 1))
    print(sum_of_integers)

    # 이곳에 코드를 작성해주세요!



if __name__ == '__main__':
    main()
