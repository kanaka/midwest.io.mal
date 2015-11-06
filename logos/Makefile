#$(info imgs: $(wildcard imgs/*))

montage.png: $(wildcard imgs/*)
	montage -geometry 100x100+10+10 $^ $@

clean:
	rm -f montage.png
