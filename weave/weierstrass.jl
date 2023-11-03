#' ## Weierstrass's nowhere differentiable function

#' Weierstrass found a function that is uniformly continuous but nowhere differentiable, see e.g. https://en.wikipedia.org/wiki/Weierstrass_function.

#' Define partial sums of the Fourier series as follows,

f(x; N = 5, a = 0.8, b = 8) = sum(a^n * cos(b^n * pi * x) for n in 0:N);

#' It depends on parameters $a$ and $b$ that must satisfy $ab > 1 + \frac{3}{2} \pi$.

using Plots

plot(f, 0, 1, lw = 0.5, legend = false, tick_orientation = :out, grid = false)

plot!(x -> f(x, N = 5), lw = 0.25)

