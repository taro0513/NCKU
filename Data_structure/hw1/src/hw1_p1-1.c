#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 1000

int priority(char operator){
    switch (operator){
        case '+': case '-': return 1;
        case '*': case '/': return 2;
        default : return 0;
    }
}

void infix_to_postfix(const char* infix, char* postfix){
    char stacks[MAX_STACK_SIZE] = {0};
    int i, j=0, top=0;
    for(i = 0, j=0, top=0;infix[i] != '\0'; i++) 
        switch(infix[i]) { 
            case '(':
                stacks[++top] = infix[i]; 
                break; 
            case '+': case '-': case '*': case '/': 
                while(priority(stacks[top]) >= priority(infix[i])){
                    postfix[j++] = stacks[top--];
                }
                stacks[++top] = infix[i];
                break;
            case ')': 
                while(stacks[top] != '(') {
                    postfix[j++] = stacks[top];
                    stacks[top--] = 0;
                } 
                stacks[top--] = 0;
                break; 
            default:
                postfix[j++] = infix[i];

        }
    while(top > 0) postfix[j++] = stacks[top--];
}


int main(){
    char infix[MAX_STACK_SIZE], postfix[MAX_STACK_SIZE];
    scanf("%s", infix);
    infix_to_postfix(infix, postfix);
    printf("%s\n", postfix);
    return 0;
}