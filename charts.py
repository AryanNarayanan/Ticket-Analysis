import os
import matplotlib.pyplot as plt
import pandas as pd
from analysis import get_closed

if not os.path.exists("charts"):
    os.makedirs("charts")


def finish(file_name):
    plt.tight_layout()
    plt.savefig("charts/" + file_name)
    print("Saved: charts/" + file_name)
    plt.show()


def bar_category(df):
    counts = df["category"].value_counts()
    plt.figure(figsize=(7, 4))
    plt.bar(counts.index, counts.values, color="steelblue")
    plt.title("Tickets per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of tickets")
    finish("1_category_bar.png")


def pie_priority(df):
    counts = df["priority"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
    plt.title("Tickets by Priority")
    finish("2_priority_pie.png")


def line_monthly(df):
    dates = pd.to_datetime(df["created_date"])
    monthly = dates.dt.month.value_counts().sort_index()
    plt.figure(figsize=(7, 4))
    plt.plot(monthly.index, monthly.values, marker="o", color="green")
    plt.title("Tickets Created per Month")
    plt.xlabel("Month number")
    plt.ylabel("Number of tickets")
    plt.grid(True)
    finish("3_monthly_line.png")


def bar_resolution(df):
    avg = get_closed(df).groupby("category")["resolution_hours"].mean()
    plt.figure(figsize=(7, 4))
    plt.bar(avg.index, avg.values, color="orange")
    plt.title("Average Resolution Time per Category")
    plt.xlabel("Category")
    plt.ylabel("Hours")
    finish("4_resolution_bar.png")


def hist_satisfaction(df):
    closed = get_closed(df)
    plt.figure(figsize=(6, 4))
    plt.hist(closed["satisfaction"], bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], color="purple", edgecolor="black")
    plt.title("Customer Satisfaction Ratings")
    plt.xlabel("Rating (1-5)")
    plt.ylabel("Number of tickets")
    finish("5_satisfaction_hist.png")


def scatter_time_rating(df):
    closed = get_closed(df)
    plt.figure(figsize=(6, 4))
    plt.scatter(closed["resolution_hours"], closed["satisfaction"], color="red")
    plt.title("Resolution Time vs Satisfaction")
    plt.xlabel("Resolution hours")
    plt.ylabel("Rating")
    finish("6_scatter.png")


def all_charts(df):
    bar_category(df)
    pie_priority(df)
    line_monthly(df)
    bar_resolution(df)
    hist_satisfaction(df)
    scatter_time_rating(df)
