from happytransformer import HappyGeneration
from happytransformer import GENSettings

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-2.7B")

args = GENSettings(min_length=500, max_length=500, no_repeat_ngram_size=2,
                   do_sample=True, early_stopping=False, top_k=50, temperature=0.7)

result = happy_gen.generate_text("How to learn how to code", args=args)

print(result.text)
