build:
	docker build -t py3-threads .
run: build
	docker run -it --mount type=bind,source=$$(pwd),target=/src py3-threads bash
clean:
	@find . -name '__pycache__' | xargs rm -rf;
	@find . -name '*.log' | xargs rm -rf;
	@find . -name 'alphabet.txt' | xargs rm -rf;