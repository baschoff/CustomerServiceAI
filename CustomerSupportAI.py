# Customer Support AI Bot
# This bot uses forward and backward chaining to provide responses based on user queries.
all_facts = ['offer_cpu_intel', 'offer_cpu_amd','offer_motherboard_intel', 'offer_motherboard_amd', 
         'offer_ram_ddr4', 'offer_ram_ddr5', 'offer_ssd', 'offer_gpu_nvidea','offer_gpu_amd']

responseDictionary = {
    'offer_cpu_intel': "We offer an Intel CPU.",
    'offer_cpu_amd': "We offer an AMD CPU.",
    'offer_motherboard_intel': "We offer an Intel motherboard.",
    'offer_motherboard_amd': "We offer an AMD motherboard.",
    'offer_ram_ddr4': "We offer an DDR4 RAM.",
    'offer_ram_ddr5': "We offer an DDR5 RAM.",
    'offer_ssd': "We offer an SSD.",
    'offer_gpu_nvidea': "We offer an NVIDIA GPU.",
    'offer_gpu_amd': "We offer an AMD GPU."
}

queryDictionary = {
    # offers
    "offer intel cpu": 'offer_cpu_intel',
    "offer amd cpu": 'offer_cpu_amd',
    "offer intel motherboard": 'offer_motherboard_intel',
    "offer amd motherboard": 'offer_motherboard_amd',
    "offer ddr4 ram": 'offer_ram_ddr4',
    "offer ddr5 ram": 'offer_ram_ddr5',
    "offer ssd": 'offer_ssd',
    "offer nvidia gpu": 'offer_gpu_nvidea',
    "offer amd gpu": 'offer_gpu_amd',
    "offer budget": 'budget',
    "offer premium": 'premium',
    "offer intel": 'offer_intel',
    "offer amd": 'offer_amd',
    "offer nvidea": 'offer_nvidia',
    "offer gpu": 'offer_gpu',
    "offer cpu": 'offer_cpu',
    "offer motherboard": 'offer_motherboard',
    "offer ram": 'offer_ram',

    # interests
    "interested in budget": 'interest_budget',
    "interested in premium": 'interest_premium',
    "interested in intel": 'interest_intel',
    "interested in amd": 'interest_amd',
    "interested in nvidea": 'interest_nvidia',
    "interested in ddr4": 'interest_ddr4',
    "interested in ddr5": 'interest_ddr5',
    "interested in ssd": 'interest_ssd',
    "interested in cpu": 'interest_cpu',
    "interested in gpu": 'interest_gpu',
    "interested in motherboard": 'interest_motherboard',
    "interested in ram": 'interest_ram',
    "interested in intel cpu": 'interest_cpu_intel',
    "interested in amd cpu": 'interest_cpu_amd',
    "interested in intel motherboard": 'interest_motherboard_intel',
    "interested in amd motherboard": 'interest_motherboard_amd',
    "interested in amd gpu": 'interest_gpu_amd',
    "interested in nvidia gpu": 'interest_gpu_nvidia',

    # recommendations
    "recommend budget": 'recommend_budget',
    "recommend premium": 'recommend_premium',
    "recommend intel": 'recommend_intel',
    "recommend amd": 'recommend_amd',
    "recommend nvidea": 'recommend_nvidia',
    "recommend ddr4": 'recommend_ddr4',
    "recommend ddr5": 'recommend_ddr5',
    "recommend ssd": 'recommend_ssd',
    "recommend cpu": 'recommend_cpu',
    "recommend gpu": 'recommend_gpu',
    "recommend motherboard": 'recommend_motherboard',
    "recommend ram": 'recommend_ram',
    "recommend intel cpu": 'recommend_intel_cpu',
    "recommend amd cpu": 'recommend_amd_cpu',
    "recommend intel motherboard": 'recommend_intel_motherboard',
    "recommend amd motherboard": 'recommend_amd_motherboard',
    "recommend nvidia gpu": 'recommend_nvidia_gpu',
    "recommend amd gpu": 'recommend_amd_gpu',
    "recommend brand": 'recommend_brand',
}

starter_facts = [
    'offer_cpu_intel', 'offer_cpu_amd', 'offer_motherboard_intel',
    'offer_motherboard_amd', 'offer_ram_ddr4', 'offer_ram_ddr5',
    'offer_ssd', 'offer_gpu_nvidia', 'offer_gpu_amd'
]

rules = [
    # Budget interests
    ({'interest_budget'}, {
        'recommend_budget_cpu', 'recommend_budget_motherboard', 'recommend_budget_ram',
        'recommend_budget_gpu', 'recommend_budget_ssd'
    }),

    # Brand preferences
    ({'interest_intel'}, {'recommend_intel_cpu', 'recommend_intel_motherboard'}),
    ({'interest_amd'}, {'recommend_amd_cpu', 'recommend_amd_motherboard', 'recommend_amd_gpu'}),
    ({'interest_nvidia'}, {'recommend_nvidia_gpu'}),

    # Specific interests
    ({'interest_ddr4'}, {'recommend_ddr4'}),
    ({'interest_ddr5'}, {'recommend_ddr5'}),
    ({'interest_ssd'}, {'recommend_ssd'}),
    ({'interest_cpu'}, {'recommend_cpu'}),
    ({'interest_gpu'}, {'recommend_gpu'}),
    ({'interest_motherboard'}, {'recommend_motherboard'}),
    ({'interest_ram'}, {'recommend_ram'}),
]

# Function to extract keywords and responses from the knowledge base
def forward_chain(facts, rules):
    inferred = set()
    total_facts = set(facts)
    while True:
        new_inference = set()
        for conditions, conclusions in rules:
            if conditions.issubset(total_facts):
                for conclusion in conclusions:
                    if conclusion not in total_facts:
                        new_inference.add(conclusion)
        if not new_inference:
            break
        inferred.update(new_inference)
        total_facts.update(new_inference)
    return inferred

# Backward Chaining (New Code)
def backward_chain(goal, rules, known_facts):
    if goal in known_facts:
        return True
    for conditions, conclusions in rules:
        if goal in conclusions:
            if all(backward_chain(condition, rules, known_facts) for condition in conditions):
                return True
    return False

def classify_query(query):
    if query.startswith("interest_"):
        return "interest"
    elif query.startswith("offer_"):
        return "offer"
    elif query.startswith("recommend_"):
        return "recommendation"
    else:
        return "None"

def get_response(dictionary, keywords):
    output = []
    if not keywords:
        return ["I'm not sure how to help with that. Please contact support."]
    for key in keywords:
        if key not in dictionary:
            output.append("I'm not sure how to help with that. Please contact support.")
        else:
            output.append(dictionary[key])
    return output
        

def run_bot():
    global starter_facts
    print("Welcome to the AI Support Bot!")
    print("Type your question (or 'exit' to quit):\n")

    while True:
        query = input("You: ").lower().strip()
        if query == "exit":
            print("Bot: Goodbye!")
            break

        if query not in queryDictionary:
            print("Bot: Sorry, I don't understand that request.")
            continue

        query_fact = queryDictionary[query]
        starter_facts.append(query_fact)

        # Forward chaining to infer new facts
        inferred_facts = forward_chain(starter_facts, rules)
        starter_facts = list(set(starter_facts).union(inferred_facts))

        # If direct response exists, give it
        if query_fact in responseDictionary:
            print(f"Bot: {responseDictionary[query_fact]}")
            continue

        # Try backward chaining for goal
        if backward_chain(query_fact, rules, starter_facts):
            print("Bot: Yes, this is possible!")
        else:
            print("Bot: I'm not sure, but here are some related things we offer:")

        # Provide responses from inferred facts (if any)
        related_responses = get_response(responseDictionary, inferred_facts)
        for res in related_responses:
            print(f"Bot: {res}")
        print() 
        

if __name__ == "__main__":
    run_bot()
