// 2) Falsa Posição; f(x) = x 3 -9x+3 ; [0, 1]; precisão = 0.0005
#include <stdio.h>
#include <math.h>

#define E 0.0005
#define A 0.0
#define B 1.0
#define K 100000 // Definindo um número elevado porque não foi determinado máximo de iterações

long double f(long double x){
	
	return (x*x*x)-(9*x)+3;
	
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
	
}
