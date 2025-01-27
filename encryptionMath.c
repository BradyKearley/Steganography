#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// Seed the random number generator once
void seed_random()
{
    srand(time(NULL));
}

void sieve_of_eratosthenes(long long limit, bool is_prime[])
{
    for (long long i = 0; i <= limit; i++)
    {
        is_prime[i] = true;
    }
    is_prime[0] = is_prime[1] = false;
    for (long long p = 2; p * p <= limit; p++)
    {
        if (is_prime[p])
        {
            for (long long i = p * p; i <= limit; i += p)
            {
                is_prime[i] = false;
            }
        }
    }
}

long long generate_prime(long long min_value, long long max_value)
{
    bool *is_prime = (bool *)malloc((max_value + 1) * sizeof(bool));
    if (is_prime == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    sieve_of_eratosthenes(max_value, is_prime);
    long long *primes = (long long *)malloc((max_value - min_value + 1) * sizeof(long long));
    if (primes == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    long long count = 0;
    for (long long p = min_value; p <= max_value; p++)
    {
        if (is_prime[p])
        {
            primes[count++] = p;
        }
    }

    long long result = primes[rand() % count];

    free(is_prime);
    free(primes);
    return result;
}

long long mod_inverse(long long a, long long m)
{
    long long m0 = m, x0 = 0, x1 = 1;
    if (m == 1)
    {
        return 0;
    }
    while (a > 1)
    {
        long long q = a / m;
        long long t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0)
    {
        x1 += m0;
    }
    return x1;
}
