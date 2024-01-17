#' # Rabbits and ratios -- a familiar story

#' The straightforward Fibonacci sequence.

def fib(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

[fib(i) for i in range(1, 6)]

#' What about pairs?

def g(x):
    return (x[1], x[0] + x[1])

s = [g((1, 1)), g(g((1, 1))), g(g(g((1, 1))))]
s

#' Take a look at ratios of the sequence.

def h(x):
    return x[1] / x[0]

h(g(g(g((1, 1)))))

#' Or more succinctly,

list(map(h, s))

#' This is still rather clumsy.

def scan(f, x0, n):
    x = x0
    u = []
    for _ in range(n):
        u.append(x)
        x = f(x)
    return u

sigma = scan(g, (1, 1), 6)
sigma

#' Nearly there ...

p = list(map(h, scan(g, (1, 1), 13)))

#' Finally

phi = p[-1]

#' and

(phi, 1 / (phi - 1))

#' "That'll do rabbit."
