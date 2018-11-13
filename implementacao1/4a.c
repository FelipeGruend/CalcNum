// 4.a) Falsa Posição; f(x) = 2,75x 3 +18x 2 -21x-12; [-1,0]; precisão = 0,01; i = 20
#include <stdio.h>
#include <math.h>

#define E 0.01
#define A -1.0
#define B 0.0
#define K 20

long double f(long double x){
	
	return 2.75*pow(x, 3) + 18*pow(x, 2) - 21*x - 12 ;
	
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

	if(fabs(f(a)) < E){
		x = a;
		printf("%Le\n", x);
		return 0;
	}

	if(fabs(f(b)) < E){
		x = b;
		printf("%Le\n", x);
		return 0;
	}
	
	M = f(a);
	
	for (int i=0; i<k; i++){
		x = (a*f(b) - b*f(a))/(f(b) - f(a));
		
		if (fabs(f(x)) < E){
			printf("%Le\n", x);
			return 0;
		}
		
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
