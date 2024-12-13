import os
from anthropic import Anthropic
import base64

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

pdf_path = 'path_to_your_manuscript.pdf'
with open(pdf_path, 'rb') as pdf_file:
    pdf_data = base64.b64encode(pdf_file.read()).decode('utf-8')


client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Please review this manuscript and provide feedback and edits.",
                },
            ],
        },
    ],
    betas=['pdfs-2024-09-25']
)

print(response['content'])
