from triplesec import TripleSec
T = TripleSec(b'* password *')
x = T.encrypt(b"IT'S A YELLOW SUBMARINE")
print(T.decrypt(x).decode())
