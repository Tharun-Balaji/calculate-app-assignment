import os
from dotenv import load_dotenv
from google import genai
# TODO: Import SYSTEM_PROMPT from utils.config
# TODO: Import parse_function_call from utils.parser

# TODO: Load environment variables

class CalculatorAssistant:
    
    def __init__(self, api_key=None):
        # TODO: Initialize API key from parameter or env var GEMINI_API_KEY
        # TODO: Raise ValueError if no key found
        # TODO: Initialize Gemini client
        # TODO: Set model name to "gemini-2.5-flash"
        pass
    
    def handle_function_call(self, function_name, parameters):
        """Handle the actual function call execution"""
        # TODO: Handle add_numbers function
        # TODO: Handle subtract_numbers function
        # TODO: Return appropriate response based on function results
        pass
    
    def chat(self, user_input):
        """Main chat function that handles user input and decides whether to call functions"""
        # TODO: Prepare the conversation context with system prompt and user input
        # TODO: Call Gemini API to get response
        # TODO: Use parse_function_call() to check if response contains CALL_FUNCTION pattern
        # TODO: If function call detected, parse and execute it using handle_function_call()
        # TODO: If no function call, return the conversational response
        # TODO: Handle any errors gracefully
        pass

def answer_math_query(query, assistant=None):
    """Convenient wrapper function for math queries"""
    # TODO: Create CalculatorAssistant instance if not provided
    # TODO: Call assistant.chat(query)
    # TODO: Handle exceptions and return error message
    pass

def main():
    """Main function to demonstrate the calculator assistant."""
    print("Simple Calculator Assistant")
    print("Type 'quit' to exit")
    print("=" * 40)
    
    # Sample test queries
    sample_queries = [
        "What is 5 plus 3?",
        "Calculate 10 minus 4",
        "Add 15 and 25",
        "Hello, how are you?",
        "What can you do?"
    ]
    
    # TODO: Initialize assistant
    assistant = None
    
    print("\n--- Sample Queries ---")
    for query in sample_queries:
        print(f"\nUser: {query}")
        response = answer_math_query(query, assistant)
        print(f"Calculator: {response}")

if __name__ == "__main__":
    main()