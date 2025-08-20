# text_formatter.py
def format_text_menu():
    """Display formatting options"""
    print("\n=== Text Formatting ===")
    print("1. Convert to uppercase")
    print("2. Convert to lowercase") 
    print("3. Title case")
    print("4. Remove extra spaces")
    print("5. Count vowels")
    print("6. Reverse text")
    print("0. Exit")

def count_vowels(text):
    """Count vowels in text"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def remove_extra_spaces(text):
    """Remove extra spaces from text"""
    return ' '.join(text.split())

def main():
    """Main program loop"""
    while True:
        format_text_menu()
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == '0':
            print("Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            text = input("Enter text to process: ")
            
            if choice == '1':
                result = text.upper()
            elif choice == '2':
                result = text.lower()
            elif choice == '3':
                result = text.title()
            elif choice == '4':
                result = remove_extra_spaces(text)
            elif choice == '5':
                vowel_count = count_vowels(text)
                result = f"Vowel count: {vowel_count}"
            elif choice == '6':
                result = text[::-1]
            
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()