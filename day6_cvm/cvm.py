import math
import random
def cvm(stream, epsilon, delta):
    p = 1
    X = set()
    m = len(stream)
    threshold = math.ceil(12/(epsilon**2)) * math.log(8 * m / delta)
    for i in stream:
        if i in X:
            X.remove(i)
        if random.random() < p:
            X.add(i)
        if(len(X) >= threshold):
            p /= 2
            X = {x for x in X if random.random() < 0.5}
    return len(X) / p

def generate_stream(length, range_start, range_end):
    list = [random.randint(range_start, range_end) for _ in range(length)]
    print(list)
    return list

# Example usage
stream_length = 10000  # Length of the random stream
range_start = 1
range_end = 8000
stream = generate_stream(stream_length, range_start, range_end)
epsilon = 0.1
delta = 0.05
estimate = cvm(stream, epsilon, delta)
print("Estimated number of distinct elements:", estimate)