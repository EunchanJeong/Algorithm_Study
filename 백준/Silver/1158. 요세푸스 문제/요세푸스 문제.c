#include <stdio.h>
void josephus(int n1, int b, int c[], int del[]);
void print(int n1, int a[]);

/* ------------------------
이름 : 정은찬
학번 : 201513437

조세퍼스 순열 과제
-------------------------- */

int main()
{
	int num[5000];       // 원을 만들 인원을 저장하는 배열
	int delect[5000];    // 제거된 인원을 저장하는 배열

	int n;               // 원을 만들 인원수
	int m;				 // 제거되는 번째수  

	scanf("%d%d", &n, &m);

	josephus(n, m, num, delect);     // 인원을 조세퍼스순열로 제거하는 함수 호출

	print(n, delect);                // 제거된 인원을 저장한 배열 출력

	return 0;
}

/* ------------------------------------
인원들을 조세퍼스순열로 제거하는 함수

매개변수
* n1   : 원을 만들 인원수
* m1   : 제거되는 번째수
* num1 : 원을 만든 인원을 저장하는 배열
* del  : 제거되는 인원을 저장하는 배열
--------------------------------------- */
void josephus(int n1, int m1, int num1[], int del[])
{
	int index = 0;
	int count = 0;
	int a = 0;
	int i;

	// n1명으로 원을 만든다
	for (i = 1; i <= n1; i++)
	{
		num1[index++] = i;
	}

	index = -1;

	// 조세퍼스 순열로 인원 제거
	while (1)
	{
		while (1)
		{
			index++;

			if (index > n1-1)
			{
				index %= n1;
			}

			if (num1[index] == 0)
			{
				while (1)
				{
					index++;

					if (index > n1 - 1)
					{
						index %= n1;
					}

					if (num1[index] != 0)
					{
						break;
					}
				}
			}
			count++;

			if (count == m1)
			{
				del[a] = num1[index];
				a++;
				num1[index] = 0;
				count = 0;
				break;
			}
		}

		if (a == n1)
		{
			break;
		}
	}
}

/* 배열을 출력하는 함수 */
void print(int n1, int a[])
{
	int i;

	printf("<");

	for (i = 0; i < n1; i++)
	{
		if (i != n1 - 1)
		{
			printf("%d, ", a[i]);
		}
		else
		{
			printf("%d>\n", a[i]);
		}
	}
}