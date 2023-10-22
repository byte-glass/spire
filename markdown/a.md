# markdown and pandoc

## usage

Typically something like

```sh
pandoc -o a.pdf --pdf-engine=xelatex a.md
```

## greek symbols

How does $\pi$ render?

## latex packages

Note: I had to install a new (?) package from the slew of texlive packages to get the above to work?!
The arrangement of the packages seems to change fairly frequently.

## `\usepackage{mathtools}`

I found I needed `\usepackage{mathtools}` to get prescripts to work (?), see below. It can be taken care of on the command line. Given a file `mathtools.tex` containing the single line,

```tex
\usepackage{mathtools}
```

then the invocation,

```sh
pandoc -o prescript.pdf -H mathtools.tex --pdf-engine=xelatex prescript.md
```

has the desired effect.

## display equations

Start the line with `$$` and all is well, e.g.

$$ \int_A d\omega = \int_{\partial{A}} \omega $$

How to number equations?

## `\newcommand`

Put `\newcommand{\from}{\colon}` in the file at some point in the file _before_ the new symbol `\from` is used, e.g.

\newcommand{\from}{\colon}

Then `\rho \from \mathbb{N} \to \mathbb{R}, x \mapsto 1/x` will render as follows,

$$ \varphi \from \mathbb{R} \to \mathbb{R}, x \mapsto 1/x $$

## `\mathbb{R}` etc

Some other useful newcommands, `\newcommand{\R}{\mathbb{R}}` etc

\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Q}{\mathbb{Q}}

And so $x \in \R$, $z \in \C$ and $u \in \Q$.

For the quaternions, try `\renewcommand{\H}{\mathbb{H}}`,

\renewcommand{\H}{\mathbb{H}}

whereupon we have $q \in \H$. And

$$ \gamma \from I \to \C $$

## Lie algebras and Hilbert spaces

`\mathfrak` does the trick for Lie algebras. Let's try `\newcommand{\so}{\mathfrak{so}}`,

\newcommand{\so}{\mathfrak{so}}

$$ h \in \so(2)$$

For a Hilbert space, `\mathcal{H}` giving $\mathcal{H}$ and an operator $T$,

$$ T \from \mathcal{H} \to \mathcal{H}$$

## prescripts

For a little nuclear physics, $\prescript{238}{92}{\mathbf{U}}$. Don't forget to `\usepackage{mathtools}`,

```sh
pandoc -o a.pdf -H mathtools.tex --pdf-engine=xelatex a.md
```

Or

$$  \prescript{g}{}{p} = \prescript{g}{}{R}^l_l + \prescript{}{g}{o_l}  $$

[I have no idea where that last example came from.]

## `\mathrm{d}` - area enclosed by a curve

Let $x \from [0, 1] \to \mathbb{R}^2$ be a closed $C^2$ curve, i.e. $x(0) = x(1)$. The area enclosed by the curve is given by the following functional,

$$ S[x] = \frac{1}{2} \int_0^1 (x^1 \dot{x}^2 − x^2 \dot{x}^1) \, \mathrm{d}t $$

How does this work, the curl or angular momentum term $x^1 \dot{x}^2 − x^2 \dot{x}^1$ and the factor of a half??


### end
