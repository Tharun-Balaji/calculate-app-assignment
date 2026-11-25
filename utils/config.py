from pathlib import Path

def load_system_prompt():
    """Load the system prompt from prompt.txt file."""
    prompt_path = Path(__file__).resolve().parent.parent / "prompt.txt"
    try:
        return prompt_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"System prompt file was not found: {prompt_path}"
        ) from exc
    except OSError as exc:
        raise OSError(f"Could not read system prompt file: {prompt_path}") from exc

def get_system_prompt():
    """Get the system prompt for the calculator assistant."""
    return load_system_prompt()

# Simple math functions for demonstration
def add_numbers_mock(num1, num2):
    """Mock function to add two numbers"""
    return num1 + num2

def subtract_numbers_mock(num1, num2):
    """Mock function to subtract two numbers"""
    return num1 - num2

SYSTEM_PROMPT = get_system_prompt()