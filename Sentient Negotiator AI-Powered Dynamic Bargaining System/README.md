# Sentient Negotiator AI-Powered Bargaining System

## Overview
The **Sentient Negotiator** is an advanced, AI-powered chatbot that engages in negotiations with users. Leveraging cutting-edge technologies like the **BlenderBot** (from the Transformers library) and **Sentiment Analysis** (via VADER), this system simulates realistic bargaining behavior, adjusting its offers based on user sentiment and negotiation history.

## Features
- **Natural Language Understanding**: Uses **BlenderBot** for generating human-like dialogue.
- **Sentiment-Driven Negotiation**: Integrates VADER sentiment analysis to adapt counteroffers based on the user's tone.
- **Price Negotiation**: Negotiates a price within a defined range using a dynamic pricing strategy.
- **Multi-round Negotiations**: Conducts up to 5 rounds of negotiation with history tracking to avoid endless loops.
- **Python-based**: Built with Python 3, leveraging popular libraries for AI and NLP.
  
## Installation

### Requirements
Ensure that Python 3.x is installed on your system. You can install the required packages by creating a virtual environment and using the \
equirements.txt\.

### Steps:
1. Clone the repository:
   \\\
   git clone https://github.com/Swaraj-91/sentient-negotiator.git
   \\\
2. Navigate to the project directory:
   \\\
   cd sentient-negotiator
   \\\
3. Create a virtual environment (optional but recommended):
   \\\
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate
   \\\
4. Install dependencies:
   \\\
   pip install -r requirements.txt
   \\\

## Usage
Start the chatbot negotiation by running the following command:

\\\
python3 negotiation_chatbot.py
\\\

The chatbot will interact with you, asking for price offers and adapting based on your sentiment and negotiation strategy.

## Key Libraries and Technologies:
- **Transformers**: For BlenderBot, enabling the chatbot to converse naturally.
- **PyTorch**: For running the BlenderBot model.
- **VADER Sentiment Analysis**: To gauge user sentiment and adjust counteroffers.
  
## Example Interaction
\\\
Welcome to the Advanced Negotiation Chatbot!
Let's negotiate a product price. Type 'exit' to end the conversation.
You: Hello, I would like to discuss the price.
Chatbot: Hello! Sure, what price are you thinking of?
You: I think \ sounds fair.
Chatbot: Your offer of \ is below the base price. How about \
\\\

## Contribution
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch: \git checkout -b new-feature\.
3. Commit your changes: \git commit -m 'Add some feature'\.
4. Push to the branch: \git push origin new-feature\.
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Author
**Swaraj** - [GitHub](https://github.com/Swaraj-91)


