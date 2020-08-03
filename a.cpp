#include <bits/stdc++.h>
using namespace std;
int main()
{
    char s[50];
    gets(s);
    while( s[0] == ' ' ) strcpy(&s[0], &s[1]);
    while( s[ strlen(s)-1 ] == ' ') s[ strlen(s)-1 ] = '\0';
    int i;
    for(i = 0; i < strlen(s); i++)
    {
        if( s[i] == ' ' && s[i+1] == ' ')
        {
            strcpy(&s[i], &s[i+1]);
            i--;
        }
    }
    puts(s);
    return 0;
}

