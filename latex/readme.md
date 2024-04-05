# latex and github markdown


## inline expressions

As with pandoc markdown, single `$` delimiters give inline expressions e.g. `$A = \pi r^2$` renders $A = \pi r^2$.

There is another form using `$\`` and `\`$` delimiters.

## block expressions

Start a new line and use `$$` delimiters e.g.

    **The Cauchy-Schwarz Inequality**
    $$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

which gives the following,

$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

Alternatively fence some latex with `\`\`\`math`

```math
\int_\partial{A} \omega = \int_A d \omega
```


### end
