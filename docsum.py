def split_document_into_chunks(text, chunk_size=5000):
	"""
	Split text into smaller chunks so an LLM can process those chunks individually.

	Args:
	  text (str): The input text to split into chunks
	  chunk_size (int): The maximum size of each chunk in terms of characters.

	Returns:
	  List[str]: A list of text chunks.
	"""
	# we split the text into chunks by the given chunk size
	chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
	return chunks
	



from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env file
load_dotenv()

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs in one sentence only.",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
