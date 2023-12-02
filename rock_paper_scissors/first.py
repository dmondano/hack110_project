"""Rock, Paper, Scissors game."""

def main():
    """Main code section."""

def get_input(prompt) -> str:
    """Get's user input."""
    while True:
        user_response: str = input(f"{prompt}").lower()
        if user_response in scissor_rock_paper:
            return user_response

scissor_rock_paper: dict[str, int] = {"rock": 0, "paper": 1, "scissors": 3}
if __name__ == "__main__":
    main()