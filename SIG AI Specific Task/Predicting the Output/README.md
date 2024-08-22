# SIG Specific Tasks - Predicting the Output

In this task, I've been given a dataset in a list where each entry consists of three numbers: `a`, `b`, and `value`. The first two numbers (`a` and `b`) are the inputs, and the third  (`value`) is the output associated with these inputs.

This is the given input data

```
data = [[0.0, 0.0, 0.0], [0.5, 1.5, 23.4], [1.2, 2.3, 45.6], [1.8,
3.7, 12.1], [2.4, 4.2, 78.9], [2.9, 5.1, 34.5], [3.5, 6.4, 56.7],
[4.1, 7.8, 67.8], [4.7, 8.5, 89.0], [5.2, 9.1, 12.3], [5.8, 1.0,
45.6], [6.3, 2.4, 78.9], [6.9, 3.1, 34.5], [7.4, 4.6, 56.7], [8.0,
5.2, 67.8], [8.6, 6.8, 89.0], [9.1, 7.3, 12.3], [9.7, 8.9, 45.6],
[10.0, 9.0, 78.9], [10.5, 0.5, 34.5]]
```

## Directory Structure

```
Predicting the Output
├── Output Pred.ipynb
├── predict.py
└── README.md
```

Here, I tried understanding the trends and relationship between, `a`, `b` and `value`. Then I tried implementing different algorithms like Linear Regression, k-Nearest Neighbours, RandomForest, Support-Vector Regressor and Multi Layer Perceptron to predict the value for input `a` and `b` and all these are recorded in `Output Pred.ipynb`

`predict.py` has the function that takes two input values, a and b, and returns the corresponding output value

## Training results

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>R-Squared Score</th>
      <th>Mean Absolute Error (MAE)</th>
      <th>Mean Square Error (MSE)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linear Regression</td>
      <td>16.32%</td>
      <td>19.74</td>
      <td>511.27</td>
    </tr>
    <tr>
      <td>k-Nearest Neighbors</td>
      <td>8.71%</td>
      <td>19.93</td>
      <td>515.49</td>
    </tr>
    <tr style="font-weight: bold;">
      <td>Random Forest Regression</td>
      <td>79.18%</td>
      <td>9.48</td>
      <td>115.19</td>
    </tr>
    <tr>
      <td>Support Vector Regression</td>
      <td>3.94%</td>
      <td>19.15</td>
      <td>547.09</td>
    </tr>
    <tr>
      <td>Multi-Layer Perceptron</td>
      <td>13.84%</td>
      <td>20.61</td>
      <td>616.89</td>
    </tr>
  </tbody>
</table>