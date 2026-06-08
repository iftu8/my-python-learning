import random
import time

def matrix_mult(A, B):
    """2x2 ম্যাট্রিক্স গুণের অ্যাডভান্সড ফাংশন"""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_power(M, p):
    """ম্যাট্রিক্স এক্সপোনেনসিয়েশন (Time Complexity: O(log N))"""
    res = [[1, 0], [0, 1]]
    base = M
    while p > 0:
        if p % 2 == 1:
            res = matrix_mult(res, base)
        base = matrix_mult(base, base)
        p //= 2
    return res

def fast_fibonacci(n):
    """ম্যাট্রিক্স এক্সপোনেনসিয়েশন ব্যবহার করে যেকোনো পজিশনের ফিবোনাচি নম্বর বের করা"""
    if n == 0: return 0
    M = [[1, 1], [1, 0]]
    res = matrix_power(M, n - 1)
    return res[0][0]

def miller_rabin_primality_test(n, k=5):
    """Miller-Rabin Primality Test: বিশাল বড় সংখ্যার মৌলিকত্ব প্রমাণের হ্যাকিং লেভেল অ্যালগরিদম"""
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    print("=== ADVANCED MATHEMATICAL COMPUTATION ENGINE ===\n")
    
    # ১. ফিবোনাচি সিকোয়েন্স (ম্যাট্রিক্স লজিক)
    n = 100000
    print(f"[*] Calculating the {n}-th Fibonacci number...")
    start_time = time.time()
    fib_result = fast_fibonacci(n)
    end_time = time.time()
    
    print(f"[+] Done in {end_time - start_time:.5f} seconds!")
    print(f"[+] The result has {len(str(fib_result))} digits! (Too large to print completely)\n")

    # ২. মিলার-র‍্যাবিন প্রাইম টেস্ট
    massive_number = 10**100 + 267 # একটি ১০১ ডিজিটের বিশাল মৌলিক সংখ্যা
    print(f"[*] Testing if a 101-digit number ({massive_number}) is a Prime Number...")
    is_prime = miller_rabin_primality_test(massive_number)
    print(f"[+] Is it prime? {'YES! It is a mathematically proven prime.' if is_prime else 'NO'}")
    
    print("\n================================================")
