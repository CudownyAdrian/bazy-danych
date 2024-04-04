class Romanian:
    def __init__(self,value):
            self.value=self.to_arab(value)
            self.roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
            self.arab={value:key for key,value in self.roman.items()}

    def __add__(self, other):
        return Romanian(self.value + other.value)
    def __sub__(self, other):
        return Romanian(self.value - other.value)

    def __mul__(self, other):
        return Romanian(self.value * other.value)

    def __str__(self):
        return self.to_roman(self.value)

    def to_roman(self, n):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_numeral = ''
        i = 0
        while n > 0:
            for _ in range(n // val[i]):
                roman_numeral += syb[i]
                n -= val[i]
            i += 1
        return roman_numeral
    def to_arab(self,n):
        arab=0
        i=0
        while i<len(n):
            if i+1<len(n) and n[i:i+2] in self.roman:
                arab+=self.roman([n[i:i+2]])
                i+=2
            else:
                arab+=self.roman[n[i]]
        return arab
a=Romanian(100)
b=Romanian(70)
c=Romanian("XV")
d=Romanian("D")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print(d+c)
