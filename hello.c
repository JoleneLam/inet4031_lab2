#include<stdio.h>

int main() {
	int a = 2;
	int b = 2;
	int c = a + b;
	
	printf("C says: Hello, World\n");
	printf("%d + %d = %d\n",a,b,c);
	
	char *listOfUsers[] = {"User1", "User2", "User2"};
	int users = sizeof(listOfUsers) / sizeof(listOfUsers[0]);

	for (int i = 0; i < users; i++) {
		printf("%s", listOfUsers[i]);
		if (i < users - 1) {
			printf(", ");
		}
	}
	printf("\n");
	return 0;
}
