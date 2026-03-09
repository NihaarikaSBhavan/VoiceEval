import ollama


class OllamaClient:

    def __init__(self, model_name):

        self.model_name = model_name

    def generate(self, prompt):

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        return response["message"]["content"]