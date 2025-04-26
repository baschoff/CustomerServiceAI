import yaml

pc_knowledge_base = """
Components:
  cpu:
    keywords: ["cpu", "processor", "intel", "amd"]
    response: "We offer Intel and AMD processors at various price points. Popular options include Intel Core i5/i7 and AMD Ryzen 5/7."
    
  motherboard:
    keywords: ["motherboard", "mobo"]
    response: "We stock ATX and Micro-ATX motherboards compatible with both Intel and AMD processors."
    
  ram:
    keywords: ["ram", "memory"]
    response: "We offer DDR4 and DDR5 memory modules in 8GB, 16GB, and 32GB capacities."
    
  storage:
    keywords: ["storage", "ssd", "hdd"]
    response: "We carry SSDs (including M.2 NVMe) and traditional HDDs from 500GB to 4TB."
    
  gpu:
    keywords: ["gpu", "graphics"]
    response: "We stock NVIDIA and AMD graphics cards across various performance tiers."

Compatibility:
  basic:
    keywords: ["compatible", "fit", "work together"]
    response: "For compatibility: Intel CPUs need Intel socket motherboards, AMD CPUs need AMD socket motherboards. RAM must match motherboard type (DDR4 or DDR5)."

Recommendations:
  budget:
    keywords: ["budget", "cheap", "affordable"]
    response: "For budget builds ($600-800): Intel i3/AMD Ryzen 3, 16GB RAM, 500GB SSD, entry-level GPU."
    
  high_end:
    keywords: ["high end", "premium", "gaming"]
    response: "For high-end builds ($1500+): Intel i7/i9 or AMD Ryzen 7/9, 32GB RAM, 1TB SSD, RTX 4070 or better."

Support:
  help:
    keywords: ["help", "support", "refund", "return"]
    response: "For technical support or returns, email Fishy@pangelo.edu or call 555-123-4567. 30-day return policy on unopened items."

  refund_policy:
    keywords: ["refund", "return", "money back"]
    response: "Our refund policy allows returns within 30 days of purchase. Please visit https://Fishy.com/refund for more info."

  technical_issue:
    keywords: ["error", "issue", "problem", "crash"]
    response: "We're sorry you're facing issues. Please try restarting the app or contact support."

  order_status:
    keywords: ["status", "tracking", "delivery", "late", "order"]
    response: "You can check your order status at https://Fishy.com/order-status."

  account_help:
    keywords: ["login", "password", "account", "sign in"]
    response: "For account issues, please visit https://Fishy.com/account-help."
"""

# Load YAML knowledge base
kb = yaml.safe_load(pc_knowledge_base)

# Classify user query based on keywords
def classify_query(query):
    query = query.lower()
    matching_categories = []
    
    for main_category, subcategories in kb.items():
        for subcategory, data in subcategories.items():
            if any(keyword in query for keyword in data["keywords"]):
                matching_categories.append((main_category, subcategory))
    
    return matching_categories

# Get response based on category
def get_response(category_matches):
    if not category_matches:
        return ["I can help with questions about PC components, compatibility, or recommendations. What are you looking for today?"]
    
    responses = []
    for main_category, subcategory in category_matches:
        responses.append(kb[main_category][subcategory]["response"])
    
    return responses

def run_pc_assistant():
    print("Welcome to the PC Components Store Assistant!")
    print("Type your question (or 'exit' to quit):")
    
    while True:
        query = input("You: ")
        if query.lower().strip() == "exit":
            print("Assistant: Thank you for visiting. Goodbye!")
            break
            
        category_matches = classify_query(query)
        responses = get_response(category_matches)
        
        for response in responses:
            print(f"Assistant: {response}")

if __name__ == "__main__":
    run_pc_assistant()
