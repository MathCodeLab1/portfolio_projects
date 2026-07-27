
# == Volume of a sphere ==

import math

r = 5
volume = (4/3) * math.pi * r**3
print(volume)


# == Wholesale cost of books ==

price = 24.95
discount = 0.4

book_price = price * (1 - discount)
books = 60

shipping = 3 + (books - 1) * 0.75

totaal = books * book_price + shipping

print(totaal)


# == Running time ==

start = 6*60 + 52

easy = 8 + 15/60
tempo = 7 + 12/60

total_run = 2 * easy + 3 * tempo

finish = start + total_run

hour = int(finish // 60)
minute = int(finish % 60)

print(hour , minute)