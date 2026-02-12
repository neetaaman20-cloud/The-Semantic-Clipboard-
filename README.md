📋 Semantic Clipboard
A local-first, AI-powered clipboard manager that allows you to search through your copy history using Natural Language. Instead of searching for exact keywords, this tool uses Semantic Search to understand the meaning behind your snippets.

🚀 Key Features
Background Monitoring: A lightweight listener that captures every text snippet you copy in real-time.

Semantic Search: Uses the all-MiniLM-L6-v2 transformer model to find clips based on context (e.g., searching for "coding" will find "Python" snippets).

Local-First Privacy: All data is stored locally in a ChromaDB vector database. No data ever leaves your machine.

Developer-Friendly CLI: Simple command-line interface to search your history instantly.

🛠️ Tech Stack
Language: Python 3.9+

Vector Database: ChromaDB

Embeddings: Sentence-Transformers (Hugging Face)

Library: pyperclip for system clipboard access

📦 Installation
Clone the repository:

Bash
git clone https://github.com/your-username/Semantic-Clipboard.git
cd Semantic-Clipboard
Install dependencies:

Bash
pip install -r requirements.txt
📖 How to Use
1. Start the Listener

Run the background script to begin capturing your clipboard history:

Bash
python3 listener.py
2. Search Your History

Open a new terminal and search for any topic or concept:

Bash
python3 search.py "your search query here"
📂 Project Structure
core.py: Manages the ChromaDB connection and embedding generation.

listener.py: Handles the real-time background clipboard monitoring.

search.py: Command-line interface for querying the vector database.

requirements.txt: Project dependencies.

🛡️ License
Distributed under the MIT License. See LICENSE for more information.

👨‍💻 About the Author
I am a Bachelor of Computer Applications (BCA) student at YCMOU with a focus on AI, Machine Learning, and building practical tools for developers. I am passionate about creating local-first AI applications and optimizing workflows.
