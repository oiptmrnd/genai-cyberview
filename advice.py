from openai import OpenAI

# Set OpenAI's API key (can be any string, as vLLM doesn't require a real key)
# and API base to use vLLM's API server.
openai_api_key = ""  # Or any placeholder string
openai_api_base = "https://api.oip.tmrnd.com.my/t/cyberview.com.my/vllmgpu/1.0.0"  # Replace with your vLLM server's address and port

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# Make a Chat Completions API call
chat_response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",  # Replace with the name of the model loaded in your vLLM server
    messages=[
        {"role": "system", "content": "Act as a mentor for a hackathon."},
        {"role": "user", "content": "Please provide an idea on how to combine GenAI with Cyberview data"},
    ]
)

print("Chat response:", chat_response.choices[0].message.content)
