"""
TASK 04 — How Much Does an AI Model Call Cost
Level 3 (AI Application)

Task: You want to know in advance how much a single AI model call will cost,
based on the number of tokens. The price is calculated per 1000 tokens.

input_tokens = 1200
output_tokens = 350
price_per_1k_input = 0.003
price_per_1k_output = 0.015

Example:
Estimated cost: $0.00885

Hint: First divide the tokens by 1000, then multiply by the price - separately for
input and output, then add the two together.

(By the way: this is what "cost tracking" looks like in real AI automations.)
"""

input_tokens = 1200
output_tokens = 350
price_per_1k_input = 0.003
price_per_1k_output = 0.015

input_estimated_cost = (input_tokens / 1000) * price_per_1k_input
output_estimated_cost = (output_tokens / 1000) * price_per_1k_output

estimated_cost = input_estimated_cost + output_estimated_cost

print(f"Input estimated cost: {input_estimated_cost}\n"
      f"Output estimated cost: {output_estimated_cost}\n"
      f"Estimated cost: {estimated_cost}")