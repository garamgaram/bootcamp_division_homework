/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    // 이곳에 코드를 작성해주세요!
{
    int i,n,sum=0;
    printf("1부터n까지의 합 계산\n");
    printf("정수n입력:");
    scanf("%d",&n);
    for(i=1;i<=n;i+=1)
      sum+=i;
    printf("1부터 %d까지의 합:%d\n",n,sum);
}
    return 0;
}