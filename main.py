########################################
# STANDALONE UNCONTAINERIZED RAW PROGRAM
########################################
from diffusers import DiffusionPipeline
from PIL import Image
import torch

pipe_id = "stabilityai/stable-diffusion-xl-base-1.0"

pipe = DiffusionPipeline.from_pretrained(pipe_id, torch_dtype=torch.float16).to("cuda")
pipe.load_lora_weights("nerijs/pixel-art-xl", weight_name="pixel-art-xl.safetensors", adapter_name="pixel")
pipe.set_adapters("pixel")

prompt = "toy_face of a knigh in black armor"

lora_scale = 0.9
image = pipe(
    prompt, num_inference_steps=30, cross_attention_kwargs={"scale": lora_scale}, generator=torch.manual_seed(0)
).images[0]
print(image)
image.save("test2.jpg")
image.close()

# run "pip install diffusers["torch"] transformers" to install
# for some reason had to "pip install -U peft"