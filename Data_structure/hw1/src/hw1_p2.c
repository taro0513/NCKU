#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_UNION_SIZE 100000
#define MAX_OPERATIONS_LENGTH 10

typedef struct DisjointSet {
	int parent;
	int height;
} ds;

void dsunion(ds*, int, int);

int dssame(ds*, int, int);
	
int dsfind(ds*, int);

int main(int argc, char* argv[]) {
	int testcase = 0;
	int i, n, o, ops;
	scanf("%d", &testcase);
	for(i=0; i<testcase; i++){
		n=0, ops=0;
		scanf("%d %d", &n, &ops);
		ds DS[MAX_UNION_SIZE];
		for(o=0; o<n; o++){
			DS[o].parent = -1;
			DS[o].height = 0;
		}
		for(o=0; o<ops; o++){
			char operations[MAX_OPERATIONS_LENGTH];
			int index1;
			scanf("%s %d", operations, &index1);
			
			if (strcmp(operations, "union") == 0){
				int index2;
				scanf("%d", &index2);
				dsunion(DS, index1, index2);
			}
			else if (strcmp(operations, "same") == 0){
				int index2;
				scanf("%d", &index2);
				if (dssame(DS, index1, index2)){
					printf("true\n");
				}
				else{
					printf("false\n");
				}
			}
			else{
				printf("%d\n", dsfind(DS, index1));
			}
		}
	}
	return 0;
}

void dsunion(ds* DS, int index1, int index2){
	int root1 = dsfind(DS, index1);
	int root2 = dsfind(DS, index2);
	
	if (root1 != root2){
		if (DS[root1].height < DS[root2].height){
			DS[root1].parent = root2;
		}
		else if (DS[root1].height > DS[root2].height){
			DS[root2].parent = root1;
		}
		else{
			DS[root2].parent = root1;
			DS[root1].height ++;
		}
	}
}

int dssame(ds* DS, int index1, int index2){
	return dsfind(DS, index1) == dsfind(DS, index2);
}

int dsfind(ds* DS, int index){
	if (DS[index].parent < 0){
		return index;
	}
	else{
		int root_index = dsfind(DS, DS[index].parent);
		DS[index].parent = root_index;
		return root_index;
	}
}
