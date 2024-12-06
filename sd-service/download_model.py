from diffusers import DiffusionPipeline
import torch
import os

pipe_id = "stabilityai/stable-diffusion-xl-base-1.0"
print(f"start {pipe_id} model download...")
pipe = DiffusionPipeline.from_pretrained(pipe_id, torch_dtype=torch.float16)
print("end download.")

save_dir = "sd-service/models/stable-diffusion-xl-base-1.0"
pipe.save_pretrained(save_dir)
print("saved to:",save_dir)

del pipe