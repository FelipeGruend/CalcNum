// 3.c) Bissecção; f(x) = e x -3x; [0,1]; i = 30
#include <stdio.h>
#include <math.h>

#define E -INFINITY
#define A 0.0
#define B 1.0
#define K 30

long double f(long double x){
	
	return pow(M_E, x) - 3*x;
	
}


int main(){
	
	long double x, a, b, M;
	int k;
	
	a = (long double)A;
	b = (long double)B;
	k = (int)K;
	
	if( (b-a) < E){
		x = (a+b)/2;
		printf("%Le\n", x);
		return 0;
	}
	
	M = f(a);
	
	for (int i=0; i<k; i++){
		x = (a+b)/2;
		if ( (M*f(x)) > 0 )
			a = x;
		else
			b = x;

		if ((b-a) < E){
			x = (a+b)/2;
			printf("%Le\n", x);
			return 0;
		}
	}

	printf("%Le\n", x);
	return 0;
	
}
