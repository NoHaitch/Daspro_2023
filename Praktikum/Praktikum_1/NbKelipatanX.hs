module NbKelipatanX where
	nbKelipatanX m n x = 
		if m <= n 
			then if mod m x == 0 
				then 1 + nbKelipatanX (m+x) n x
				else nbKelipatanX (m+1) n x 
			else 0