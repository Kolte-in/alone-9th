import spacy
import speech_recognition as sr

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to process user input and generate response
def generate_response(user_input):
    # Process user input with SpaCy
    doc = nlp(user_input)

    # Extract different parts of speech
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    prepositions = [token.text for token in doc if token.pos_ == "ADP"]
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]
    determiners = [token.text for token in doc if token.pos_ == "DET"]
    conjunctions = [token.text for token in doc if token.pos_ == "CONJ"]

    # Extract entities (like names)
    entities = [ent.text for ent in doc.ents]

    # Identify if the input is a question
    is_question = any(token.dep_ == "ROOT" and token.pos_ == "AUX" and token.text.lower() in ["how", "why", "where", "when", "what"] for token in doc)

    # Construct a response based on extracted tokens
    if is_question:
        if len(entities) > 0:
            response = f"I noticed you mentioned {', '.join(entities)}."
        elif len(nouns) > 0:
            response = f"I noticed you mentioned {', '.join(nouns)}."
        else:
            response = "I'm not sure what you're asking about."

    elif len(nouns) > 0 or len(verbs) > 0 or len(adjectives) > 0 or len(pronouns) > 0 or len(prepositions) > 0 or len(adverbs) > 0 or len(determiners) > 0 or len(conjunctions) > 0:
        response = "I noticed you mentioned "
        parts_of_speech = []
        if len(nouns) > 0:
            parts_of_speech.append(f"nouns like {', '.join(nouns)}")
        if len(verbs) > 0:
            parts_of_speech.append(f"verbs like {', '.join(verbs)}")
        if len(adjectives) > 0:
            parts_of_speech.append(f"adjectives like {', '.join(adjectives)}")
        if len(pronouns) > 0:
            parts_of_speech.append(f"pronouns like {', '.join(pronouns)}")
        if len(prepositions) > 0:
            parts_of_speech.append(f"prepositions like {', '.join(prepositions)}")
        if len(adverbs) > 0:
            parts_of_speech.append(f"adverbs like {', '.join(adverbs)}")
        if len(determiners) > 0:
            parts_of_speech.append(f"determiners like {', '.join(determiners)}")
        if len(conjunctions) > 0:
            parts_of_speech.append(f"conjunctions like {', '.join(conjunctions)}")

        response += " and ".join(parts_of_speech) + "."
    elif len(entities) > 0:
        response = f"I noticed you mentioned {', '.join(entities)}."
    else:
        response = "I'm not sure what you're talking about."

    return response

# Function to simulate a chat session using speech recognition
def chat_with_speech():
    print("Hello! I'm your chatbot. Speak something or say 'exit' to end the conversation.")

    # Initialize speech recognizer
    recognizer = sr.Recognizer()

    while True:
        # Capture audio from microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            user_input = recognizer.recognize_google(audio)
            print("You:", user_input)

            if user_input.lower() == 'exit':
                print("Bot: Goodbye!")
                break

            # Generate and print response
            response = generate_response(user_input)
            print("Bot:", response)

        except sr.UnknownValueError:
            print("Bot: Sorry, I didn't catch that. Can you say it again?")
        except sr.RequestError:
            print("Bot: Sorry, my speech service is down at the moment.")

# Main function to start the chatbot with speech recognition
if __name__ == "__main__":
    chat_with_speech()
