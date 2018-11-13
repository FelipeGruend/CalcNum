// 6) Secante; f(x) = x 2 - 2; x0=0 e x1=1; precisão = 0.001
#include <stdio.h>
#include <math.h>

#define E 0.001
#define X0 0.0
#define X1 1.0
#define K 100000

long double f(long double x){
	
	return (x*x)-2;
	
}


int main(){
	
	long double x2, x1, x0;
	int k;
	
	x0 = (long double)X0;
	x1 = (long double)X1;	
	k = (int)K;

	if( (fabs(f(x0))) < E ){
		x2 = x0;
		printf("%Le\n", x2);
		return 0;
	}

	if( (fabs(f(x1))) < E ){
		x2 = x1;
		printf("%Le\n", x2);
		return 0;
	}

	if( (fabs(x1-x0)) < E ){
		x2 = x1;
		printf("%Le\n", x2);
		return 0;
	}

	
	for (int i=0; i<k; i++){
		x2 = (x0*f(x1) - x1*f(x0)) / (f(x1) - f(x0));
		
		if( (fabs(f(x2))) < E ){
			printf("%Le\n", x2);
			return 0;
		}

		if( (fabs(x2-x1)) < E ){
			printf("%Le\n", x2);
			return 0;
		}
		
		x0 = x1;
		x1 = x2;
	}

	printf("%Le\n", x2);
	return 0;
	
}
