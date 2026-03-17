# Calculus Logic in Python 🚀

This repository is dedicated to my journey of mastering **MIT 18.01 (Single Variable Calculus)** and bridging it with **LLM Engineering** through code.

## 🧠 Core Concept: Automatic Differentiation
Instead of just solving math problems on paper, I am implementing calculus rules (Product Rule, Chain Rule, etc.) using **Python Object-Oriented Programming (OOP)**.

### Features
- **Dual Numbers**: Exact derivative calculation using the Dual Number algebra.
- **Operator Overloading**: Implementing `__mul__`, `__add__`, etc., to reflect 18.01 rules.
- **Verified via 18.01**: Each implementation is tested against MIT 18.01 exam problems.

## 🛠️ How to use
```python
from core.dual import Dual, sin

# Let's find the derivative of sin(x^10) at x = 1.5
x = Dual(1.5, der=1.0)
f = sin(x**10)
print(f.der) # The exact derivative!
