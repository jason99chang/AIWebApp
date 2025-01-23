
def load_business_profile():
    #update business context for AI before making decisions
    print("Profile loaded...\n")
    return

def load_menu():
    #display options infinitely until quit
    while True:
            print("\nDigital Marketing AI Tool Menu:")
            print("1. Generate SEO Content")
            #print("2. Create Ad Copy")
            #print("3. Draft Email Campaign")
            print("2. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice in ['1', '2', '3']:
                load_business_profile()

            if choice == '1':
                keyword = input("Enter the target keyword for SEO content: ")
                leads = find_outreach()
                generate_outreach(leads, keyword)
                print(f"\nGenerated SEO content:\n")

            elif choice == '2':
                product = input("Enter the product name for ad copy: ")

                print(f"\nGenerated ad copy:\n")

            elif choice == '3':
                topic = input("Enter the topic for email campaign: ")

                print(f"\nDrafted email campaign:\n")

            elif choice == '4':
                print("Thank you for using the Digital Marketing AI Tool. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    return

def find_outreach():
    #look at company profile, pick which platforms may be most effective
    #webscrape platforms for contact information
    #synthesise and generate potential leads list
    print("Outreach has been found.")
    leads = {"Jason", "Jenny"}
    return leads

def generate_outreach(leads, message):
    #go through potential leads list
    #contact people who we haven't conacted yet
    #analyze and improve the automated outreach strategy
    for a in leads:
        print(a + ", " + message)

    print("Outreach has been generated.")
    return

if __name__ == "__main__":
    load_menu()
