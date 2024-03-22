/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    int a,b;
    printf("시각입력(1-24)?");
    scanf("%d",&a);
    if(a>11) {
        a=a-12;
        printf("PM%d");
    }
    else {
        printf("AM%d");
    }

    return 0;
}