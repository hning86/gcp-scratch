from google.cloud import language_v1


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

    # Loop through entitites returned from the API
    for entity in response.entities:
        print("Representative name for the entity: {}".format(entity.name))

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print("Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

        # Get the salience score associated with the entity in the [0, 1.0] range
        print("Salience score: {}".format(entity.salience))

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print("{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print("Mention text: {}".format(mention.text.content))

            # Get the mention type, e.g. PROPER for proper noun
            print(
                "Mention type: {}".format(
                    language_v1.EntityMention.Type(mention.type_).name
                )
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print("Language of the text: {}".format(response.language))


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
