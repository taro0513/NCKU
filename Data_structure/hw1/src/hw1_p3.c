#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TREE_SIZE 1000000
#define MAX_UNION_SIZE 1000000
#define MAX_OPERATIONS_LENGTH 10

typedef struct DisjointSet {
	int parent;
	int height;
} ds;

typedef struct Edge{
	int source;
	int destination;
	long long int cost;
} edge;

int edge_compare(const void*, const void*);

long long int kruskal(edge*, const int, const int);

void dsinitial(ds*, int);

void dsunion(ds*, int, int);

int dssame(ds*, int, int);
	
int dsfind(ds*, int);

int main(int argc, char* argv[]) {
    int V, E;
    scanf("%d %d", &V, &E);
    // edge ee[MAX_TREE_SIZE];
    edge* ee = (edge*)malloc(E*sizeof(edge));
    for(int i=0; i<E; i++){
    	scanf("%d %d %lld", &ee[i].source, &ee[i].destination, &ee[i].cost);
    }
     
    long long int minimum_cost = 0;
    minimum_cost = kruskal(ee, V, E);
    printf("%lld", minimum_cost);
    return 0;
}

long long int kruskal(edge* ee, const int v, const int e){
	long long int cost = 0;
	qsort(ee, e, sizeof(edge), edge_compare);
	// ds DS[MAX_UNION_SIZE];
	ds* DS = (ds*)malloc(v*sizeof(ds));
	dsinitial(DS, v);
	for(int i=0; i<e; i++){
    	if(!dssame(DS, ee[i].source, ee[i].destination)){
    		dsunion(DS, ee[i].source, ee[i].destination);
    		cost += ee[i].cost;
    	}
    }

    
	return cost;
}

int edge_compare(const void* e1, const void* e2){
	edge* se1 = (edge *)e1;
	edge* se2 = (edge *)e2; 
	return se1->cost - se2->cost;
}

void dsinitial(ds* DS, int n){
	for(int o=0; o<n; o++){
		DS[o].parent = -1;
		DS[o].height = 0;
	}
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