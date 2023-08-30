module SumOfDigits where
    sumOfDigits n 
    	| n < 10 = n
    	| (div n 10) /= 0 = (mod n 10) + sumOfDigits (div n 10)   