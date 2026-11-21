
import numpy as np
import pandas as pd
from helpers import print_header, show_table


def get_closed(df):

    return df[df["status"].isin(["Resolved", "Closed"])]



def numpy_demo(df):
    print_header("NUMPY")
    one_d = np.array(df["resolution_hours"].dropna())
    print("1D array (first 10 resolution hours):", one_d[:10])

    two_d = np.array(df[["response_hours", "resolution_hours", "satisfaction"]].dropna())
    print("2D array shape (rows, columns):", two_d.shape)

    print("\nIndexing: row 0, column 1 ->", two_d[0, 1])
    print("Slicing : first 5 rows of column 0 ->", two_d[:5, 0])
    print("Slicing : rows 2 to 3 (all columns) ->\n", two_d[2:4])

    names = ["response_hours", "resolution_hours", "satisfaction"]
    print("\n", "column".ljust(18), "sum".rjust(8), "mean".rjust(8), "max".rjust(6), "min".rjust(6), "std".rjust(8))
    for i in range(3):
        col = two_d[:, i]
        print("", names[i].ljust(18), str(round(col.sum(), 1)).rjust(8), str(round(col.mean(), 2)).rjust(8),
              str(col.max()).rjust(6), str(col.min()).rjust(6), str(round(col.std(), 2)).rjust(8))


def pandas_basics(df):
    print_header("PANDAS: SELECT, FILTER, SORT")
    print("Selected columns (first 5 rows):")
    show_table(df[["ticket_id", "customer", "category", "priority", "status"]].head())

    print("\nRows 10 to 14 using iloc:")
    show_table(df.iloc[10:15, 0:5])

    print("\nFilter: Critical tickets that are still Open")
    show_table(df[(df["priority"] == "Critical") & (df["status"] == "Open")][["ticket_id", "category", "agent", "created_date"]])

    print("\nSort: 5 slowest resolved tickets")
    slow = get_closed(df).sort_values("resolution_hours", ascending=False)
    show_table(slow[["ticket_id", "category", "priority", "resolution_hours"]].head())


def groupby_demo(df):
    print_header("PANDAS: GROUPBY")
    closed = get_closed(df)
    print("Tickets per category:")
    print(df.groupby("category")["ticket_id"].count())
    print("\nAverage resolution hours per priority:")
    print(closed.groupby("priority")["resolution_hours"].mean().round(1))
    print("\nAgent performance (resolved tickets):")
    print(closed.groupby("agent").agg(tickets=("ticket_id", "count"),
                                      avg_hours=("resolution_hours", "mean"),
                                      avg_rating=("satisfaction", "mean")).round(2))
    print("\nStatus count:")
    print(df.groupby("status")["ticket_id"].count())


def handle_missing_values(df):
    print_header("MISSING VALUES")
    print("Missing values per column:")
    print(df.isnull().sum())
    df = df.copy()
    avg = round(df["response_hours"].mean())
    df["response_hours"] = df["response_hours"].fillna(avg)
    print("\nresponse_hours filled with mean (", avg, ")")
    print("resolution_hours and satisfaction are blank only for unresolved tickets,")
    print("so we leave them blank and use dropna() when calculating.")
    print("\nMissing values after fixing:")
    print(df.isnull().sum())
    return df


def statistics(df):
    print_header("PANDAS: STATISTICS")
    print(df[["response_hours", "resolution_hours", "satisfaction"]].describe().round(2))
    closed = get_closed(df)
    print("\nCorrelation:")
    print(closed[["response_hours", "resolution_hours", "satisfaction"]].corr().round(2))



def insights(df):
    print_header("INSIGHTS")
    closed = get_closed(df)
    cat_count = df["category"].value_counts()
    cat_hours = closed.groupby("category")["resolution_hours"].mean()
    cat_rating = closed.groupby("category")["satisfaction"].mean()
    agent_count = closed["agent"].value_counts()
    corr = np.corrcoef(closed["resolution_hours"], closed["satisfaction"])[0, 1]
    critical_open = df[(df["priority"] == "Critical") & (df["status"].isin(["Open", "In Progress"]))]

    print("1. Most tickets come from     :", cat_count.idxmax(), "(" + str(cat_count.max()) + " tickets)")
    print("2. Slowest category to resolve:", cat_hours.idxmax(), "(" + str(round(cat_hours.max(), 1)) + " hours)")
    print("3. Happiest customers         :", cat_rating.idxmax(), "(rating " + str(round(cat_rating.max(), 2)) + ")")
    print("4. Agent with most resolved   :", agent_count.idxmax(), "(" + str(agent_count.max()) + " tickets)")
    print("5. Resolution time vs rating correlation:", round(corr, 2), "(negative = slow tickets get lower ratings)")
    print("6. Critical tickets not yet resolved    :", len(critical_open))
    print("7. Resolved percentage                  :", round(len(closed) / len(df) * 100, 1), "%")


def summary_report(df):
    print_header("SUMMARY REPORT")
    closed = get_closed(df)
    print("Total tickets          :", len(df))
    print("Resolved / Closed      :", len(closed))
    print("Open / In Progress     :", len(df) - len(closed))
    print("Avg first response     :", round(df["response_hours"].mean(), 1), "hours")
    print("Avg resolution time    :", round(closed["resolution_hours"].mean(), 1), "hours")
    print("Avg satisfaction       :", round(closed["satisfaction"].mean(), 2), "/ 5")
    print("Std dev of resolution  :", round(np.std(closed["resolution_hours"]), 2))
    print("\nTickets by priority:")
    print(df["priority"].value_counts())
    print("\nTickets by status:")
    print(df["status"].value_counts())
