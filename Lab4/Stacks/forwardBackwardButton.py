class BrowserStacks:
    def __init__(self):
        self.backStack = []  # Stack for backward navigation history
        self.forwardStack = []  # Stack for forward navigation history
        self.current_url = None  # Current URL

    def navigate_to(self, url):
        if self.current_url:
            self.backStack.append(self.current_url)
            self.forwardStack = []  # Clear the forward stack when navigating to a new URL
        self.current_url = url

    def go_back(self):
        if not self.backStack:
            print("Cannot go back. Backward history is empty.")
            return
        self.forwardStack.append(self.current_url)
        self.current_url = self.backStack.pop()

    def go_forward(self):
        if not self.forwardStack:
            print("Cannot go forward. Forward history is empty.")
            return
        self.backStack.append(self.current_url)
        self.current_url = self.forwardStack.pop()

    def current_page(self):
        return self.current_url

    def print_history(self):
        print("Backward History:", self.backStack)
        print("Forward History:", self.forwardStack)


# Example usage:
browser = BrowserStacks()

browser.navigate_to("https://www.example.com")
browser.navigate_to("https://www.openai.com")
browser.navigate_to("https://www.github.com")

browser.print_history()  # Print navigation history

print("Current Page:", browser.current_page())  # Print the current page

browser.go_back()
print("Current Page (after going back):", browser.current_page())

browser.go_forward()
print("Current Page (after going forward):", browser.current_page())

browser.print_history()  # Print updated navigation history
