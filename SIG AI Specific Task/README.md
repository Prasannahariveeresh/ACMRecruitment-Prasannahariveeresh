# SIG AI Specific Tasks

In this directory I've posted my SIG AI specific tasks

## Step 0: The CS50x 2024 Artificial Intelligence Lecture

In this lecture I got to know what is Image Generation, ChatGPT, Prompt Engineering, Machine Learning, Deep Learning, Gen AI, Decision Trees and many more.

## Step 1: Presenting Fundamental AI Concepts

In this step I have prepared a presentation explaining

1. What is the working Principle of AI and What is a Model?
2. What is a Classifier? I've defined and explained a few classifiers that I know
3. Supervised vs Unsupervised Learning
4. How ChatGPT and Gemini works

Unfortunately I wasn't able to prepare a video on this topic as I was at hospital due to my health issues

#### LINK TO THE GOOGLE SHEET IS HERE

<a href="https://docs.google.com/presentation/d/1PF8x4lHYBAW2ad4U6NTSu-wlgLnBpEWsvkSJ726UyyU/edit?usp=sharing">
    <img src="https://img.shields.io/badge/Google Sheet-f48024" alt="Google Sheet" />
</a>

## Step 2: Power Of Preprocessing

In this task, I've performed some basic dataset operations, like

1. Load the Loan Prediction Dataset into a pandas DataFrame from the CSV file.

2. Display the first 5 rows of the DataFrame.

3. Display the last 5 rows of the DataFrame.

4. Find all the names of columns having missing values.

5. Find the number of missing values in each of the columns identified in the above step.

6. List all the columns which contain non-numerical entries.

7. Find all the Loan IDs of people who are not graduates.

8. Find all the Loan IDs of people who have an Applicant Income of less than 5000.

9. Find all the Loan IDs where the person is unmarried and has dependents '3+'.

10. Print all the rows which have Dependents '3+'.

11. Drop the rows having null/missing values.

12. Drop the column Loan_ID from the DataFrame.

## Step 3: Predicting the Output

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

Here, I tried understanding the trends and relationship between, `a`, `b` and `value`. Then I tried implementing different algorithms like Linear Regression, k-Nearest Neighbours, RandomForest, Support-Vector Regressor and Multi Layer Perceptron to predict the value for input `a` and `b`

## Step 4: API Integration

In this task, I built a command line based application that tells weather forecast city, latitude and longitude. This also produce weather forecast for 5 days. The data is being fetched from RapidAPI.