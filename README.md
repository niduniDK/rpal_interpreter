# 🌀 RPAL Interpreter

An interpreter for the RPAL (Right-reference Programming Algorithmic Language) language — a simple functional language designed for educational purposes.

## 🚀 Overview

This project implements a full pipeline for RPAL source code:
- Lexical analysis (tokenization)
- Syntax parsing into a Concrete Syntax Tree (CST)
- Abstract Syntax Tree (AST) generation
- Standardization of AST
- Evaluation using an environment model interpreter

## 📂 Project Structure
```
rpal-interpreter/
│
├── testsing_scripts/ # Test RPAL programs
├── .gitignore
├── AST.py
├── CSE.py
├── CSE_machine.py
├── Closure.py
├── ControlStructureBuilder.py
├── Makefile
├── Node.py
├── README.md
├── lexical_analyser.py
├── myrpal.py
├── parser.py
├── standardizer.oy
├── utils.py
```


## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/rpal-interpreter.git
cd rpal-interpreter
```

Run with Python 3.7+:

```bash
python main.py -ast teststing_scripts/sample.txt
```

## 🛠 Built With
- Python 3

- Recursive descent parsing
