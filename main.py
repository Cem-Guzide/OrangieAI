class WalletTracker:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_transaction(self, amount, description=""):
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description
        }
        self.transactions.append(transaction)
        print(f"Transaction added: {transaction}")

    def get_balance(self):
        return sum(txn['amount'] for txn in self.transactions)

    def show_transactions(self):
        print(f"\nTransaction History for {self.owner}:\n")
        for txn in self.transactions:
            print(f"Date: {txn['date']}, Amount: {txn['amount']}, Description: {txn['description']}")
        print(f"\nCurrent Balance: {self.get_balance()}\n")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)
        print(f"Transactions saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.transactions = json.load(file)
            print(f"Transactions loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty transaction list.")
