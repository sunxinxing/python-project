i = 100
while i < 1000:
    a = i // 100
   # b = i // 10 % 10
    b = (i - a * 100) // 10
    c = i % 10
    
    if a**3 + b**3 + c**3 == i:        
       print(i)
    i += 1

