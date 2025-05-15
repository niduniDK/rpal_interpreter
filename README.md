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
├── lexer.py # Lexical analyzer
├── parser.py # Syntax parser
├── AST.py # AST generator from CST
├── standardizer.py # Standardizer for AST
├── myrpal.py # Entry point
└── README.md
```


## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/rpal-interpreter.git
cd rpal-interpreter
```

Run with Python 3.7+:

```bash
python main.py -ast teststing_scripts/Q!.txt
```

##🛠 Built With
- Python 3

- Recursive descent parsing
