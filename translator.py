import transformers

def translate(text, source_lang, target_lang):
  """
  This function translates a given text from one language to another.

  Args:
    text: The text to be translated.
    source_lang: The source language of the text.
    target_lang: The target language of the text.

  Returns:
    The translated text.
  """

  # Load the translation model.
  model = transformers.AutoModelForSeq2SeqLM.from_pretrained("marian-transformer")

  # Encode the text.
  encoded_input = model.encode(text, source_lang)

  # Decode the output.
  translated_output = model.decode(encoded_input, target_lang)

  return translated_output


def main():
  # Get the text to be translated.
  text = input("Enter a text: ")

  # Get the source and target languages.
  source_lang = input("Enter the source language: ")
  target_lang = input("Enter the target language: ")

  # Translate the text.
  translated_text = translate(text, source_lang, target_lang)

  # Print the translated text.
  print("The translated text is:", translated_text)


if __name__ == "__main__":
  main()
