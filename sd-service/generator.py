from pipeline import Pipeline
import torch
import random

class Generator:
    def __init__(self) -> None:
        self.pipe = Pipeline().load_pipeline()
        
    def generate_img_from_prompt(self, prompt: str, lora_scale = 0.9):
        print("Start Image Generation...")
        image = self.pipe(
            prompt, num_inference_steps=30, cross_attention_kwargs={"scale": lora_scale}, generator=torch.manual_seed(random.randint(0,10000))
        ).images[0]
        print("DONE generating image.")
        img_name = "test_"+str(random.randint(0,10000))+".jpg"
        image.save(img_name)
        image.close()
        print("saved as:",img_name)
        return img_name
        