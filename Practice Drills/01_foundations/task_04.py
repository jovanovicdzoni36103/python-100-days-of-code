"""
TASK 04 — Koliko košta poziv AI modela
Level 3 (AI primena)

Zadatak: Hoćeš unapred da znaš koliko će koštati jedan poziv ka AI
modelu, na osnovu broja tokena. Cena se računa na 1000 tokena.

input_tokens = 1200
output_tokens = 350
price_per_1k_input = 0.003
price_per_1k_output = 0.015

Primer:
Estimated cost: $0.00885

Hint: prvo podeli tokene sa 1000, pa pomnoži cenom - posebno za
input, posebno za output, pa to dvoje saberi.

(Usput: ovako izgleda "cost tracking" u realnim AI automatizacijama.)
"""

# Napiši rešenje ispod ove linije:

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