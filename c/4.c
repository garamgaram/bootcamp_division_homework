/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() 
    // 이곳에 코드를 작성해주세요!
{
    int score = 0;

    printf("점수를 입력하세요 : ");
    scanf_s("%d", &score);

    if (score >= 90 && score <= 100) {
        printf("%d점은 A 학점입니다.\n", score);
    }else if (score >= 80) {
        printf("%d점은 B 학점입니다.\n", score);
    }else if (score >= 70) {
        printf("%d점은 C 학점입니다.\n", score);
    }else if (score >= 60) {
        printf("%d점은 D 학점입니다.\n", score);
    }else {
        printf("%d점은 F 학점입니다.\n", score);
    }
    
    return 0;
}