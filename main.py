# from happytransformer import HappyGeneration
# from happytransformer import GENSettings
#
# happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-2.7B")
#
# args = GENSettings(min_length=50, max_length=50, do_sample=True, temperature=0.9)
#
# result = happy_gen.generate_text("how to get rich", args=args)
#
# print(result.text)

from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
post = "implementing a linked list"
result = generator(post, max_length=500, do_sample=True, temperature=0.9)

print(result[0]['generated_text'])
