"""
OpenAI model integration for Chat IA.
"""
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

class OpenAIModel:
    """Integration with OpenAI's GPT models."""
    
    def __init__(self, api_key, model="gpt-4"):
        """
        Initialize the OpenAI model.
        
        Args:
            api_key (str): OpenAI API key
            model (str): Model name to use (default: gpt-4)
        """
        self.name = "openai"
        self.api_key = api_key
        self.model = model
        self.client = openai.OpenAI(api_key=api_key)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def generate_response(self, message, system_prompt=None):
        """
        Generate a response using the OpenAI model.
        
        Args:
            message (str): User message to respond to
            system_prompt (str, optional): System prompt to guide the model
            
        Returns:
            str: Generated response
        """
        if not self.api_key:
            return "OpenAI API key not configured. Please check your .env file."
        
        messages = []
        
        # Add system prompt if provided
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        else:
            # Default system prompt
            messages.append({
                "role": "system", 
                "content": "You are a helpful assistant that provides accurate, concise, and useful information."
            })
        
        # Add user message
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response from OpenAI: {str(e)}"
    
    def get_capabilities(self):
        """
        Return the capabilities of this model.
        
        Returns:
            dict: Capability information
        """
        return {
            "name": self.name,
            "model": self.model,
            "strengths": ["general knowledge", "code generation", "creative writing", "logical reasoning"],
            "weaknesses": ["very recent events", "mathematical calculations"],
            "cost_per_1k_tokens": 0.03,  # Example cost, update based on current pricing
        }