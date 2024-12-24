## Wallet Tracker, Trading, and Twitter Integration

This Python program combines a wallet tracker, simulated trading functionality, and Twitter integration to fetch the latest tweets from a specified user. Designed for "Cupsey," this script is modular and can be adapted for other users or use cases.

---

### Features

1. **Wallet Tracker**: 
   - Tracks transactions with descriptions.
   - Calculates and displays current balance.
   - Saves and loads transaction history to/from a file.

2. **Trading Simulator**:
   - Mimics trading transactions.
   - Updates wallet with simulated trades.

3. **Twitter Integration**:
   - Fetches the latest tweet from a specified Twitter/X account using the Twitter API.

---

### Requirements

#### Dependencies:
- Python 3.7+
- Libraries:
  - `requests` (install with `pip install requests`)

#### Twitter API:
- A valid Twitter Developer account and Bearer Token are required to use the Twitter API.

---

### How to Use

1. **Clone/Download the Code**:
   - Save the script in a local Python file, e.g., `wallet_tracker.py`.

2. **Set Up Twitter API**:
   - Replace `YOUR_ACCESS_TOKEN_HERE` in the `get_latest_tweet` function with your Twitter API Bearer Token.

3. **Run the Code**:
   - Execute the script using Python:
     ```bash
     python wallet_tracker.py
     ```

4. **Functionality**:
   - **Wallet Tracking**:
     - Automatically loads saved transactions from `cupsey_wallet.json`.
     - Displays transaction history and current balance.
     - Updates the wallet with simulated trades.
   - **Twitter Integration**:
     - Fetches and displays the latest tweet from Cupsey's Twitter/X account.

---

### File Structure

- **`wallet_tracker.py`**: Main script.
- **`cupsey_wallet.json`**: Stores transaction history. Automatically created if it doesn't exist.

---

### Example Output

#### Initial Transactions:
```
Transaction History for Cupsey:

Date: 2024-12-01 10:00:00, Amount: 500, Description: Initial Deposit
Current Balance: 500
```

#### Simulated Trades:
```
Simulating trades...

Transaction added: {'date': '2024-12-01 11:00:00', 'amount': -500, 'description': 'Bought XYZ stock'}
Transaction added: {'date': '2024-12-01 11:30:00', 'amount': 300, 'description': 'Sold ABC stock'}
Transaction added: {'date': '2024-12-01 12:00:00', 'amount': -200, 'description': 'Bought DEF stock'}

Current Balance: 100
```

#### Latest Tweet:
```
Fetching Cupsey's latest tweet...

Latest tweet: "Just closed a great trade! 🚀 #trading"
```

---

### Notes

- Ensure the Twitter API token is kept secure.
- Use the `WalletTracker` methods to add new transactions or modify functionality.
- Customize the `trading_function` to simulate trades specific to your use case.

---

### License

This code is provided as-is for educational purposes. No warranty is provided, and the author is not responsible for any misuse of the software.
