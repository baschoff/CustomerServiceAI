# Customer Support AI Bot
# This bot uses forward and backward chaining to provide responses based on user queries.
all_facts = ['offer_cpu_intel', 'offer_cpu_amd','offer_motherboard_intel', 'offer_motherboard_amd', 
         'offer_ram_ddr4', 'offer_ram_ddr5', 'offer_ssd', 'offer_gpu_nvidea','offer_gpu_amd']

responseDictionary = {
    # offer line
    'offer_cpu_intel': "We offer an Intel CPU.",
    'offer_cpu_amd': "We offer an AMD CPU.",
    'offer_motherboard_intel': "We offer an Intel motherboard.",
    'offer_motherboard_amd': "We offer an AMD motherboard.",
    'offer_ram_ddr4': "We offer DDR4 RAM modules.",
    'offer_ram_ddr5': "We offer DDR5 RAM modules.",
    'offer_ssd': "We offer a variety of SSDs.",
    'offer_gpu_nvidea': "We offer an NVIDIA GPU.",
    'offer_gpu_amd': "We offer an AMD GPU.",
    'offer_cpu': "We offer both Intel and AMD CPUs.",
    'offer_gpu': "We offer both NVIDIA and AMD GPUs.",
    'offer_motherboard': "We offer motherboards compatible with Intel and AMD CPUs.",
    'offer_ram': "We provide DDR4 and DDR5 RAM options.",
    'offer_intel': "We provide Intel CPUs and compatible motherboards.",
    'offer_amd': "We offer AMD CPUs, GPUs, and motherboards.",
    'offer_nvidea': "You might be looking for NVIDIA — yes, we offer NVIDIA GPUs.",
    'offer_budget': "We offer budget-friendly options for CPUs, GPUs, RAM, and SSDs.",
    'offer_premium': "We provide high-performance components for premium setups.",

    # recommendation line
    'recommend_budget_cpu': "We recommend AMD Ryzen 3 or Intel i3 for budget builds.",
    'recommend_budget_motherboard': "We suggest entry-level B-series motherboards.",
    'recommend_budget_ram': "We suggest 8GB DDR4 RAM for budget systems.",
    'recommend_budget_gpu': "We recommend AMD RX 6400 or NVIDIA GTX 1650 for budget gamers.",
    'recommend_budget_ssd': "We suggest 256GB SATA SSDs as a low-cost option.",
    'recommend_intel_cpu': "We recommend Intel's 12th/13th Gen CPUs based on your interest.",
    'recommend_intel_motherboard': "We suggest Z690 or B660 motherboards for Intel CPUs.",
    'recommend_amd_cpu': "You might like AMD Ryzen 5 or Ryzen 7 processors.",
    'recommend_amd_motherboard': "We recommend B550 or X570 motherboards for AMD builds.",
    'recommend_amd_gpu': "Consider the AMD RX 6600 or RX 6700 XT for great performance.",
    'recommend_nvidia_gpu': "We recommend NVIDIA RTX 3060 or higher for optimal gaming.",
    'recommend_ddr4': "DDR4 is great for cost-effective builds with wide compatibility.",
    'recommend_ddr5': "DDR5 offers faster speeds — ideal for new-gen systems.",
    'recommend_ssd': "We recommend NVMe SSDs for fast boot times and app loading.",
    'recommend_cpu': "Based on your needs, we suggest either Intel or AMD processors.",
    'recommend_gpu': "You may consider GPUs from NVIDIA or AMD based on your use-case.",
    'recommend_motherboard': "We recommend compatible motherboards based on your CPU choice.",
    'recommend_ram': "We suggest 16GB DDR4 or DDR5 for modern computing needs.",
    'recommend_brand': "We support recommendations for Intel, AMD, and NVIDIA brands.",
    'recommend_premium': "For premium setups, we recommend high-end CPUs, GPUs, and Gen4 SSDs."
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
