import gensim

def summarize_text(text, ratio=0.5, word_count=None):
  """
  This function summarizes a given text using the TextRank algorithm.

  Args:
    text: The text to be summarized.
    ratio: The percentage of the text to be summarized.
    word_count: The number of words to be used in the summary.

  Returns:
    A summary of the text.
  """

  # Create a TextRank summarizer.
  summarizer = gensim.summarization.summarizer.TextRankSummarizer()

  # Summarize the text.
  summary = summarizer(text, ratio=ratio, word_count=word_count)

  return summary


def main():
  # Get the text to be summarized.
  text = """
  The text summarization is a technique that extracts the most important 
  information from a text and presents it in a concise and understandable 
  way. It can be used to summarize news articles, research papers, 
  and other types of text.
  """

  # Summarize the text.
  summary = summarize_text(text, ratio=0.5)

  # Print the summary.
  print("Summary:", summary)


if __name__ == "__main__":
  main()
