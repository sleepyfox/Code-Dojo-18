build:
	coffee -c -b -o lib src

clean:
	rm lib/*.js

test: build
	mocha -R spec lib/test*
