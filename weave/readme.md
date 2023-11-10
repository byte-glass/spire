# Weave.jl

## next steps
 - styles or themes, in the examples above julia code is rather colourful i.e. _too_ colourful
 - try command line script bin/weave.jl provided by the package

## latest

Tried to do away with syntax highlighting in code chunks, see the header of `a.jmd`. This does not seem to do anything. Other efforts e.g. pass keyword argument to `weave` met with the same fate. [The internet is pretty quite about this, one issue open since March 2021 with no comments from developers.]

## simple example

Suppose the file `b.jmd` looks as follows


    # Intro

    have a nice day!

    ```julia
    using Plots
    plot(sin, -3, 3, legend = false)
    ```

Then at the command line

```sh
GKSwstype=nul julia -e 'using Weave; weave("b.jmd", doctype="md2pdf")' 
```

has the desired effect.

### `GKSwstype=nul`

What is going on here?!

There is a known bug with Weave.jl. See https://github.com/JunoLab/Weave.jl/issues/436.

## LaTeX in document chunks

The invocation above will not work when latex is used in document chunks, this calls for `pandoc`.

The file `a.jmd` contains a display equation, namely


    $$ \hat{w}(x) = \sum_{j=1}^{\infty} \sin (2j - 1) \omega x $$ 

and inline latex such as `$\omega = 2 \pi / L$`.

A different `doctype` is called for. 

```sh
GKSwstype=nul julia -e 'using Weave; weave("a.jmd", doctype="pandoc2pdf")' 
```

## a make file

The make file in this directory (seems) to work as expected.

## inline code and the header

The file `a.jmd` uses inline code i.e. 

    `j using Dates; print(Dates.format(today(), "U d, Y"))` 

in the header no less, to get today's date.

## file `d.jmd`

This short example shows off some formatting i.e. the use of `&nbsp;` to insert some vertical white space and a weave keyword argument `pandoc_options` to pass a `-B` argument to `pandoc`. See also the make file.


### end
