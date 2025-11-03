# Free-image-generator-using-Hugging-Face

AI Image Generator with Stable Diffusion
A simple Python script that generates images from text prompts using RunwayML's Stable Diffusion v1-5 model.

🚀 Features
Text-to-Image Generation: Convert text descriptions into visual artwork

Automatic Device Detection: Uses GPU (CUDA) if available, otherwise falls back to CPU

Timestamped Output: Automatically saves images with unique timestamps

Performance Tracking: Measures and displays generation time

Memory Efficient: Optimized for both GPU and CPU usage

📋 Prerequisites
Before running this script, ensure you have the following installed:

Python 3.7+

PyTorch

Hugging Face Diffusers

PIL (Pillow)

🔧 Installation
Install required packages:

bash
pip install torch diffusers transformers pillow
For GPU support (optional but recommended):

bash
# Install CUDA-enabled PyTorch if you have NVIDIA GPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
💻 Usage
Run the script:

bash
python your_script_name.py
Enter your prompt when prompted:

text
Descreva a imagem que deseja criar: a beautiful sunset over mountains with a lake
Wait for generation - the script will:

Load the Stable Diffusion model

Generate your image

Save it with a timestamp

Display performance metrics

⚙️ Technical Details
Model: runwayml/stable-diffusion-v1-5

Supported Devices: CUDA (GPU) and CPU

Precision: FP16 on GPU, FP32 on CPU

Guidance Scale: 7.5 (balanced creativity/accuracy)

Output Format: PNG with timestamp (e.g., imagem_hf_20231201_143022.png)

🎨 Example Prompts
Try these sample prompts to get started:

"a serene landscape with mountains and lake at sunset"

"a cyberpunk cityscape with neon lights and flying cars"

"a cute cartoon cat wearing a wizard hat"

"an astronaut riding a horse in space, photorealistic"

📊 Output
The script provides:

Generated image file with timestamp

Processing time in seconds

Used prompt for reference

Example output:

text
Imagem salva como: imagem_hf_20231201_143022.png
Tempo de processamento: 45.32 segundos
Prompt usado: a beautiful sunset over mountains with a lake
🛠️ Performance Notes
GPU: Typically 10-30 seconds generation time

CPU: Can take several minutes depending on hardware

First run: May take longer due to model downloading

Storage: Model requires ~5GB of disk space

🔒 Memory Management
The script includes low_cpu_mem_usage=True to optimize memory usage, making it suitable for systems with limited RAM.

📝 License
This script uses the Stable Diffusion v1-5 model which is subject to its own license terms. Please ensure compliance with RunwayML's model license for your use case.

⚠️ Important Notes
First execution will download the model (~5GB)

Ensure sufficient disk space is available

GPU recommended for faster generation

Generated images are saved in the current working directory

Happy creating! 🎨 Transform your imagination into visual reality with AI-powered image generation.

