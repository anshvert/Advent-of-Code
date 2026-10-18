from collections import defaultdict
import hashlib

salt = "cuanljph"
candidates = defaultdict(list)
keys = set()

def get_triplet(h):
    for i in range(len(h) - 2):
        if h[i] == h[i+1] == h[i+2]:
            return h[i]
    return None

def get_quintuplets(h):
    quints = set()
    for i in range(len(h) - 4):
        if h[i] == h[i+1] == h[i+2] == h[i+3] == h[i+4]:
            quints.add(h[i])
    return quints

def get_stretched_hash(st: str):
    for _ in range(2016):
        st = hashlib.md5(st.encode('utf-8')).hexdigest()
    return st

idx = 0
while True:
    h = hashlib.md5((salt + str(idx)).encode('utf-8')).hexdigest()
    h = get_stretched_hash(h)
    
    quints = get_quintuplets(h)
    for q in quints:
        if q in candidates:
            for cand_idx in candidates[q]:
                if idx - cand_idx <= 1000:
                    keys.add(cand_idx)
                    
    triplet = get_triplet(h)
    if triplet is not None:
        candidates[triplet].append(idx)
        
    for char in list(candidates.keys()):
        while candidates[char] and idx - candidates[char][0] >= 1000:
            candidates[char].pop(0)
            
    if len(keys) >= 64:
        sorted_keys = sorted(list(keys))
        if idx > sorted_keys[63] + 1000:
            print(sorted_keys[63])
            break
            
    idx += 1