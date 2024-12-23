import datetime

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, price, quantity):
        if symbol in self.portfolio:
            print(f"{symbol} already in portfolio. Updating values.")
            self.portfolio[symbol]['price'] = price
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'price': price, 'quantity': quantity}
        print(f"Added/Updated {symbol}: {quantity} shares at ${price} each.")

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return
        print(f"\n{'Stock':<10}{'Price':<10}{'Quantity':<10}{'Value':<10}")
        print("-" * 40)
        total_value = 0
        for symbol, details in self.portfolio.items():
            value = details['price'] * details['quantity']
            total_value += value
            print(f"{symbol:<10}${details['price']:<10.2f}{details['quantity']:<10}{value:<10.2f}")
        print("-" * 40)
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

    def performance(self, current_prices):
        if not self.portfolio:
            print("Portfolio is empty. No performance to track.")
            return
        print(f"\n{'Stock':<10}{'Buy Price':<10}{'Current Price':<15}{'Change (%)':<10}")
        print("-" * 50)
        for symbol, details in self.portfolio.items():
            if symbol not in current_prices:
                print(f"{symbol:<10}N/A       Current price not provided")
                continue
            current_price = current_prices[symbol]
            change_percent = ((current_price - details['price']) / details['price']) * 100
            print(f"{symbol:<10}${details['price']:<10.2f}${current_price:<15.2f}{change_percent:<10.2f}")
        print("-" * 50)


def main():
    tracker = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            try:
                price = float(input("Enter purchase price: "))
                quantity = int(input("Enter quantity: "))
                tracker.add_stock(symbol, price, quantity)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            tracker.remove_stock(symbol)

        elif choice == '3':
            tracker.view_portfolio()

        elif choice == '4':
            current_prices = {}
            print("Enter current prices for your stocks. Type 'done' to finish.")
            while True:
                symbol = input("Stock symbol (or 'done' to finish): ").upper()
                if symbol.lower() == 'done':
                    break
                try:
                    current_price = float(input(f"Current price of {symbol}: "))
                    current_prices[symbol] = current_price
                except ValueError:
                    print("Invalid price. Please try again.")
            tracker.performance(current_prices)

        elif choice == '5':
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
