import os

from dotenv import load_dotenv
from google import genai


def main() -> None:
	load_dotenv()

	api_key = os.getenv("GEMINI_API_KEY")
	if not api_key:
		raise RuntimeError("Missing GEMINI_API_KEY in .env")

	client = genai.Client(api_key=api_key)

	response = client.models.generate_content(
		model="gemini-2.5-flash",
		contents="Tell me more about the Gemini 2.5 Flash model.",
	)

	text = getattr(response, "text", None)
	if text:
		print(text)
		return

	candidates = getattr(response, "candidates", None)
	if candidates:
		first_candidate = candidates[0]
		parts = first_candidate.content.parts
		if parts and getattr(parts[0], "text", None):
			print(parts[0].text)
			return

	print(response)


if __name__ == "__main__":
	main()
