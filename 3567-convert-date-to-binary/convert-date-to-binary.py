class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, mon, day = date.split("-")
        year_bin = bin(int(year))[2:]
        mon_bin = bin(int(mon))[2:]
        day_bin = bin(int(day))[2:]
        return f"{year_bin}-{mon_bin}-{day_bin}"