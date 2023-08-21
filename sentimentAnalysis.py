import nltk

def sentiment_analysis(text):
  """
  This function performs sentiment analysis on a given text.

  Args:
    text: The text to be analyzed.

  Returns:
    A sentiment score, where 1 is positive, 0 is neutral, and -1 is negative.
  """

  # Tokenize the text.
  tokens = nltk.word_tokenize(text)

  # Create a sentiment lexicon.
  lexicon = {
      "positive": ["good", "great", "love"],
      "negative": ["bad", "terrible", "hate"]
  }

  # Calculate the sentiment score.
  sentiment_score = 0
  for token in tokens:
    if token in lexicon["positive"]:
      sentiment_score += 1
    elif token in lexicon["negative"]:
      sentiment_score -= 1

  return sentiment_score


def main():
  # Get the text to be analyzed.
  text = input("Enter a text: ")

  # Perform sentiment analysis.
  sentiment_score = sentiment_analysis(text)

  # Print the sentiment score.
  print("The sentiment score is:", sentiment_score)


if __name__ == "__main__":
  main()
