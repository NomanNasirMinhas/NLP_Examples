import spacy

def named_entity_recognition(text):
  """
  This function performs named entity recognition on a given text.

  Args:
    text: The text to be analyzed.

  Returns:
    A list of named entities.
  """

  # Load the spaCy model.
  nlp = spacy.load("en_core_web_sm")

  # Create a document object.
  doc = nlp(text)

  # Extract the named entities.
  named_entities = []
  for entity in doc.ents:
    named_entities.append(entity.text)

  return named_entities


def main():
  # Get the text to be analyzed.
  text = input("Enter a text: ")

  # Perform named entity recognition.
  named_entities = named_entity_recognition(text)

  # Print the named entities.
  print("The named entities are:", named_entities)


if __name__ == "__main__":
  main()
