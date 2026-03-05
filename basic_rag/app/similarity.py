import math

def dot(a: list[float], b: list[float]) -> float:
    return sum(x*y for x, y in zip(a,b))

def norm(a: list[float]) -> float:
    return math.sqrt(sum(x*x for x in a))

def cosine_sim(a: list[float], b: list[float]) -> float:
    if not a or not b:
        return 0.0
    
    denom = norm(a) * norm(b)
    if denom == 0:
        return 0.0
    
    return dot(a,b)/denom