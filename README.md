## AI-Powered MCQ Generator
## Overview
This project is a Django-based web application that generates Multiple-Choice Questions (MCQs) from any given text using Google FLAN-T5. It processes input text, formulates structured questions, and provides four answer options along with the correct answer. The system is designed to be simple, efficient, and easy to use.

## Key Features
1. AI-Powered MCQ Generation – Automatically generates MCQs from input text.
2. Django Backend – Provides a structured, scalable, and maintainable web framework.
3. Hugging Face Integration – Uses google/flan-t5-base for advanced question generation.
4. Dynamic Output – Generates questions covering different aspects of the text (main idea, details, inference, etc.).
5. User-Friendly – Simple input-output interface for seamless interaction.
6. Logging & Debugging Support – Integrated logging to track errors and model performance.

## Tech Stack
1. Backend: Django (Python)
2. AI Model: Google FLAN-T5 (via Hugging Face transformers)
3. Libraries: Transformers, Requests, Logging
4. Frontend: HTML, CSS, JavaScript
5. Data Handling: JSON (Planned for Future Enhancements)

## How It Works
1. User Input: The user enters a paragraph or passage into the web interface.
2. Processing: The Django backend sends the text to the FLAN-T5 model via Hugging Face.
3. Question Generation: The model generates an MCQ with four answer choices.
4. Output Display: The question and options are formatted and displayed on the frontend.

## Future Enhancements
1. JSON Integration – Store and retrieve generated MCQs in JSON format for structured data handling.
2. Improved Question Variety – Fine-tune the model prompts to generate diverse and meaningful questions.
3. Better Frontend UI – Enhance the interface for a smoother user experience.
4. User Authentication – Allow users to save, edit, and manage their generated MCQs.
5. Export Options – Enable users to download MCQs as PDFs or CSV files.


