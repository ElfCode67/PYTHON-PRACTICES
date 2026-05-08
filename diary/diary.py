import datetime

# --------------------- FUNCTIONS ---------------------
def show_menu():
    print("\n" + "="*30)
    print("📔 PERSONAL DIARY")
    print("="*30)
    print("1. Write new entry")
    print("2. Read all entries")
    print("3. Search entries")
    print("4. Delete all entries")
    print("5. Exit")
    print("="*30)

def add_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    title = input("\n📌 Title: ")
    print("✏️ Write your entry (press Enter twice when done):")
    
    lines = []
    while True:
        line = input()
        if line == "" and (len(lines) == 0 or lines[-1] == ""):
            if len(lines) > 0:
                lines.pop()
            break
        lines.append(line)
    
    content = "\n".join(lines)
    
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{'#'*50}\n")
        file.write(f"📅 {date}\n")
        file.write(f"📌 {title}\n")
        file.write(f"\n{content}\n")
        file.write(f"{'#'*50}\n")
    
    print("\n✅ Entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            entries = file.read()
            if entries.strip():
                print("\n" + entries)
            else:
                print("\n📭 No entries yet!")
    except FileNotFoundError:
        print("\n📭 No entries yet!")

def search_entries():
    keyword = input("\n🔍 Search for: ").lower()
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if keyword in content.lower():
                print(f"\n✅ Found entries containing: {keyword}")
                print("-"*30)
                paragraphs = content.split('#'*50)
                for para in paragraphs:
                    if keyword in para.lower():
                        print(para.strip())
                        print("-"*30)
            else:
                print(f"\n❌ No entries found with: {keyword}")
    except FileNotFoundError:
        print("\n📭 No entries yet!")

def delete_all():
    confirm = input("\n⚠️ Delete ALL entries? (yes/no): ")
    if confirm.lower() == "yes":
        with open("diary.txt", "w", encoding="utf-8") as file:
            file.write("")
        print("\n🗑️ All entries deleted!")
    else:
        print("\n❌ Deletion cancelled")

# --------------------- MAIN PROGRAM ---------------------
def main():
    while True:
        show_menu()
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            delete_all()
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again!")

# Run the app
if __name__ == "__main__":
    main()