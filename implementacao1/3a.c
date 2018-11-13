// 3.a) Falsa Posição; f(x) = e x -3x; [0,1]; i = 17
#include <stdio.h>
#include <math.h>

#define E -INFINITY // definindo precisão como infinito negativo, porque só foi especificado máx de iiterações
#define A 0.0
#define B 1.0
#define K 17

long double f(long double x){
	
	return pow(M_E, x) - 3*x ;
	
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
