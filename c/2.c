/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    // 이곳에 코드를 작성해주세요!
    int age;

    printf("나이를 입력하세요: ");
    int result = scanf("%d", &age);

    if (result != 1) {
        printf("유효한 나이를 입력하세요.\n");
        return 1;
    }
     printf("입력된 나이: %d\n", age);

     if (age >= 61) {
        printf("DISCOUNT\n");
    }
    
     printf("BOARD\n");

    return 0;
}