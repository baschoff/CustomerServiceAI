# Customer Support Chatbot

responseDictionary = {
    # Offer lines
    'offer_cpu_intel': "We offer an Intel Core i5 CPU for $199.",
    'offer_cpu_amd': "We offer an AMD Ryzen 5 CPU for $179.",
    'offer_motherboard_intel': "We offer an Intel B660 motherboard for $129.",
    'offer_motherboard_amd': "We offer an AMD B550 motherboard for $119.",
    'offer_ram_ddr4': "We offer 8GB DDR4 RAM for $39.",
    'offer_ram_ddr5': "We offer 16GB DDR5 RAM for $69.",
    'offer_ssd': "We offer a 512GB NVMe SSD for $49.",
    'offer_gpu_nvidia': "We offer an NVIDIA GTX 1660 GPU for $249.",
    'offer_gpu_amd': "We offer an AMD RX 6600 GPU for $219.",
    'offer_cpu': "We offer CPUs starting at $179.",
    'offer_gpu': "We offer GPUs starting at $219.",
    'offer_motherboard': "We offer motherboards starting at $119.",
    'offer_ram': "We offer RAM starting at $39.",
    'offer_intel': "We offer Intel parts starting at $129.",
    'offer_amd': "We offer AMD parts starting at $119.",
    'offer_nvidia': "Yes, we offer NVIDIA GPUs starting at $249.",
    # Recommendations
    'recommend_intel_cpu': "We recommend the Intel Core i5-12400F for $199.",
    'recommend_intel_motherboard': "We recommend the ASUS B660 motherboard for $129.",
    'recommend_amd_cpu': "We recommend the AMD Ryzen 5 5600 for $179.",
    'recommend_amd_motherboard': "We recommend the MSI B550 motherboard for $119.",
    'recommend_amd_gpu': "We recommend the AMD RX 6600 for $249.",
    'recommend_nvidia_gpu': "We recommend the NVIDIA RTX 3060 for $299.",
    'recommend_ddr4': "We recommend 8GB DDR4 RAM for $39.",
    'recommend_ddr5': "We recommend 16GB DDR5 RAM for $69.",
    'recommend_ssd': "We recommend a 512GB NVMe SSD for $49.",
    'recommend_intel': "We recommend the Intel Core i5 CPU and ASUS B660 motherboard.",
    'recommend_amd': "We recommend the AMD Ryzen 5 CPU, MSI B550 motherboard, and RX 6600 GPU.",
    'recommend_nvidia': "We recommend the NVIDIA RTX 3060 GPU for optimal performance.",
    'recommend_cpu': "We recommend the Intel Core i5-12400F or AMD Ryzen 5 5600 for great performance.",
    'recommend_gpu': "Consider the NVIDIA RTX 3060 or AMD RX 6600 depending on your preference.",
    'recommend_motherboard': "We suggest the ASUS B660 for Intel or the MSI B550 for AMD builds.",
    'recommend_ram': "Choose between DDR4 8GB for $39 or DDR5 16GB for $69 based on compatibility.",
    # refund and other help
    'refund': "Our refund policy allows returns within 30 days of purchase. Please contact support for assistance at https://example.com/refund-application.",
    'help': "For assistance, please visit our support page at https://example.com/support.",
}


queryDictionary = {
    # offers
    "offer intel cpu": 'offer_cpu_intel',
    "offer amd cpu": 'offer_cpu_amd',
    "offer intel motherboard": 'offer_motherboard_intel',
    "offer amd motherboard": 'offer_motherboard_amd',
    "offer ddr4": 'offer_ram_ddr4',
    "offer ddr5": 'offer_ram_ddr5',
    "offer ssd": 'offer_ssd',
    "offer nvidia gpu": 'offer_gpu_nvidia',
    "offer amd gpu": 'offer_gpu_amd',
    "offer intel": 'offer_intel',
    "offer amd": 'offer_amd',
    "offer nvidia": 'offer_nvidia',
    "offer gpu": 'offer_gpu',
    "offer cpu": 'offer_cpu',
    "offer motherboard": 'offer_motherboard',
    "offer ram": 'offer_ram',
    # interests
    "interested in intel": 'interest_intel',
    "interested in amd": 'interest_amd',
    "interested in nvidia": 'interest_nvidia',
    "interested in ddr4": 'interest_ddr4',
    "interested in ddr5": 'interest_ddr5',
    "interested in ssd": 'interest_ssd',
    "interested in intel cpu": 'interest_cpu_intel',
    "interested in amd cpu": 'interest_cpu_amd',
    "interested in intel motherboard": 'interest_motherboard_intel',
    "interested in amd motherboard": 'interest_motherboard_amd',
    "interested in amd gpu": 'interest_gpu_amd',
    "interested in nvidia gpu": 'interest_gpu_nvidia',
    "interested in cpu": 'interest_cpu',
    "interested in gpu": 'interest_gpu',
    "interested in motherboard": 'interest_motherboard',
    "interested in ram": 'interest_ram',
    # recommendations
    "recommend intel": 'recommend_intel',
    "recommend amd": 'recommend_amd',
    "recommend nvidia": 'recommend_nvidia',
    "recommend ddr4": 'recommend_ddr4',
    "recommend ddr5": 'recommend_ddr5',
    "recommend ssd": 'recommend_ssd',
    "recommend intel cpu": 'recommend_intel_cpu',
    "recommend amd cpu": 'recommend_amd_cpu',
    "recommend intel motherboard": 'recommend_intel_motherboard',
    "recommend amd motherboard": 'recommend_amd_motherboard',
    "recommend nvidia gpu": 'recommend_nvidia_gpu',
    "recommend amd gpu": 'recommend_amd_gpu',
    "recommend cpu": 'recommend_cpu',
    "recommend gpu": 'recommend_gpu',
    "recommend motherboard": 'recommend_motherboard',
    "recommend ram": 'recommend_ram',
    # price data
    "price of intel cpu": 'price_intel_cpu',
    "price of amd cpu": 'price_amd_cpu',
    "price of intel motherboard": 'price_intel_motherboard',
    "price of amd motherboard": 'price_amd_motherboard',
    "price of ddr4 ram": 'price_ddr4_ram',
    "price of ddr5 ram": 'price_ddr5_ram',
    "price of ssd": 'price_ssd',
    "price of nvidia gpu": 'price_nvidia_gpu',
    "price of amd gpu": 'price_amd_gpu',
    "price of cpu": 'price_cpu',
    "price of gpu": 'price_gpu',
    "price of motherboard": 'price_motherboard',
    "price of ram": 'price_ram',
    # add cart
    "add amd cpu to cart": "add_amd_cpu",
    "add intel cpu to cart": "add_intel_cpu",
    "add ssd to cart": "add_ssd",
    "add ddr4 ram to cart": "add_ddr4_ram",
    "add ddr5 ram to cart": "add_ddr5_ram",
    "add nvidia gpu to cart": "add_nvidia_gpu",
    "add amd gpu to cart": "add_amd_gpu",
    "add amd motherboard to cart": "add_amd_motherboard",
    "add intel motherboard to cart": "add_intel_motherboard",
    "show cart": "show_cart",
    "empty cart": "empty_cart",
    # remove cart
    "remove amd cpu from cart": "remove_amd_cpu",
    "remove intel cpu from cart": "remove_intel_cpu",
    "remove ssd from cart": "remove_ssd",
    "remove ddr4 ram from cart": "remove_ddr4_ram",
    "remove ddr5 ram from cart": "remove_ddr5_ram",
    "remove nvidia gpu from cart": "remove_nvidia_gpu",
    "remove amd gpu from cart": "remove_amd_gpu",
    "remove amd motherboard from cart": "remove_amd_motherboard",
    "remove intel motherboard from cart": "remove_intel_motherboard",
    # refund
    "refund": 'refund',
    "how do i get a refund": 'refund',
    "i want a refund": 'refund',
    "apply for refund": 'refund',
    "request refund": 'refund',
    "refund policy": 'refund',
    # help
    "help": 'help',
    "i need help": 'help',
    "technical difficulties": 'help',
    "having issues": 'help',
    "support": 'help',
    "trouble using site": 'help'
}

priceDictionary = {
    'intel cpu': 199,
    'amd cpu': 179,
    'intel motherboard': 129,
    'amd motherboard': 119,
    'ddr4 ram': 39,
    'ddr5 ram': 69,
    'ssd': 49,
    'nvidia gpu': 249,
    'amd gpu': 219,
}

# Now add the derived prices after initial dictionary is built
priceDictionary['cpu'] = min(priceDictionary['intel cpu'], priceDictionary['amd cpu'])
priceDictionary['gpu'] = min(priceDictionary['nvidia gpu'], priceDictionary['amd gpu'])
priceDictionary['motherboard'] = min(priceDictionary['intel motherboard'], priceDictionary['amd motherboard'])
priceDictionary['ram'] = min(priceDictionary['ddr4 ram'], priceDictionary['ddr5 ram'])

starter_facts = [
    # offer facts
    'offer_cpu_intel', 'offer_cpu_amd', 'offer_motherboard_intel',
    'offer_motherboard_amd', 'offer_ram_ddr4', 'offer_ram_ddr5',
    'offer_ssd', 'offer_gpu_nvidia', 'offer_gpu_amd',
    'offer_cpu', 'offer_gpu', 'offer_motherboard', 'offer_ram', 
    'offer_intel', 'offer_amd', 'offer_nvidia',  # adding more offer categories
]

shopping_cart = []

rules = [
    # General + specific recommendations based on BOTH offer and interest
    # Intel bundle
    ({'interest_intel', 'offer_intel'}, {'recommend_intel'}),
    ({'interest_intel', 'offer_cpu_intel'}, {'recommend_intel_cpu'}),
    ({'interest_intel', 'offer_motherboard_intel'}, {'recommend_intel_motherboard'}),
    # AMD bundle
    ({'interest_amd', 'offer_amd'}, {'recommend_amd'}),
    ({'interest_amd', 'offer_cpu_amd'}, {'recommend_amd_cpu'}),
    ({'interest_amd', 'offer_motherboard_amd'}, {'recommend_amd_motherboard'}),
    ({'interest_amd', 'offer_gpu_amd'}, {'recommend_amd_gpu'}),
    # NVIDIA GPU
    ({'interest_nvidia', 'offer_gpu_nvidia'}, {'recommend_nvidia'}),
    ({'interest_nvidia', 'offer_gpu_nvidia'}, {'recommend_nvidia_gpu'}),
    # CPU general
    ({'interest_cpu', 'offer_cpu'}, {'recommend_cpu'}),
    ({'interest_cpu', 'offer_cpu_intel'}, {'recommend_intel_cpu'}),
    ({'interest_cpu', 'offer_cpu_amd'}, {'recommend_amd_cpu'}),
    # GPU general
    ({'interest_gpu', 'offer_gpu'}, {'recommend_gpu'}),
    ({'interest_gpu', 'offer_gpu_nvidia'}, {'recommend_nvidia_gpu'}),
    ({'interest_gpu', 'offer_gpu_amd'}, {'recommend_amd_gpu'}),
    # Motherboard
    ({'interest_motherboard', 'offer_motherboard'}, {'recommend_motherboard'}),
    ({'interest_motherboard', 'offer_motherboard_intel'}, {'recommend_intel_motherboard'}),
    ({'interest_motherboard', 'offer_motherboard_amd'}, {'recommend_amd_motherboard'}),
    # RAM
    ({'interest_ram', 'offer_ram'}, {'recommend_ram'}),
    ({'interest_ddr4', 'offer_ram_ddr4'}, {'recommend_ddr4'}),
    ({'interest_ddr5', 'offer_ram_ddr5'}, {'recommend_ddr5'}),
    # SSD
    ({'interest_ssd', 'offer_ssd'}, {'recommend_ssd'}),
    # Specific product interests
    ({'interest_cpu_intel', 'offer_cpu_intel'}, {'recommend_intel_cpu'}),
    ({'interest_cpu_amd', 'offer_cpu_amd'}, {'recommend_amd_cpu'}),
    ({'interest_motherboard_intel', 'offer_motherboard_intel'}, {'recommend_intel_motherboard'}),
    ({'interest_motherboard_amd', 'offer_motherboard_amd'}, {'recommend_amd_motherboard'}),
    ({'interest_gpu_nvidia', 'offer_gpu_nvidia'}, {'recommend_nvidia_gpu'}),
    ({'interest_gpu_amd', 'offer_gpu_amd'}, {'recommend_amd_gpu'}),
]

def forward_chaining(query, facts):
    """
    Implements forward chaining to infer new facts based on the initial query.
    """
    facts = set(facts)
    facts.add(query)
    new_facts = set()
    updated = True

    while updated:
        updated = False
        for condition_set, result_set in rules:
            if condition_set.issubset(facts) and not result_set.issubset(facts):
                facts.update(result_set)
                new_facts.update(result_set)
                updated = True

    return new_facts
    

def backward_chaining(goal, facts):
    """
    Implements backward chaining to check if a goal (recommendation) is justified by known facts.
    """
    facts_set = set(facts)

    # Directly known
    if goal in facts_set:
        return True

    # Try to justify the goal using the rules
    for condition_set, result_set in rules:
        if goal in result_set:
            if condition_set.issubset(facts_set):
                return True  # All preconditions are satisfied

    return False
    

def classify_query(query):
    """
    Classifies the query into a specific category based on the query dictionary.
    """
    if query in queryDictionary:
        return queryDictionary[query]
    else:
        return 'unknown_query'
    
def queryType(query):
    """
    Determines the type of query based on the classified query.
    """
    if query.startswith('offer'):
        return 'offer'
    elif query.startswith('recommend'):
        return 'recommend'
    elif query.startswith('interest'):
        return 'interest'
    elif query.startswith('price'):
        return 'price'
    elif query.startswith('add') or query == "show_cart" or query == "empty_cart" or query.startswith('remove'):
        return 'cart'
    elif query == 'refund':
        return 'refund'
    elif query == 'help':
        return 'help'
    else:
        return 'unknown_type'
    
def get_response(query, query_type):
    """
    Generates a response based on the classified query and its type.
    """
    global starter_facts  # This allows us to modify the actual global list
    if query_type == 'offer':
        return responseDictionary.get(query, "I'm sorry, I don't have that information.")
    
    elif query_type == 'recommend':
        viable = backward_chaining(query, starter_facts)  # Pass starter_facts here
        if viable:
            return responseDictionary.get(query, "Yes, we do recommend that option.")
        else:
            return "Based on your interests, we recommend other options."
        
    elif query_type == 'interest':
        inferred_facts = forward_chaining(query, starter_facts)
        for fact in inferred_facts:
            if fact not in starter_facts:
                starter_facts.append(fact)

        responses = [responseDictionary.get(fact, "") for fact in inferred_facts if fact in responseDictionary]
        if responses:
            return "\n".join(responses)
        else:
            return "Thanks for sharing your interest!"
        
    elif query_type == 'price':
        item = query.replace("price_", "").replace("_", " ")
        price = priceDictionary.get(item)
        if price:
            return f"The price of {item.title()} is ${price}."
        return "Sorry, I couldn't find the price for that item."

    elif query_type == 'cart':
        if query == "show_cart":
            if not shopping_cart:
                return "Your cart is currently empty."
            total = sum(priceDictionary[item] for item in shopping_cart)
            special_words = {'ssd', 'gpu', 'cpu', 'ram', 'nvme', 'ddr4', 'ddr5'}
            items_text = "\n".join(
                    f"- {' '.join(word.upper() if word.lower() in special_words else word.capitalize() for word in item.split())}: ${priceDictionary[item]}"
                    for item in shopping_cart)            
            return f"Your cart contains:\n{items_text}\nTotal: ${total}"

        elif query == "empty_cart":
            shopping_cart.clear()
            return "Your cart has been emptied."

        elif query.startswith("add_"):
            item = query.replace("add_", "").replace("_", " ")
            if item in priceDictionary:
                if item in shopping_cart:
                    return f"{item.title()} is already in your cart."
                shopping_cart.append(item)
                return f"{item.title()} has been added to your cart."
            return "Sorry, I couldn't add that item to your cart."
        
        elif query.startswith("remove_"):
            item = query.replace("remove_", "").replace("_", " ")
            if item in shopping_cart:
                shopping_cart.remove(item)
                return f"{item.title()} has been removed from your cart."
            else:
                return f"{item.title()} is not in your cart."
        
    elif query == 'refund':
        return responseDictionary['refund']

    elif query_type == 'help':
        return responseDictionary['help']

    else:
        return "I'm sorry, I didn't understand that. Try asking about a product offer, recommendation, or cart action."

def run_bot():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Customer Support Chatbot!")
    print("Type your question (or 'exit' to quit):\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("Bot: Thank you for chatting with us. Goodbye!")
            break
        
        # Classify the query
        classified_query = classify_query(user_input)
        query_type = queryType(classified_query)

        # Get responses based on query type
        query_response = get_response(classified_query, query_type)
        print(f"Bot: {query_response}")
        print(f"Bot: classified_query: {classified_query}")
        print(f"Bot: type: {query_type}")
        print()
    print()
if __name__ == "__main__":
    run_bot()