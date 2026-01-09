import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Draw a simple line with labels and title
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y, label="Sample Line")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()

# 2. Line chart of Alphabet Inc. financial data
data = {
    "Date": ["10-03-16", "10-04-16", "10-05-16", "10-06-16", "10-07-16"],
    "Open": [774.25, 776.03, 779.31, 779.00, 779.66],
    "High": [776.06, 778.71, 782.07, 780.48, 779.66],
    "Low": [769.50, 772.89, 775.65, 775.54, 770.75],
    "Close": [772.56, 776.43, 776.47, 776.86, 775.08]
}

df = pd.DataFrame(data)

plt.figure()
plt.plot(df["Date"], df["Open"], label="Open")
plt.plot(df["Date"], df["High"], label="High")
plt.plot(df["Date"], df["Low"], label="Low")
plt.plot(df["Date"], df["Close"], label="Close")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Inc. Stock Prices (Oct 3–7, 2016)")
plt.legend()
plt.show()

# 3. Plot two or more lines with different styles
plt.figure()
plt.plot(x, y, 'r--', label="Dashed Line")
plt.plot(x, [i**2 for i in x], 'b:', label="Dotted Line")
plt.plot(x, [i*3 for i in x], 'g-', label="Solid Line")
plt.legend()
plt.title("Multiple Line Styles")
plt.show()

# 4. Bar chart with value labels
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.figure()
bars = plt.bar(languages, popularity)
plt.title("Popularity of Programming Languages")
plt.ylabel("Popularity")

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             bar.get_height(), ha='center', va='bottom')

plt.show()

# 5. Bar chart with different colors
colors = ["red", "blue", "green", "orange", "purple", "brown"]

plt.figure()
plt.bar(languages, popularity, color=colors)
plt.title("Popularity of Programming Languages (Colored)")
plt.ylabel("Popularity")
plt.show()

# 6. Bar plot of scores by group and gender
men_scores = [22, 30, 35, 35, 26]
women_scores = [25, 32, 30, 35, 29]

index = np.arange(len(men_scores))
bar_width = 0.35

plt.figure()
plt.bar(index, men_scores, bar_width, label="Men")
plt.bar(index + bar_width, women_scores, bar_width, label="Women")

plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.xticks(index + bar_width / 2, ["G1", "G2", "G3", "G4", "G5"])
plt.legend()
plt.show()

# 7. Pie chart of programming language popularity
plt.figure()
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title("Popularity of Programming Languages")
plt.show()

# 8. Scatter plot with random distribution
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title("Random Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 9. Scatter plot with empty circles
plt.figure()
plt.scatter(x, y, facecolors='none', edgecolors='blue')
plt.title("Scatter Plot with Empty Circles")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 10. Scatter plot comparing Math and Science marks
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10,20,30,40,50,60,70,80,90,100]

plt.figure()
plt.scatter(marks_range, math_marks, color='red', label="Math")
plt.scatter(marks_range, science_marks, color='blue', label="Science")
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Math vs Science Marks")
plt.legend()
plt.show()
