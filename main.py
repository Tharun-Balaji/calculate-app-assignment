import os
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT, add_numbers_mock, subtract_numbers_mock
from utils.parser import parse_function_call

load_dotenv()

class CalculatorAssistant:
    
    def __init__(self, api_key=None):
        resolved_api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not resolved_api_key:
            raise ValueError(
                "Gemini API key is required. Set GEMINI_API_KEY or pass api_key."
            )

        self.client = genai.Client(api_key=resolved_api_key)
        self.model = "gemini-2.5-flash"
    
    def handle_function_call(self, function_name, parameters):
        """Handle the actual function call execution"""
        if set(parameters) != {"num1", "num2"}:
            raise ValueError("Function calls must include num1 and num2.")

        num1 = float(parameters["num1"])
        num2 = float(parameters["num2"])
        if function_name == "add_numbers":
            result = add_numbers_mock(num1, num2)
            operator = "+"
        elif function_name == "subtract_numbers":
            result = subtract_numbers_mock(num1, num2)
            operator = "-"
        else:
            raise ValueError(f"Unknown calculator function: {function_name}")

        return f"The result of {num1} {operator} {num2} is {result}"
    
    def chat(self, user_input):
        """Main chat function that handles user input and decides whether to call functions"""
        fullprompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}"
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=fullprompt,
            )
        except Exception:
            return (
                "I'm sorry, I couldn't process your request because the Gemini "
                "API request failed. Please try again."
            )

        response_text = getattr(response, "text", None)
        if not response_text or not response_text.strip():
            return "I didn't receive a response. Please try again."

        function_name, parameters = parse_function_call(response_text)
        if function_name is None:
            return response_text.strip()

        try:
            return self.handle_function_call(function_name, parameters)
        except Exception:
            return "I'm sorry, I couldn't complete that calculation."

def answer_math_query(query, assistant=None):
    """Convenient wrapper function for math queries"""
    try:
        if assistant is None:
            assistant = CalculatorAssistant()
        return assistant.chat(query)
    except Exception:
        return "I'm sorry, the calculator assistant could not be started."

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
    
    try:
        assistant = CalculatorAssistant()
    except ValueError as exc:
        print(exc)
        return
    
    print("\n--- Sample Queries ---")
    for query in sample_queries:
        print(f"\nUser: {query}")
        response = answer_math_query(query, assistant)
        print(f"Calculator: {response}")

if __name__ == "__main__":
    main()