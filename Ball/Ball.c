#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#define MAX 10

// crated first varibel
int model_movment, x_ball, y_ball , TIME_CHANGE , TIME = 210000;

void strat_ball(int *ptrx , int *ptry , int *ptrmod){
	/*
	 * created ball on the random of space
	 * ball can bie faster or slower
	 * ptrmod is 4 model:
	  		     up_left     up_right

	  			      o

	  	           down_left    down_right
	 */
	*ptrx = rand() % MAX;
	*ptry = rand() % MAX;
	*ptrmod = rand() % 4;
	TIME_CHANGE = rand() % 2;

	if(TIME_CHANGE == 0)
		TIME_CHANGE = 2000;
	else
		TIME_CHANGE = -1000;


}

void ball_movment(int *ptrmodel , int *ptrx , int *ptry){
	//we need crating draw function for showing ball
	void draw(int *ptrx , int *ptry);
	//ball what is have a model now?
	//this is like a python version. so first time you need reading python version
	//python version is ez then logic
	switch(*ptrmodel){
		case 0:
			if(*ptrx == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry < MAX-1){
					*ptrx = *ptrx+1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME );
				}
			}
			if(*ptry == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx > 0){
					*ptrx = *ptrx-1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if(*ptrx == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry > 0){
					*ptry = *ptry-1;
					*ptrx = *ptrx-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx < MAX-1){
					*ptrx=*ptrx+1;
					*ptry=*ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if((*ptrx != 0 && *ptrx != MAX-1) && (*ptry != 0 && *ptry != MAX-1)){
				*ptrx=*ptrx+1;
				*ptry=*ptry-1;
				draw(ptrx , ptry);
				//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
			}
		break;
		case 1:
			if(*ptrx == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry > 0){
					*ptrx = *ptrx+1;
					*ptry = *ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d, time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx < MAX-1){
					*ptrx = *ptrx+1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if(*ptrx == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry < MAX-1){
					*ptry = *ptry+1;
					*ptrx = *ptrx-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx > 0){
					*ptrx=*ptrx-1;
					*ptry=*ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if((*ptrx != 0 && *ptrx != MAX-1) && (*ptry != 0 && *ptry != MAX-1)){
				*ptrx=*ptrx-1;
				*ptry=*ptry+1;
				draw(ptrx , ptry);
				//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
			}
		break;
		case 2:
			if(*ptrx == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry > 0){
					*ptrx = *ptrx+1;
					*ptry = *ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx < MAX-1){
					*ptrx = *ptrx+1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if(*ptrx == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry < MAX-1){
					*ptry = *ptry+1;
					*ptrx = *ptrx-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx > 0){
					*ptrx=*ptrx-1;
					*ptry=*ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if((*ptrx != 0 && *ptrx != MAX-1) && (*ptry != 0 && *ptry != MAX-1)){
				*ptrx=*ptrx-1;
				*ptry=*ptry-1;
				draw(ptrx , ptry);
				//printf("x = %d , y = %d ,time=%d\n" , *ptrx , *ptry , TIME);
			}
		break;
		case 3:
			if(*ptrx == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry < MAX-1){
					*ptrx = *ptrx+1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == 0){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx > 0){
					*ptrx = *ptrx-1;
					*ptry = *ptry+1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if(*ptrx == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptry > 0){
					*ptry = *ptry-1;
					*ptrx = *ptrx-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}
			if(*ptry == MAX-1){
				if((TIME_CHANGE ==  -1000 && TIME >= 1000) || (TIME_CHANGE == 2000 && TIME <=1100000))
					TIME += TIME_CHANGE;
				while(*ptrx < MAX-1){
					*ptrx=*ptrx+1;
					*ptry=*ptry-1;
					draw(ptrx , ptry);
					//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
				}
			}

			if((*ptrx != 0 && *ptrx != MAX-1) && (*ptry != 0 && *ptry != MAX-1)){
				*ptrx=*ptrx+1;
				*ptry=*ptry+1;
				draw(ptrx , ptry);
				//printf("x = %d , y = %d , time=%d\n" , *ptrx , *ptry , TIME);
			}
		break;



	}
	ball_movment(ptrmodel , ptrx , ptry);
}

void draw(int *ptrx , int *ptry){
	printf("\033[H");
	for(int i = 0; i < MAX ; i++){
		for(int j = 0; j < MAX ; j++){
			if(i == *ptry && j == *ptrx ){
				printf("o");
			}
			else
				printf(" ");

          }
		printf("\n");
	}
	usleep(TIME);

}

int main(){

	printf("\033[H");
	srand(time(0));

	int x_ball;
	int y_ball;

	strat_ball(&x_ball , &y_ball , &model_movment);
	ball_movment(&model_movment , &x_ball , &y_ball);
}
