import re
import logging
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def load_pipeline():
    """Load the model pipeline with exception handling."""
    try:
        pipe = pipeline("text2text-generation", model="google/flan-t5-base", tokenizer="google/flan-t5-base")
        logging.debug("Pipeline loaded successfully!")
        return pipe
    except Exception as e:
        logging.error("Error loading model pipeline: %s", e)
        return None

# Load the model
mcq_pipeline = load_pipeline()

def clean_output(text):
    """Ensure the generated text follows a structured format."""
    text = text.replace("Options:", "\nOptions:\n")  # Ensure options section is clearly separated
    text = re.sub(r"([A-D])\)", r"\n\1)", text)  # Ensure each option appears on a new line
    text = text.replace("Answer:", "\nAnswer:")  # Ensure answer appears on a new line
    return text.strip()

def extract_mcq_components(generated_text):
    """Extract question, options, and answer using regex."""
    generated_text = clean_output(generated_text)
    logging.debug("Cleaned output:\n%s", generated_text)

    # Extract the question
    question_match = re.search(r'Question:\s*(.*?)\nOptions:', generated_text, re.DOTALL)
    question = question_match.group(1).strip() if question_match else "Failed to generate question"

    # Extract options (handling incorrect formatting)
    options_text = re.search(r'Options:\s*(.*?)\nAnswer:', generated_text, re.DOTALL)
    if options_text:
        raw_options = options_text.group(1).strip().split("\n")
        pattern = r"([A-D])\s*(.*?)(?=(?:[A-D]\s)|$)"
        matches = re.findall(pattern, raw_options[0])
        options = [f"{letter}) {text.strip()}" for letter, text in matches]

    # Ensure exactly 4 options
    if len(options) < 4:
        missing_count = 4 - len(options)
        options += [f"{chr(65+i)}) Placeholder Option {i+1}" for i in range(missing_count)]

    # Extract answer
    answer_match = re.search(r'Answer:\s*([A-D])', generated_text)
    answer = answer_match.group(1).strip() if answer_match else "A"

    return question, options, answer

def generate_question_and_options(text):
    """Generate an MCQ with four answer options using FLAN-T5."""
    if not mcq_pipeline:
        logging.error("Pipeline is not loaded. Cannot generate questions.")
        return "Failed to generate question", ["A) Option A", "B) Option B", "C) Option C", "D) Option D"], "A"

    prompt = (
        "Generate a multiple-choice question based on the following text.\n\n"
        "Format your output exactly as follows:\n\n"
        "Question: <Generated Question>\n"
        "Options:\n"
        "A) <Option 1>\n"
        "B) <Option 2>\n"
        "C) <Option 3>\n"
        "D) <Option 4>\n"
        "Answer: <Correct Option Letter>\n\n"
        f"Text: {text}"
    )

    try:
        output = mcq_pipeline(prompt, max_length=300, do_sample=True, top_p=0.9, top_k=50, temperature=0.7)
        logging.debug("Pipeline output: %s", output)

        if output and isinstance(output, list) and "generated_text" in output[0]:
            return extract_mcq_components(output[0]["generated_text"])
    except Exception as e:
        logging.error("Error generating question and options: %s", e)

    return "Failed to generate question", ["A) Option A", "B) Option B", "C) Option C", "D) Option D"], "A"

def generate_mcqs(text, question_count=5):
    """Generate multiple MCQs."""
    mcqs = []
    for i in range(question_count):
        logging.info("Generating MCQ %d...", i + 1)
        question, options, answer = generate_question_and_options(text)
        mcqs.append({"question": question, "options": options, "answer": answer})
    return mcqs

if __name__ == "__main__":
    sample_text = "Elon Musk has influenced the digital currency market with his tweets. Tesla stopped accepting Bitcoin due to environmental concerns. He has also expressed support for Dogecoin."
    result = generate_mcqs(sample_text, question_count=5)

    for i, mcq in enumerate(result, 1):
        print(f"MCQ {i}:")
        print(f"Question: {mcq['question']}")
        for option in mcq["options"]:
            print(option)
        print(f"Answer: {mcq['answer']}\n")
