# Ticket Data Analysis System (Support Tickets)

## How to run
1. Put all files in one folder and open it in VS Code.
2. `pip install numpy pandas matplotlib`
3. `python main.py`  (creates `tickets.csv` automatically if missing)

Graphs are shown in a window and also saved in the `charts` folder.

## Files
| File | Purpose |
|---|---|
| generate_tickets.py | Creates the dataset (80 records) |
| helpers.py (module 1) | Tuple, dict, set, list methods, dict methods, 5 user-defined functions |
| file_handler.py (module 2) | csv + pandas file reading, add / search / update / delete |
| analysis.py (module 3) | NumPy, Pandas, GroupBy, missing values, statistics, insights, report |
| charts.py (module 4) | 6 matplotlib graphs |
| main.py | Menu program that imports all modules |

## 1-week teaching plan
| Day | Topic | File / menu option |
|---|---|---|
| 1 | Data structures (tuple, dict, set, list and dict methods) and user-defined functions | helpers.py |
| 2 | File handling with csv module, creating a dataset, modules and imports | generate_tickets.py, file_handler.py (read functions) |
| 3 | NumPy: 1D/2D arrays, indexing, slicing, sum, mean, max, min, std | analysis.py `numpy_demo` (menu 7) |
| 4 | Pandas basics: DataFrame, read_csv, select rows/columns, filter, sort | `pandas_basics` (menu 8) |
| 5 | GroupBy, missing values, statistics, insights | `groupby_demo`, `handle_missing_values`, `statistics`, `insights` (menu 9, 10, 11) |
| 6 | Graphs: bar, pie, line, histogram, scatter | charts.py (menu 12) |
| 7 | Add / search / update / delete, summary report, menu program, revision | file_handler.py, main.py (menu 1 to 6) |

## Requirement checklist
1 dataset (80 records) | 2 data structures (tuple, dict, set, list methods, dict methods) | 3 user-defined functions (5 in helpers.py plus many more) | 4 NumPy | 5 Pandas | 6 four modules | 7 file handling | 8 CRUD and report | 9 insights | 10 terminal output plus graphs
