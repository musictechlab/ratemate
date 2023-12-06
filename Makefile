#! /usr/bin/make -f

flake8:
	flake8 ratemate/*

black:
	black ratemate/*

isort:
	isort ratemate/*