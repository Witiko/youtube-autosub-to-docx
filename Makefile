%.vtt:
	youtube-dl --skip-download --write-auto-sub https://www.youtube.com/watch?v=$(basename $@)
	mv *.vtt $@

%.ass: %.vtt
	ffmpeg -i $< -y $@

%.md: %.ass
	python subtitles.py $< > $@

%.docx: %.md
	pandoc -i $< -o $@
	rm $(basename $<).vtt
