"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""
def main():
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def days_in_month(year, month):
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        else:
            return 31
        
    year = int(input("연도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))

    days = days_in_month(year, month)
    print(days)

if __name__ == "__main__":
    main()