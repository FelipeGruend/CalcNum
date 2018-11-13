// 1) Bissecção; f(x) = x 3 -9x+5 ; [0.5, 1]; precisão = 0.01
#include <stdio.h>

#define E 0.01
#define A 0.5
#define B 1.0
#define K 5

long double f(long double x){
	
	return (x*x*x)-(9*x)+5;
	
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
