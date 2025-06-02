# Python interpreter
PYTHON = python
INTERPRETER = myrpal.py

# Directory of test scripts
SCRIPT_DIR = ./testing_scripts
SCRIPTS = $(wildcard $(SCRIPT_DIR)/*.txt)

# Run all files normally
run-all:
	@for file in $(SCRIPTS); do \
		echo "Running $$file..."; \
		$(PYTHON) $(INTERPRETER) $$file; \
		echo ""; \
	done

# Run all files to generate ASTs
run-all-ast:
	@for file in $(SCRIPTS); do \
		echo "Running AST for $$file..."; \
		$(PYTHON) $(INTERPRETER) -ast $$file; \
		echo ""; \
	done

# Run all files to generate symbol tables
run-all-st:
	@for file in $(SCRIPTS); do \
		echo "Running ST for $$file..."; \
		$(PYTHON) $(INTERPRETER) -st $$file; \
		echo ""; \
	done
