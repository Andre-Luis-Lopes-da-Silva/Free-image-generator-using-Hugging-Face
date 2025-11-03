# Free-image-generator-using-Hugging-Face

AI Image Generator with Stable Diffusion
A simple Python script that generates images from text prompts using RunwayML's Stable Diffusion v1-5 model.

**🚀 Features**
Text-to-Image Generation: Convert text descriptions into visual artwork

Automatic Device Detection: Uses GPU (CUDA) if available, otherwise falls back to CPU

Timestamped Output: Automatically saves images with unique timestamps

Performance Tracking: Measures and displays generation time

Memory Efficient: Optimized for both GPU and CPU usage

**⚙️ Technical Details**
Model: runwayml/stable-diffusion-v1-5

Supported Devices: CUDA (GPU) and CPU

Precision: FP16 on GPU, FP32 on CPU

Guidance Scale: 7.5 (balanced creativity/accuracy)

Output Format: PNG with timestamp (e.g., imagem_hf_20231201_143022.png)

**🔒 Memory Management**
The script includes low_cpu_mem_usage=True to optimize memory usage, making it suitable for systems with limited RAM.

**⚠️ Important Notes**
First execution will download the model (~5GB)

Ensure sufficient disk space is available

GPU recommended for faster generation

Generated images are saved in the current working directory

Happy creating! 🎨 Transform your imagination into visual reality with AI-powered image generation.

