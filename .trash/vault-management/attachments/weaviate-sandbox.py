import weaviate

client = weaviate.Client(
    url = "https://ammarh-getting-started.weaviate.network/",
    additional_headers = {
        "X-OpenAI-Api-Key": "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"  
    }  
)

class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai"  # Or "text2vec-cohere" or "text2vec-huggingface"
}

#client.schema.create_class(class_obj)

schema = client.schema.get()
print(schema)

# ===== import data ===== 
# Load data 
import requests
import json
url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
with client.batch as batch:
    batch.batch_size=100
    for i, d in enumerate(data):
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        client.batch.add_data_object(properties, "Question")

nearText = {"concepts": ["biology"]}

result = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))


# ask = {
#   "question": "Who is the king of the Netherlands?",
#   "properties": ["summary"]
# }

# result = (
#   client.query
#   .get("Article", ["title", "_additional {answer {hasAnswer certainty property result startPosition endPosition} }"])
#   .with_ask(ask)
#   .with_limit(1)
#   .do()
# )

# print(result)