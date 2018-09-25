#Credit goes to Reusable Authentication from the Iris-Sailesh Simhadri, James Steel, and Benjamin Fuller. This is the Python implementation from that paper


def gen(self, bits, locker_size, lockers):
    length = self.hash().digest_size
    r = self.generate_same(size= length / 2  )
    zeros = bytearray ( [ 0  for  x  in  range ( length / 2 ) ] )
    check = zeros + r
    seeds = self.generate_sample(length.lockers)
    vs = numPy.array([random.generate_sample(pick_range, locker_size) \
        for x in range(lockers)])

    p = []
    for x in range(lockers):
        v_i = numPy.array([bits[y] for y in vs[x]])
        seed = seeds[x]
        h = bytearray(hmac.new(seed, v_i, self.hash).digest())
        c_i = self.xor(check, h)
        p.append((c_i, position[x], seed))
    return r, p