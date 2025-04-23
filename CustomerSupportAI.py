import yaml

# Knowledge base
knowledge_base = """
Instructions:
  refund_policy:
    keywords: ["refund", "return", "money back"]
    response: "Our refund policy allows returns within 30 days of purchase. Please visit https://example.com/refund for more info."

  technical_issue:
    keywords: ["error", "issue", "problem", "crash"]
    response: "We're sorry you're facing issues. Please try restarting the app or contact support."

  order_status:
    keywords: ["status", "tracking", "delivery", "late", "order"]
    response: "You can check your order status at https://example.com/order-status."

  account_help:
    keywords: ["login", "password", "account", "sign in"]
    response: "For account issues, please visit https://example.com/account-help."
"""

# Load YAML knowledge base 
kb = yaml.safe_load(knowledge_base)["Instructions"]

# Classify user query based on keywords
def classify_query(query):
    query = query.lower()
    matching_categories = []
    for category, data in kb.items():
        if any(keyword in query for keyword in data["keywords"]):
            matching_categories.append(category)
    return matching_categories

# Get response based on category 
def get_response(categories):
    if not categories:
        return ["I'm not sure how to help with that. Please contact support."]
    return [kb[category]["response"] for category in categories]

def run_bot():
    print("Welcome to the AI Support Bot!")
    print("Type your question (or 'exit' to quit):\n")
    
    while True:
        query = input("You: ")
        if query.lower().strip() == "exit":
            print("Bot: Goodbye!")
            break
        categories = classify_query(query)
        responses = get_response(categories)
        for response in responses:
          print(f"Bot: {response}")
        print()


if __name__ == "__main__":
    run_bot()