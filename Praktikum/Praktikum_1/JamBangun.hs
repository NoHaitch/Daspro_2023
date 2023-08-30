module JamBangun where
jamBangun j m d =
	if j >= 7 then (True, abs(7 - j), abs(45 - m),abs(d))
		else if m >= 45 then (True, abs(7 - j), (45 - m), abs(d))
			else (True, abs(7 - j), abs(45 - m), abs(d))