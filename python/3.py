"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    hour = int(input("시간을 입력하세요 (0부터 23까지): "))

    if hour < 0 or hour > 23:
        print("잘못된 입력입니다. 시간은 0부터 23까지의 정수여야 합니다.")
        return

    if hour < 12:
        print("AM")
    else:
        print("PM")

    # 이곳에 코드를 작성해주세요!


if __name__ == '__main__':
    main()
