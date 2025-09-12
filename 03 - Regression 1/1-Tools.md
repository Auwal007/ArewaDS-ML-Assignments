Certainly! Here's your assignment written in clean, well-structured Markdown (`.md`) format:

---

# Regression Analysis: Waistline vs. Situps Using the Linnerud Dataset

## Objective
To build and visualize a linear regression model that explores the relationship between **waistline measurements** (independent variable) and the **number of situps completed** (dependent variable) using the `Linnerud` dataset from Scikit-learn.

---

## Dataset Overview

The **Linnerud dataset** is a small multivariate dataset included in `sklearn.datasets`. It contains:

| Features (Exercise Variables) | Targets (Physiological Measures) |
|-------------------------------|----------------------------------|
| `Waist` (inches)              | `Situps` (count)                 |
| `Weight` (pounds)             | `Chinups` (count)                |
| `Pulse` (bpm)                 | `Jump` (jumps per 15 seconds)    |

We will focus on:
- **Feature**: `Waist`
- **Target**: `Situps`

---

## Step-by-Step Implementation

### 1. Import Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```

### 2. Load the Dataset

```python
# Load the Linnerud dataset
linnerud = load_linnerud()

# Extract features and target
X = linnerud.data[:, [0]]  # Waist (first column)
y = linnerud.target[:, 0]  # Situps (first target column)

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
```

### 3. Create and Train the Model

```python
# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Print model coefficients
print(f"Intercept: {model.intercept_:.2f}")
print(f"Slope (coefficient): {model.coef_[0]:.2f}")
```

### 4. Make Predictions

```python
# Predict situps based on waistline
y_pred = model.predict(X)
```

### 5. Visualize the Results

```python
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data', alpha=0.7)
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression: Waistline vs. Situps')
plt.xlabel('Waistline (inches)')
plt.ylabel('Number of Situps')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
```

### 6. Evaluate Model Performance (Optional)

```python
from sklearn.metrics import r2_score, mean_squared_error

r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print(f"\nModel Evaluation:")
print(f"R² Score: {r2:.3f}")
print(f"Mean Squared Error: {mse:.2f}")
```

---

## Interpretation

- The **R² score** indicates how well the regression line fits the data (closer to 1.0 = better fit).
- A **negative slope** would suggest that larger waistlines are associated with fewer situps — which is physiologically plausible.
- This simple linear model provides insight into the inverse relationship between abdominal size and core endurance.

---

## Extension: Explore Other Relationships

You can repeat the same process for other pairs:

| Feature       | Target     |
|---------------|------------|
| `Weight`      | `Chinups`  |
| `Pulse`       | `Jump`     |

Example code snippet for Weight → Chinups:

```python
X2 = linnerud.data[:, [1]]  # Weight
y2 = linnerud.target[:, 1]  # Chinups

model2 = LinearRegression()
model2.fit(X2, y2)
y2_pred = model2.predict(X2)

plt.scatter(X2, y2, label='Data')
plt.plot(X2, y2_pred, color='green', label='Regression Line')
plt.title('Weight vs. Chinups')
plt.xlabel('Weight (lbs)')
plt.ylabel('Chinups')
plt.legend()
plt.show()
```

---

## Conclusion

This assignment demonstrates how linear regression can be used to uncover simple linear relationships between physiological and exercise metrics. The model reveals that **increased waist circumference is generally associated with fewer situps**, supporting the intuitive notion that higher body fat may correlate with reduced muscular endurance.

> ✅ **Note**: While this is a univariate analysis, real-world applications often use multivariate models (e.g., multiple features like waist + weight + pulse to predict situps).

---

## References

- Scikit-learn Linnerud Dataset: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html
- Linear Regression Theory: Hastie, Tibshirani, & Friedman (2009), *Elements of Statistical Learning*

---

Let me know if you'd like this exported as a downloadable `.md` file or converted to a Jupyter Notebook!