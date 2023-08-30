isOneElmt l = length l == 1
konso :: Int -> [Int] -> [Int]
konso x l = [x] ++ l
isEmpty l = null l

isSortedDown :: [Int] -> Bool
isSortedDown l 
    | isOneElmt l = True
    | head (l) < head(tail l) = False
    | otherwise = isSortedDown (tail l)

getElTengah :: [Int] -> Int
getElTengah l
 | isOneElmt l = head l
 | length l == 2 = head l
 | otherwise = getElTengah (init (tail l)) 

elPosGanjil :: [Int] -> [Int]
elPosGanjil l 
 | isOneElmt l = l
 | length l == 2 = init l
 | otherwise = konso (head l) (elPosGanjil (tail (tail l)))

delAllx :: [Int] -> Int -> ([Int], Int)
delAllx l x =
    let (l1,n) = delAllx (tail l) x
    in 
        if isEmpty l then ([],0)
        else if head l /= x then ([head l] ++ l1 ,n)
        else (l1,n+1)

delAllx2 l x 
 | isEmpty l = (l,0)
 | head l /= x = (konso (head l) (fst (delAllx (tail l) x)), 1 + snd (delAllx (tail l) x))
 | otherwise = delAllx (tail l) x

