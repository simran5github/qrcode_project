import time

def typing_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(prompt_text)
    input("Press Enter when you are ready to start...")

    start_time = time.time()

    user_input = input("Start typing: ")

    end_time = time.time()

    # Calculate words per minute (WPM) and accuracy
    prompt_words = prompt_text.split()
    user_words = user_input.split()

    correct_words = sum(w1 == w2 for w1, w2 in zip(prompt_words, user_words))
    accuracy = (correct_words / len(prompt_words)) * 100

    elapsed_time = end_time - start_time
    words_per_minute = (len(user_words) / elapsed_time) * 60

    print("\nTyping Test Results:")
    print(f"Words per Minute: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()