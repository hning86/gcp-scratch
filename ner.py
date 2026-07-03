# add some comments
from google.cloud import language_v1

# use gemini-3.5-flash model
def really_non_functional_test(x, y):
    x = 8
    a = x - 2
    y = x + a
    return y

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """
    print(f"Analyzing entities in the following text: '{text_content}'")

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(
        request={"document": document, "encoding_type": encoding_type}
    )

    # Loop through entities returned from the API
    for entity in response.entities:
        print(f"\nEntity: {entity.name}")
        print(f"  Type: {language_v1.Entity.Type(entity.type_).name}")
        print(f"  Salience score: {entity.salience:.3f}")

        if entity.metadata:
            print("  Metadata:")
            for metadata_name, metadata_value in entity.metadata.items():
                print(f"    {metadata_name}: {metadata_value}")

        if entity.mentions:
            print("  Mentions:")
            for mention in entity.mentions:
                print(f"    - Text: {mention.text.content}")
                print(f"      Type: {language_v1.EntityMention.Type(mention.type_).name}")

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(f"\nLanguage of the text: {response.language}")


def simulate_fibonacci(n: int) -> list[int]:
    """Simulates the generation of the Fibonacci sequence up to n terms.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding numbers, starting with 0 and 1:
    F(0) = 0, F(1) = 1
    F(i) = F(i - 1) + F(i - 2) for i > 1

    Args:
        n (int): The total number of terms in the sequence to generate.

    Returns:
        list[int]: A list containing the first n terms of the Fibonacci sequence.
    """
    # Handle non-positive input values by returning an empty list
    if n <= 0:
        return []

    # If only one term is requested, return the sequence starting with 0
    if n == 1:
        return [0]

    # Initialize the sequence with the two base cases of Fibonacci: 0 and 1
    sequence = [0, 1]

    # Iteratively compute the subsequent terms starting from index 2 up to n - 1
    for _ in range(2, n):
        # Calculate the next number by summing the last two numbers in the sequence
        next_term = sequence[-1] + sequence[-2]

        # Append the newly calculated term to our sequence
        sequence.append(next_term)

    return sequence


if __name__ == "__main__":
    test_text = (
        "The Apollo 11 mission was the first spaceflight that landed humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin landed the Apollo Lunar Module Eagle "
        "on July 20, 1969, at 20:17 UTC. Armstrong became the first person to step onto the lunar surface "
        "six hours and 39 minutes later on July 21; Aldrin joined him 19 minutes later. "
        "They spent about two and a quarter hours together outside the spacecraft, and they collected "
        "47.5 pounds of lunar material to bring back to Earth."
    )
    sample_analyze_entities(test_text)

    # Demonstrate the Fibonacci simulation
    print("\n--- Fibonacci Simulation (First 10 Terms) ---")
    fib_10 = simulate_fibonacci(10)
    print(f"Result: {fib_10}")
