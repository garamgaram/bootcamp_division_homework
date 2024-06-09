"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    score = int(input("점수를 입력하세요: "))

    if score >= 90:
        print("등급: A")
    elif score >= 80:
        print("등급: B")
    elif score >= 70:
        print("등급: C")
    elif score >= 60:
        print("등급: D")
    else:
        print("등급: F")

    # 이곳에 코드를 작성해주세요!


if __name__ == '__main__':
    main()
