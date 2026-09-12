# 🧮 Calculator Tools (`calculator_tools`)

A modular, reusable, and robust Python package demonstrating the fundamental concepts of **Functions**, **Modules**, **Packages**, and **Imports** in Python.

---

## 📁 Package Architecture

```
my_personal_calculator/
│
├── calculator_tools/             # The Reusable Package
│   ├── __init__.py               # Package initializer & top-level export namespace
│   ├── arithmetic.py             # Arithmetic & percentage calculations
│   ├── statistics.py             # Statistical & average calculations
│   ├── converter.py              # Temperature & simple unit conversions
│   └── exceptions.py             # Custom InvalidOperationError definition
│
├── tests/                        # Automated Unit Tests
│   ├── __init__.py
│   └── test_calculator.py        # 27 unit test cases with 100% coverage
│
├── main.py                       # Complete demonstration script
├── README.md                     # Documentation
└── LICENSE
```

---

## 🧠 Core Concepts Explained

| Concept | Definition | Example in this Repository |
| :--- | :--- | :--- |
| **Function** | A reusable block of code that performs a specific task. | `add(a, b)`, `mean(data)`, `convert_temperature(val, 'C', 'F')` |
| **Module** | A single `.py` file containing related functions, classes, and variables. | `arithmetic.py`, `statistics.py`, `converter.py`, `exceptions.py` |
| **Package** | A directory containing an `__init__.py` file and one or more modules/subpackages. | `calculator_tools/` folder |
| **Import** | Python's mechanism to access code from other modules and packages into a file. | `import calculator_tools`, `from calculator_tools import arithmetic`, `from calculator_tools.exceptions import InvalidOperationError` |

---

## 🚀 Import Styles Demonstrated

```python
# 1. Package-level import
import calculator_tools as calc
result = calc.add(10, 20)

# 2. Module-level import
from calculator_tools import arithmetic, statistics, converter
avg = statistics.mean([10, 20, 30])

# 3. Direct function-level import
from calculator_tools.converter import convert_temperature, convert_length
temp_f = convert_temperature(100, 'C', 'F') # 212.0

# 4. Custom exception import
from calculator_tools.exceptions import InvalidOperationError

try:
    calc.divide(10, 0)
except InvalidOperationError as e:
    print(f"Error handled: {e}")
```

---

## 🛠️ Modules and Features

### 1. `calculator_tools.arithmetic`
- `add(*numbers)`: Sums 2 or more numeric values.
- `subtract(a, b)`: Computes $a - b$.
- `multiply(*numbers)`: Multiplies 2 or more numeric values.
- `divide(a, b)`: Computes $a / b$ with division-by-zero protection.
- `power(base, exponent)`: Computes $base^{exponent}$.
- `percentage(part, total)`: Computes $\frac{part}{total} \times 100\%$.
- `percentage_of(percent, total)`: Computes $percent\%$ of $total$.

### 2. `calculator_tools.statistics`
- `mean(data)` / `average(data)`: Computes arithmetic mean.
- `median(data)`: Computes the median value (handles both odd and even datasets).
- `mode(data)`: Returns the most frequent value(s).
- `variance(data, sample=False)`: Computes population or sample variance.
- `standard_deviation(data, sample=False)`: Computes population or sample standard deviation.

### 3. `calculator_tools.converter`
- **Temperature Conversions**:
  - `celsius_to_fahrenheit(c)`
  - `fahrenheit_to_celsius(f)`
  - `celsius_to_kelvin(c)`
  - `kelvin_to_celsius(k)`
  - `convert_temperature(value, from_unit, to_unit)` (supports `'C'`, `'F'`, `'K'`)
  - Validates physical absolute zero limits ($K \ge 0$, $C \ge -273.15$, $F \ge -459.67$).
- **Unit Conversions**:
  - `convert_length(value, from_unit, to_unit)`: Supports `m`, `km`, `cm`, `mm`, `mi`, `yd`, `ft`, `in`.
  - `convert_weight(value, from_unit, to_unit)`: Supports `kg`, `g`, `mg`, `lb`, `oz`.

### 4. `calculator_tools.exceptions`
- `InvalidOperationError`: Custom exception raised for:
  - Division by zero
  - Invalid types (strings, `None`, boolean flags passed to numeric math)
  - Negative values for lengths/weights or sub-absolute-zero temperatures
  - Empty datasets for statistical calculation
  - Unsupported conversion units or operations

---

## 🧪 Running the Demo and Tests

### 1. Run the Demonstration
```bash
python main.py
```

### 2. Run Automated Unit Tests
```bash
python -m unittest discover -s tests -p "test_*.py"
```