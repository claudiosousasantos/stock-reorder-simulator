# Stock Reorder Simulator

A simple Python pattern that simulates automatically reordering stock whenever it drops to or below a minimum threshold, shown across two examples.

## Files
- **stock_reorder.py** — coffee bean stock reorder
- **flour_reorder.py** — flour stock reorder

## How it works
- Starts with an initial stock level
- If stock is at or below the reorder threshold, it adds a fixed reorder amount
- Repeats until stock is safely above the threshold
- Prints the stock level after each reorder, plus the final stock

## How to run
```bash
python stock_reorder.py
python flour_reorder.py
```

## What I learned
- Using a `while` loop to repeat an action until a condition is no longer true
- Modeling a simple real-world inventory rule with variables and a loop
- Using `+=` to update a running value
- Recognizing when the same logic pattern applies across different real-world items
