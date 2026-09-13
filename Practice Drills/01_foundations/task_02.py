"""
TASK 02 — Clean Dirty Text
Level 1 (Easy)

Task: You received a batch ID full of unnecessary spaces, uppercase letters,
and underscores: "  BATCH_2024_A17  ". Clean it - remove spaces, convert to
lowercase, and replace "_" with "-". You don't have to do it all at once,
you can do it step by step.

Example:
"batch-2024-a17"

Hint: .strip() removes spaces, .lower() converts to lowercase,
.replace("_", "-") replaces underscores with dashes. Do it in order.

(By the way: this is "data cleaning" - the first step in almost every AI project.)
"""

batch_id = "  BATCH_2024_A17  "
print(f"Original batch ID: {batch_id}")

clear_batch_id = batch_id.lower().strip().replace