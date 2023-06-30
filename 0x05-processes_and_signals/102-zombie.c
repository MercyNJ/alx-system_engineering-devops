#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - An infinite loop helping the main function
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Function creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int count;
	pid_t child_pid;

	for (count = 0; count < 5; count++)
	{
		child_pid = fork();
		if (child_pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", child_pid);
	}

	infinite_while();
	return (0);
}
