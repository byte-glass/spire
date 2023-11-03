
%.pdf: %.jmd
	GKSwstype=nul julia -e 'using Weave; weave("$<", doctype = "pandoc2pdf")'

%.pdf: %.jl
	GKSwstype=nul julia -e 'using Weave; weave("$<", doctype = "pandoc2pdf")'

clean:
	rm -rf *.tex *.out *.aux *.log figures jl_*

