package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	sqrtN := int(math.Sqrt(float64(n)))
	for i := 2; i <= sqrtN; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func isCaboose(n int) bool {
	for i := 1; i <= n; i++ {
		x := i*i - i + 41
		if !isPrime(x) {
			return false
		}
	}
	return true
}

func caboosePrimeRatio(n int) float64 {
	primeCount := 0
	for i := 1; i <= n; i++ {
		x := i*i - i + 41
		if isPrime(x) {
			primeCount++
		}
	}
	return float64(primeCount) / float64(n)
}

func main() {
	n := 100
	for i := 1; i < n; i++ {
		if isCaboose(i) {
			fmt.Printf("%d is Caboose\n", i)
		} else {
			fmt.Printf("%d is not Caboose\n", i)
		}
		fmt.Printf("Caboose ratio for %d is %.2f\n", i, caboosePrimeRatio(i))
	}
}
