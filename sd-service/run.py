from generator import Generator
import torch

class Run:
    def __init__(self):
        pass

    def run(self, prompt):
        print(f"using prompt: \"{prompt}\"")
        torch.cuda.empty_cache()
        generator = Generator()
        file = generator.generate_img_from_prompt(prompt)
        return file
