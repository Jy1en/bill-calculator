# Bill Calculator and Data Usage Tracker

monthly_usage = []

def calculate_bill(data_used, data_limit, base_price):
    if data_used <= data_limit:
        total = base_price
    else:
        overage = data_used - data_limit
        total = base_price + (overage * 10)
    
    print(f"\n--- Bill Summary ---")
    print(f"Data Used: {data_used}GB")
    print(f"Data Limit: {data_limit}GB")
    print(f"Base Price: ${base_price}")
    print(f"Total Bill: ${total}")

def check_usage(data_used, data_limit):
    percentage = (data_used / data_limit) * 100
    
    if percentage >= 100:
        print("🚨 WARNING: You have exceeded your data limit!")
    elif percentage >= 80:
        print("⚠️ WARNING: You are close to your data limit!")
    else:
        print("✅ Your data usage is normal.")

def add_month(month, data_used):
    monthly_usage.append({"month": month, "data_used": data_used})
    print(f"✅ {month} usage recorded: {data_used}GB")

def view_usage_history():
    if len(monthly_usage) == 0:
        print("No usage history yet.")
    else:
        print("\n--- Usage History ---")
        for entry in monthly_usage:
            print(f"{entry['month']}: {entry['data_used']}GB")

def main_menu():
    while True:
        print("\n--- T-Mobile Bill Calculator ---")
        print("1. Calculate Bill")
        print("2. Check Data Usage")
        print("3. Add Month to History")
        print("4. View Usage History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data_used = float(input("Enter data used (GB): "))
            data_limit = float(input("Enter data limit (GB): "))
            base_price = float(input("Enter base price ($): "))
            calculate_bill(data_used, data_limit, base_price)
        elif choice == "2":
            data_used = float(input("Enter data used (GB): "))
            data_limit = float(input("Enter data limit (GB): "))
            check_usage(data_used, data_limit)
        elif choice == "3":
            month = input("Enter month name: ")
            data_used = float(input("Enter data used (GB): "))
            add_month(month, data_used)
        elif choice == "4":
            view_usage_history()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main_menu()