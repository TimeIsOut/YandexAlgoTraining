n, k, m = map(int, input().split())
details = 0
while n >= k and k >= m:
    k_in_n, leftover = n // k, n % k
    m_in_k, leftover = k // m, leftover + k % m * k_in_n
    cur_det = k_in_n * m_in_k
    details += cur_det
    n = leftover
print(details)