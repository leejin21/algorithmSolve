#include <stdlib.h> // atoi, rand, qsort, malloc
#include <stdio.h>
#include <assert.h> // assert
#include <time.h> //time

#define RANGE 10000


void change(int * pointer){
    // 함수 인자로 포인터 생성해 버리기
    *pointer = 3;               // 포인터가 가리키는 number에 3 저장하기
}

int main(void){
    int number = 2;
    printf("%d\n", number);
    change(&number);            // number의 주소 보냄
    printf("%d\n", number);
}

