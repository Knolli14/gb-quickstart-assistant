# Board Game Rules Retrieval System

This project is a retrieval-augmented generation (RAG) pipeline designed to index and retrieve game rule documents. Using ChromaDB and advanced embedding models, it allows users to search and retrieve specific game rules from a large dataset of board game PDFs.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Features
- Indexes over 3,700 PDFs (11 GB of data) into a vector database.
- Uses state-of-the-art embeddings for semantic similarity.
- Enables fast, metadata-filtered retrieval of game rules.
- Supports query expansion and multi-vector querying.

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- ChromaDB
- sentence-transformers

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/game-rules-retrieval.git
   cd game-rules-retrieval
2. pip install -r requirements.txt
3. mkdir chroma_db


### Development setup
Place your PDFs in the `raw_data/` directory and run:
```bash
python index_pdfs.py


### Project Structure
├── raw_data/ # Original PDF files ├── output_chunks/ # JSON files with indexed data ├── scripts/ # Utility scripts (e.g., indexing, querying) ├── requirements.txt # Python dependencies ├── README.md # Project documentation

## Technologies Used
- ChromaDB
- Sentence Transformers
- Python
