#include <stdio.h>
int main(void) {
	// your code goes here
	int row, col;
	int i, j;
	int t,b,l,r;
	printf("Enter rows\n");
	scanf("%d", &row);
	printf("enter cols\n");
	scanf("%d", &col);
	printf("rows : %d and cols : %d\n", row,col);
	int s[row][col];
	printf("enter array elems\n");
	for(i=0; i<row; i++)
	{
		printf("row %d\n", i);
		for(j=0; j<col; j++)
		{
			scanf("%d", &s[i][j]);
		}
	}
	for(i=0; i<row; i++)
	{
		printf("row %d\n", i);
		for(j=0; j<col; j++)
		{
			printf("%d", s[i][j]);
		}
		printf("\n");
	}
	t=0;
	b= row-1;
	l=0;
	r=col-1;
	int dir = 0;
	printf("l: %d r: %d, t: %d, b: %d\n", l, r, t, b);
	int x, y;
	printf("\n");
	while(l<=r && t<=b)
	{
		if(dir==0)
		{
			printf("left to right\n");
			for(x=l; x<=r; x++)
			{
				printf("%d", s[t][x]);
			}
			t++;
			printf("l: %d r: %d, t: %d, b: %d\n", l, r, t, b);
		}
		else if(dir==1)
		{
			printf("top to bottom\n");
			for(y=t; y<=b; y++)
			{
				printf("%d", s[y][r]);
			}
			r--;
			printf("l: %d r: %d, t: %d, b: %d\n", l, r, t, b);
		}
		else if(dir==2)
		{
			printf("right to left\n");
			for(x=r; x>=l; x--)
			{
				printf("%d", s[b][x]);
			}
			b--;
			printf("l: %d r: %d, t: %d, b: %d\n", l, r, t, b);
		}
		else if(dir==3)
		{
			printf("bottom to top\n");
			for(y=b;y>=t; y--)
			{
				printf("%d", s[y][l]);
			}
			l++;
			printf("l: %d r: %d, t: %d, b: %d\n", l, r, t, b);
		}
		printf("\n");
		dir = (dir+1)%4;
	}
	
}
