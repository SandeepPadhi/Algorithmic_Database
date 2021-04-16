# Python3 program to find the smallest
# twin in given range
import random

# Iterative Function to calculate
# (a^n)%p in O(logy)
def power(a, n, p):
	
	# Initialize result
	res = 1
	
	# Update 'a' if 'a' >= p
	a = a % p
	
	while n > 0:
		
		# If n is odd, multiply
		# 'a' with result
		if n % 2:
			res = (res * a) % p
			n = n - 1
		else:
			a = (a ** 2) % p
			
			# n must be even now
			n = n // 2
			
	return res % p
	
# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def isPrime(n, k):
	
	# Corner cases
	if n == 1 or n == 4:
		return False
	elif n == 2 or n == 3:
		return True
	
	# Try k times
	else:
		for i in range(k):
			
			# Pick a random number
			# in [2..n-2]	
			# Above corner cases make
			# sure that n > 4
			a = random.randint(2, n - 2)
			
			# Fermat's little theorem
			if power(a, n - 1, n) != 1:
				return False
				
	return True
			
# Driver code
k = 3
if isPrime(11, k):
print("true")
else:
print("false")

if isPrime(15, k):
print("true")
else:
print("false")

# This code is contributed by Aanchal Tiwari
