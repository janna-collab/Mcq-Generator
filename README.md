## AI-Powered MCQ Generator
Overview
This project is a Django-based web application that generates Multiple-Choice Questions (MCQs) from any given text using Google FLAN-T5. It processes input text, formulates structured questions, and provides four answer options along with the correct answer. The system is designed to be simple, efficient, and easy to use.

Key Features
AI-Powered MCQ Generation – Automatically generates MCQs from input text.
Django Backend – Provides a structured, scalable, and maintainable web framework.
Hugging Face Integration – Uses google/flan-t5-base for advanced question generation.
Dynamic Output – Generates questions covering different aspects of the text (main idea, details, inference, etc.).
User-Friendly – Simple input-output interface for seamless interaction.
Logging & Debugging Support – Integrated logging to track errors and model performance.

Tech Stack
Backend: Django (Python)
AI Model: Google FLAN-T5 (via Hugging Face transformers)
Libraries: Transformers, Requests, Logging
Frontend: HTML, CSS, JavaScript
Data Handling: JSON (Planned for Future Enhancements)

How It Works
User Input: The user enters a paragraph or passage into the web interface.
Processing: The Django backend sends the text to the FLAN-T5 model via Hugging Face.
Question Generation: The model generates an MCQ with four answer choices.
Output Display: The question and options are formatted and displayed on the frontend.

Future Enhancements
JSON Integration – Store and retrieve generated MCQs in JSON format for structured data handling.
Improved Question Variety – Fine-tune the model prompts to generate diverse and meaningful questions.
Better Frontend UI – Enhance the interface for a smoother user experience.
User Authentication – Allow users to save, edit, and manage their generated MCQs.
Export Options – Enable users to download MCQs as PDFs or CSV files.


