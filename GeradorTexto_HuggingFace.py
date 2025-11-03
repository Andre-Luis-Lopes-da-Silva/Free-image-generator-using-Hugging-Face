import time
from datetime import datetime
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline

# Prompt do usuário
prompt = input("Descreva a imagem que deseja criar: ")

# Marca o início do processamento
inicio = time.time()

# Carrega o modelo (usando versão gratuita via CPU ou GPU, se disponível)
model_id = "runwayml/stable-diffusion-v1-5"  # modelo popular

# Se você tiver GPU, use torch.device("cuda")
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
   torch_dtype=torch.float16 if device=="cuda" else torch.float32,
    low_cpu_mem_usage=True
)
pipe = pipe.to(device)

# Gera a imagem
image = pipe(prompt, guidance_scale=7.5).images[0]

# Marca o fim e calcula o tempo
fim = time.time()
tempo_processamento = fim - inicio

# Salva a imagem com timestamp
nome_arquivo = f"imagem_hf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
image.save(nome_arquivo)

# Exibe a imagem
image.show()

# Mostra resumo
print(f"\nImagem salva como: {nome_arquivo}")
print(f"Tempo de processamento: {tempo_processamento:.2f} segundos")
print(f"Prompt usado: {prompt}")
