build:
	coffee -c -b -o lib src

clean:
	rm lib/*.js

test:
	mocha lib/test*
