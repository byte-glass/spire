
%.md: %.pm
	pweave $< -f pandoc

%.md: %.py
	pweave $< -f pandoc

%.pdf: %.md
	pandoc -o $@ $< --pdf-engine=xelatex

clean:
	rm -rf *.pdf figures
