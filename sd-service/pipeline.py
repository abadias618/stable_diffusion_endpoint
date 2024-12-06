from diffusers import DiffusionPipeline
import torch

class Pipeline:
    def __init__(self):
        self.model_name = "stabilityai/stable-diffusion-xl-base-1.0"
        
    def load_pipeline(self):
        print(f"start {self.model_name} model download...")
        pipe = DiffusionPipeline.from_pretrained(self.model_name, torch_dtype=torch.float16).to("cuda")
        print("end download.")
        
        print("Loading LoRa weights...")
        pipe.load_lora_weights("nerijs/pixel-art-xl", weight_name="pixel-art-xl.safetensors", adapter_name="pixel")
        print("Setting Adapters...")
        pipe.set_adapters("pixel")
        print("DONE with Pipeline.")
        return pipe