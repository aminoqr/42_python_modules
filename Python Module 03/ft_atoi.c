#include <stdio.h>

int ft_atoi(char *str)
{
    int i = 0;
    int res = 0;
    int sign = 1;
    while(str[i] && (str[i] == ' ' || str[i] == '\t'))
    {
        i++;
    }
    if (str[i] == '+' || str[i] == '-')
    {
        if(str[i] == '-')
            sign *= -1;
        i++;
    }
    while(str[i] >= '0' && str[i] <= '9')
    {
        res = res * 10 + (str[i] - '0');
        i++;
    }
    return (res * sign);
}

int main()
{
    printf("%d\n", ft_atoi("    +123"));
    printf("%d\n", ft_atoi("    -123"));
    printf("%d\n", ft_atoi("    ++---+123asda"));
    printf("%d\n", ft_atoi("    asd123"));
}