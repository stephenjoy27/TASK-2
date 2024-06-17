def word_counter():
    """
    This function prompts the user to enter a sentence or paragraph,
    counts the number of words in the input, and displays the word count.
    """
    user_input = input("Enter a sentence or paragraph: ")

    if not user_input.strip():
        print("Error: No input provided.")
        return

    words = user_input.split()

    word_count = len(words)

    print(f"Word Count: {word_count}")

word_counter()
