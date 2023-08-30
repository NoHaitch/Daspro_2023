-- DERERT FIBONACCI         fibonacci(n)
-- DEFINIS DAN SPESIFIKASI
fibonacci :: Int -> Int
{- fibonacci menerima integer n dan mengembalikan deret fibonacci suku ke-n -}
-- REALISASI
fibonacci n 
 | n == 0 = 0
 | n == 1 = 1
 | otherwise = fibonacci(n-1) + fibonacci(n-2)


 -- deret 0 1 1 2 3 5 8 13 21
 -- sigma (Un(n-1) + Un(n-2)) n>2