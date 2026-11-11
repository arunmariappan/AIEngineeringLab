"""Mini-lab (3 minutes): what does the same sentence cost in different languages?

Research on GPT-4's tokenizer found Indian languages averaged about 8x more tokens
than English for the same meaning. Nobody has told you Claude's number - so measure it.
"""
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-haiku-5-5"

# Same meaning in each language. Add your own language - and fix any line you read better than we do.
SENTENCES = {
    "English": "Please reset my password; I have not been able to log in since this morning.",
    "Hindi":   "कृपया मेरा पासवर्ड रीसेट करें; मैं आज सुबह से लॉग इन नहीं कर पा रहा हूँ।",
    "Kannada": "ದಯವಿಟ್ಟು ನನ್ನ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಮರುಹೊಂದಿಸಿ; ಇಂದು ಬೆಳಿಗ್ಗೆಯಿಂದ ನನಗೆ ಲಾಗಿನ್ ಆಗಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ.",
    "Tamil":   "தயவுசெய்து என் கடவுச்சொல்லை மீட்டமைக்கவும்; இன்று காலை முதல் என்னால் உள்நுழைய முடியவில்லை.",
}


def count(text: str) -> int:
    result = client.messages.count_tokens(
        model=MODEL,
        messages=[{"role": "user", "content": text}],
    )
    return result.input_tokens


if __name__ == "__main__":
    baseline = count(SENTENCES["English"])
    print(f"{'language':<10}{'chars':>7}{'tokens':>8}{'vs English':>12}")
    for language, sentence in SENTENCES.items():
        tokens = count(sentence)
        print(f"{language:<10}{len(sentence):>7}{tokens:>8}{tokens / baseline:>11.1f}x")
    print("\nCounts include a few tokens of message framing, so compare ratios, not raw numbers.")
