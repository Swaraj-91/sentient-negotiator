import random
import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class AdvancedNegotiationChatbot:
    def __init__(self):
        """Initialize the negotiation chatbot with model, sentiment analysis, and base configuration."""
        # Load the pre-trained BlenderBot model and tokenizer
        self.tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        self.model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
        # Negotiation-related variables
        self.base_price = 100  # Base price for negotiation
        self.price_range = (80, 120)  # Define price range for negotiation
        self.negotiation_history = []  # Store negotiation context
        self.max_negotiation_rounds = 5  # Limit negotiation rounds to avoid endless loops

    def analyze_sentiment(self, user_input):
        """Analyze the sentiment of the user's message."""
        sentiment = self.sentiment_analyzer.polarity_scores(user_input)
        return sentiment['compound']  # Return compound sentiment score (-1 to 1)
    
    def dynamic_counteroffer(self, user_price, sentiment_score):
        """
        Adjust the counteroffer dynamically based on the user's sentiment 
        and previous offers, simulating realistic negotiation behavior.
        """
        last_offer = self.negotiation_history[-1] if self.negotiation_history else self.base_price
        
        # Adjust counteroffer based on sentiment score
        if sentiment_score > 0.5:
            # Positive sentiment, chatbot raises its offer
            counteroffer = random.randint(last_offer + 5, self.price_range[1])
        elif sentiment_score < -0.5:
            # Negative sentiment, chatbot lowers its offer
            counteroffer = random.randint(self.price_range[0], last_offer - 5)
        else:
            # Neutral sentiment, moderate counteroffer
            counteroffer = random.randint(last_offer, self.price_range[1])
        
        # Ensure counteroffer is within range
        counteroffer = max(min(counteroffer, self.price_range[1]), self.price_range[0])
        return counteroffer
    
    def generate_response(self, user_input):
        """Generate a response using the pre-trained BlenderBot model."""
        inputs = self.tokenizer([user_input], return_tensors="pt")
        response_ids = self.model.generate(**inputs)
        response = self.tokenizer.batch_decode(response_ids, skip_special_tokens=True)[0]
        return response

    def negotiate(self, user_price, sentiment_score):
        """Negotiate based on user price, previous offers, and sentiment analysis."""
        if len(self.negotiation_history) >= self.max_negotiation_rounds:
            return f"We've negotiated enough rounds. Final offer: ${self.base_price + 10}."
        
        if user_price < self.base_price:
            counteroffer = self.dynamic_counteroffer(user_price, sentiment_score)
            response = f"Your offer of ${user_price} is below the base price. How about ${counteroffer}?"
        elif user_price > self.base_price + 20:
            response = f"Your offer of ${user_price} is a bit too high. The best I can do is ${self.base_price + 10}."
        else:
            response = f"Your offer of ${user_price} is accepted! We'll finalize the deal at ${user_price}."
        
        # Save the negotiation history for tracking purposes
        self.negotiation_history.append(user_price)
        return response

    def start_negotiation(self):
        """Start the negotiation chatbot session."""
        print("Welcome to the Advanced Negotiation Chatbot!")
        print("Let's negotiate a product price. Type 'exit' to end the conversation.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for negotiating! Goodbye.")
                break

            # Analyze sentiment of user input
            sentiment_score = self.analyze_sentiment(user_input)
            print(f"Debug (Sentiment Score): {sentiment_score:.2f}")  # Show sentiment analysis (debugging)
            
            # Check if the user mentioned price in the input
            if "price" in user_input.lower():
                try:
                    # Ask for the desired price explicitly
                    desired_price = int(input("What price do you want to propose? "))
                    response = self.negotiate(desired_price, sentiment_score)
                    print(f"Chatbot: {response}")
                except ValueError:
                    print("Chatbot: Please enter a valid price.")
            else:
                # Get a generic response from the BlenderBot model
                response = self.generate_response(user_input)
                print(f"Chatbot: {response}")
                # Optionally, save the non-negotiation dialogue history for more context

if __name__ == "__main__":
    chatbot = AdvancedNegotiationChatbot()
    chatbot.start_negotiation()
