module KonversiSuhu where
	konversiSuhu s k 
	 | k == 'K' = s + 273.15
	 | k == 'F' = (9/5 * s) + 32
	 | k == 'R' = 4/5 * s