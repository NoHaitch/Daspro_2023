-- DETIK SEBELUMNYA         prevScond(j, m, d)
-- DEFINIS DAN SPESIFIKASI
prevSecond :: Int -> Int -> Int -> (Int,Int,Int)
{- prevSecond menerima integer jam, menit, detik dan mengembalikan sebuah tuple yang berisi
    waktu 1 detik sebelumnya -}
-- REALISASI
prevSecond j m d = 
    let totalDetik = d + (m*60) + (j*60*60)
        detikSebelumnya = totalDetik - 1
        -- dipisah biar mudah dimengerti sebenernya bisa langsung saja
        -- dibawah ini sebenernya ngga perlu dibikin variable tapi biar mudah 
        jam = div detikSebelumnya 3600
        menit = div (mod detikSebelumnya 3600) 60
        detik = mod (mod detikSebelumnya 3600) 60
    in 
        (jam, menit, detik)
        -- hasilnya tuple








----------------------------------------------------------------
-- HARUS PAKE REKURSIF

prevNSeconds :: Int -> Int -> Int -> Int -> (Int,Int,Int)
{- prevNSeconds j m d n menghasilkan tuple (j1,m1,d1) yang merupakan waktu n detik 
    sebelum pukul j:m:d. Prekondisi: 0<=j<=23, 0<=m<=59, 0<=d<=59, n>=0 -}
-- REALISASI
prevNSeconds j m d n  
    -- KARENA UDH ADA prevSecond dari atas maka bisa dipakai ulang 
    -- Sebenernya prevSecond itu kan sama aja dengan (prevNSeconds j m d 1 )
    -- kalo n = 0 maka ngga ada perubahan
    -- Karena di test case ke-3 bahwa kalo hasil detiknya negatif maka ganti hari
    | n == 0 = (j, m, d)
    | d + (m*60) + (j*60*60) <= 0 = prevNSeconds 23 59 59 (n-1)
    -- n >= 1,  (0,0,0) n --> (24,0,0) n --> (23,59,59) (n-1)
    | n == 1 = prevSecond j m d
    | otherwise = prevNSeconds j m (d-1) (n-1)

-- n >= 2 / 5 / 6
-- d + m*60 + j*60*60 = x + n ==>> x = prevNSeconds j m d n
-- (d + m*60 + j*60*60) - 1 = x + (n-1)
-- (d-1) + m*60 + j*60*60 = x + (n-1) ==> x = prevNSeconds j m (d-1) (n-1)
