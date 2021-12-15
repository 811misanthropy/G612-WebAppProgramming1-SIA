#include <stdio.h>
int main()
{

    int n, arr[50], ct=0;

    for(int i=0;i<n;i++)
        scanf(arr[i]);

    for(int i=0;i<n-1;i++)
        {
            if(arr[i]<=arr[i+1])
            {
                ct++;
            }
        }

    printf("%d ", ct);

    return 0;
}