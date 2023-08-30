module HitungIndeks where
-- Hitung Indeks               hitungIndeks(d1,d2)
-- Definisi dan Spesifikasi
hitungIndeks :: Float -> Float -> Float -> Int
-- Realisasi
hitungIndeks nilaiUTS nilaiUAS nilaiTubes 
  | nilaiUTS == 0 || nilaiUAS == 0 || nilaiTubes == 0 = 0
  | nilaiUTS < 40 || nilaiUAS < 40 = 1
  | nilaiUTS >= 75 && nilaiUAS >= 75 && nilaiTubes >= 75 = 4
  | nilaiTubes < 40 && nilaiUAS > 40 && nilaiUTS > 40 = 2
  | nilaiUTS >= 40 && nilaiUAS >= 40 && nilaiTubes >= 40 && nilaiUTS < 75 && nilaiUAS < 75 && nilaiTubes < 75 = 2 
  | nilaiUTS < 75 || nilaiUAS < 75 = 3
  | otherwise = 3
