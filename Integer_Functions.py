n=10
m=10.5
print("n=",n)
print("m=",m)
print()
print("--Integer Functions--")
print()
print("Returns ratio of integer",n.as_integer_ratio())
print("Counts 1s in binary:",n.bit_count())
print("Number of bits needed:",n.bit_length())
print("Returns same integer:",n.conjugate())
print("Returns denominator:",n.denominator)
print("Converts byte to int:",int.from_bytes(b'\x05', 'big'))
print("Returns the imaginary part:",n.imag)
print("Returns imaginary part:",m.is_integer())
print("Returns numerator.",n.numerator)
print("Returns real part.",n.real)

