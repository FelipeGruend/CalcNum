// 1) Tangente; f(x) = cos(x) +2sen(x)+ x 2 ; x0 = 0; precisão = 0.001
#include <stdio.h>
#include <math.h>

#define E 0.001
#define X0 0.0
#define K 100000

long double f(long double x){
	
	return cos(x) + 2*sin(x) + pow(x, 2);
	
}

long double f1(long double x){
	
	return (2*x) - sin(x) + 2*cos(x);

}

int main(){
	
	long double x, x0;
	int k;
	
	x0 = (long double)X0;
	k = (int)K;

	if( (fabs(f(x0))) < E ){
		x = x0;
		printf("%Le\n", x);
		return 0;
	}
	
	for (int i=0; i<k; i++){
		x = x0 - f(x0)/f1(x0);
		
		if ((fabs(f(x)) < E) || (fabs(x-x0) < E)){
			printf("%Le\n", x);
			return 0;
		}

		x0 = x;
	}

	printf("%Le\n", x);
	return 0;
	
}
