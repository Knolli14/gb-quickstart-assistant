
# Board Game Rules Retrieval System

This project is a retrieval-augmented generation (RAG) pipeline designed to help users query and retrieve specific rules from board game manuals. Using Google Cloud, ChromaDB, and advanced embedding models, it provides detailed answers about gameplay directly from the manuals.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Board games often come with extensive manuals that can make understanding the rules overwhelming. This project simplifies the process by allowing players to query specific rules or strategies and receive clear, concise answers. The system is built on a retrieval-augmented generation (RAG) pipeline to ensure answers are relevant and grounded in the game's actual manual.

---

## Features
- **Dynamic Querying**: Supports over 3,700 board games (11 GB of PDFs) with metadata-based filtering.
- **Semantic Search**: Uses embeddings for accurate text matching and retrieval.
- **Streamlit Frontend**: User-friendly interface to select games and ask questions.
- **LLM Answer Generation**: Generates responses using `google/flan-t5-small` for precise and context-aware answers.

---

## Getting Started

### Prerequisites
- Python 3.10+
- Google Cloud SDK (with Vertex AI enabled)
- OpenAI API key (optional for testing with GPT models)
- Required Python packages:
  - `transformers`
  - `sentence-transformers`
  - `ChromaDB`
  - `streamlit`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/game-rules-retrieval.git
   cd game-rules-retrieval


2. Install dependencies:

bash
Copy code
pip install -r requirements.txt
3. Set up Google Cloud:

4. Create a bucket and upload game manual PDFs.


### Usage

1. Indexing PDFs
Extract text and create embeddings:

bash
Copy code
python index_pdfs.py
2. Run the Streamlit App
Launch the interactive user interface:

bash
Copy code
streamlit run app.py
3. Query Game Rules
Choose a game from the dropdown.
Enter your question about the game's rules or strategy.
View detailed answers generated based on the game's manual.
Project Structure
graphql
Copy code
├── raw_data/          # Original PDF files
├── output_chunks/     # Processed JSON files with indexed data
├── vector_store/      # ChromaDB files storing embeddings
├── scripts/           # Utility scripts for indexing and querying
├── app.py             # Streamlit frontend
├── index_pdfs.py      # Script for indexing game manuals
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

Technologies Used
ChromaDB: For semantic search and efficient embedding storage.
Sentence Transformers: For generating embeddings of queries and texts.
Streamlit: For building the interactive frontend.
Google FLAN-T5 Small: As the primary language model for response generation.
Future Roadmap
User Manual Upload:
Allow users to upload their own game manuals for custom querying.
Model Optimization:
Improve model precision and speed for better user experience.
In-Game Assistance:
Real-time query support during gameplay.
Expanded Dataset:
Include more board games and languages.
Contributing
We welcome contributions! Please fork the repository and submit a pull request with your changes.
