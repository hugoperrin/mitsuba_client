lint:
	python -m black mitsuba_client tests; python3 -m isort --multi-line 3 --trailing-comma --force-grid-wrap 0 --use-parentheses --skip __init__.py  --line-width 88 -rc mitsuba_client tests

flake8:
	python -m flake8 --exclude=tests/bdd/features/steps,mitsuba_client/externals mitsuba_client tests

testing:
	bash ./scripts/tests/coverage.sh
