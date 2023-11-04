
%.pdf: %.jmd
	GKSwstype=nul julia -e 'using Weave; weave("$<", doctype = "pandoc2pdf", pandoc_options = ["-B", "maths-extras.tex"])'

%.pdf: %.jl
	GKSwstype=nul julia -e 'using Weave; weave("$<", doctype = "pandoc2pdf")'

tidy:
	rm -rf *.tex *.out *.aux *.log figures jl_*

clean: tidy
	rm -f *.pdf

