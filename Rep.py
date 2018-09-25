#Credit goes to Reusable Authentication from the Iris-Sailesh Simhadri, James Steel, and Benjamin Fuller. This is the Python implementation from that paper

def rep(self, bits, p):
    count = 0
    for c_i, positions, seed in p:
        v_i = numPy.array ([bits[x] for x in positions])
        h = bytearray(hmac.new(seed, v_i, self.hash).digest())
        res = self.xor(c_i, h)
        if(self.check_result(res)):
            return res[len(res)/2:]
            count += 1
    return None