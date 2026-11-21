import csv
import datetime
import numpy as np
import pandas as pd

FILE_PATH = "tickets.csv"


def read_with_csv():
   
    file = open(FILE_PATH, "r")
    reader = csv.DictReader(file)
    data = list(reader)
    file.close()
    return data


def load_data():
  
    return pd.read_csv(FILE_PATH)


def save_data(df):
    df.to_csv(FILE_PATH, index=False)


def next_ticket_id(df):
    return int(df["ticket_id"].max()) + 1


def add_ticket(df, customer, category, priority, agent):
    new_row = {
        "ticket_id": next_ticket_id(df),
        "customer": customer,
        "category": category,
        "priority": priority,
        "status": "Open",
        "agent": agent,
        "created_date": str(datetime.date.today()),
        "response_hours": np.nan,
        "resolution_hours": np.nan,
        "satisfaction": np.nan,
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    return df, new_row["ticket_id"]


def search_ticket(df, keyword):
    # search by ticket id or customer name
    return df[(df["ticket_id"].astype(str) == keyword) |
              (df["customer"].str.contains(keyword, case=False))]


def update_ticket(df, ticket_id, column, value):
    if ticket_id not in df["ticket_id"].values:
        return df, False
    df.loc[df["ticket_id"] == ticket_id, column] = value
    save_data(df)
    return df, True


def delete_ticket(df, ticket_id):
    if ticket_id not in df["ticket_id"].values:
        return df, False
    df = df[df["ticket_id"] != ticket_id]
    save_data(df)
    return df, True
