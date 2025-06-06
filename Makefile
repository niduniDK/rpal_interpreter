# Python interpreter
ifeq ($(OS),Windows_NT)
	PYTHON = python
else
	PYTHON = python3
endif

INTERPRETER = myrpal.py

# Directory of test scripts
SCRIPT_DIR = ./testing_scripts
SCRIPTS = $(wildcard $(SCRIPT_DIR)/*.txt)

# Detect if running on Windows (CMD/PowerShell)
ifeq ($(OS),Windows_NT)
  IS_WINDOWS := 1
else
  IS_WINDOWS := 0
  SHELL := /bin/bash
endif

# Run a specific file
run:
	$(PYTHON) $(INTERPRETER) $(file)

# Print AST for a specific file
ast:
	$(PYTHON) $(INTERPRETER) -ast $(file)

# Print standardized AST for a specific file
st:
	$(PYTHON) $(INTERPRETER) -st $(file)

# Run all test scripts normally
run-all:
ifeq ($(IS_WINDOWS),1)
	@for %%f in ($(SCRIPTS)) do ( \
		echo Running %%f... && \
		$(PYTHON) $(INTERPRETER) %%f && \
		echo. \
	)
else
	@for f in $(SCRIPTS); do \
		echo "Running $$f..."; \
		$(PYTHON) $(INTERPRETER) $$f; \
		echo ""; \
	done
endif

# Run all test scripts to generate ASTs
run-all-ast:
ifeq ($(IS_WINDOWS),1)
	@for %%f in ($(SCRIPTS)) do ( \
		echo Running AST for %%f... && \
		$(PYTHON) $(INTERPRETER) -ast %%f && \
		echo. \
	)
else
	@for f in $(SCRIPTS); do \
		echo "Running AST for $$f..."; \
		$(PYTHON) $(INTERPRETER) -ast "$$f"; \
		echo ""; \
	done
endif

# Run all test scripts to generate STs
run-all-st:
ifeq ($(IS_WINDOWS),1)
	@for %%f in ($(SCRIPTS)) do ( \
		echo Running ST for %%f... && \
		$(PYTHON) $(INTERPRETER) -st %%f && \
		echo. \
	)
else
	@for f in $(SCRIPTS); do \
		echo "Running ST for $$f..."; \
		$(PYTHON) $(INTERPRETER) -st $$f; \
		echo ""; \
	done
endif

# Clean up
clean:
	rm -rf __pycache__ *.pyc

# Declare phony targets to avoid conflicts with filenames
.PHONY: run ast sast run-all run-all-ast run-all-st clean
