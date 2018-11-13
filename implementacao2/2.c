// 2) Tangente; f(x) = e x cos(x) ; x0 = 1.3; precisão = 0.00001
#include <stdio.h>
#include <math.h>

#define E 0.00001
#define X0 1.3
#define K 100000

long double f(long double x){
	
	return pow(M_E, x) * cos(x);
	
}

long double f1(long double x){
	
	return pow(M_E, x) * (cos(x) - sin(x));

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
