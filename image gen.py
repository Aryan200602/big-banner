# -*- coding: utf-8 -*-
"""Untitled35.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yokEWFdNwejEl4Miz33kHtahOYckwKxI
"""

!pip install transformers torch huggingface_hub

from transformers import pipeline
from huggingface_hub import login

# Get your Hugging Face token from https://huggingface.co/settings/tokens
login("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")

from huggingface_hub import login
login("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")

login("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", add_to_git_credential=True)

!pip install diffusers

from diffusers import StableDiffusionPipeline

# Load the model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Make sure you're using a GPU

# Generate an image based on a prompt
image = generator("A sunset over a mountain range").images[0]
image.show()  # Display the image

from diffusers import StableDiffusionPipeline

# Load the model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Now it should find the GPU

# Generate an image based on a prompt
image = generator("A sunset over a mountain range").images[0]
image.show()  # Display the image

!pip install diffusers

from diffusers import StableDiffusionPipeline

# Load the model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Use GPU if available

# Generate an image based on a prompt
image = generator("A sunset over a mountain range").images[0]
image.show()  # Display the image

from diffusers import StableDiffusionPipeline

# Load the pre-trained Stable Diffusion model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Use GPU for faster processing

# Generate an image based on a prompt
prompt = "A futuristic cityscape at sunset"
image = generator(prompt).images[0]

# Display the generated image
image.show()

# Generate an image based on a prompt
prompt = "A futuristic cityscape at sunset"
image = generator(prompt).images[0]

# Display the generated image
image.show()

from diffusers import StableDiffusionPipeline
import torch

# Check if GPU is available
if not torch.cuda.is_available():
    print("CUDA is not available. Ensure that you have a GPU enabled.")
else:
    print("CUDA is available. Proceeding with GPU.")

# Load the pre-trained Stable Diffusion model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Send to GPU

# Generate an image based on a prompt
prompt = "A futuristic cityscape at sunset"
print("Generating the image...")

# Generate the image with the model
result = generator(prompt)

# Check if result is successful
if result and result.images:
    # Display the generated image
    image = result.images[0]
    image.show()
else:
    print("Image generation failed. Please check the model and prompt.")

from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import matplotlib.pyplot as plt

# Check if GPU is available
if not torch.cuda.is_available():
    print("CUDA is not available. Ensure that you have a GPU enabled.")
else:
    print("CUDA is available. Proceeding with GPU.")

# Load the pre-trained Stable Diffusion model
generator = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
generator.to("cuda")  # Send to GPU

# Generate an image based on a prompt
prompt = "Sanket from Bennett University"
print("Generating the image...")

# Generate the image with the model
result = generator(prompt)

# Check if the result is successful
if result and result.images:
    # Save the image and display it
    image = result.images[0]

    # Save image locally
    image.save("generated_image.png")

    # Display image using matplotlib
    plt.imshow(image)
    plt.axis("off")  # Turn off axis
    plt.show()
else:
    print("Image generation failed. Please check the model and prompt.")