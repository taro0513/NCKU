#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LENGTH 100000
#define MAX_STACK_SIZE 1000

void postfix_to_prefix(const char*, char*);
int is_operator(const char);

int main(int argc, char * argv[]){
	char postfix[MAX_STRING_LENGTH] = {0};
	char prefix[MAX_STRING_LENGTH] = {0};
	scanf("%s", postfix);
	postfix_to_prefix(postfix, prefix);
	printf("%s", prefix); 
	return 0;
}

void postfix_to_prefix(const char* postfix, char* prefix){
	char temp[MAX_STACK_SIZE] = {0};
	char stacks[MAX_STACK_SIZE] = {0};
	int len = strlen(postfix);
	int i, p, top;
	for(i=len-1, p=0, top=0; i>=0; i--){
		if (is_operator(postfix[i])){
			stacks[++top] = postfix[i];
		}
		else{
			temp[p++] = postfix[i];
			while((top != -1) && (stacks[top] == ';')){
				top--;
				temp[p++] = stacks[top--];
			}
			stacks[++top] = ';';
		}
	}
	len = p - 1;
	int index = 0;
	while(temp[index] != '\0'){
		prefix[len--] = temp[index++];
	}
	
	
}

int is_operator(char ops){
	switch(ops){
		case '+': case '-': case '*': case '/':
			return 1;
	}
	return 0;
}