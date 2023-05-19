# import torch
# from diffusers import StableDiffusionImg2ImgPipeline, EulerDiscreteScheduler
# from datetime import datetime
# from PIL import Image
import logging

logger = logging.getLogger(__name__)

# class DiffusionV2:
#     def __init__(self):
#         self.model_id = "stabilityai/stable-diffusion-2"
#         self.device = "cuda" if torch.cuda.is_available() else "cpu"
#         self.scheduler = EulerDiscreteScheduler.from_pretrained(self.model_id, subfolder="scheduler")
#         self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(self.model_id, scheduler=self.scheduler, torch_dtype=torch.float16)
#         self.pipe = self.pipe.to(self.device)
#         logger.info("Stable Diffusion V2 Loaded")

#     def perform_diffusion(self, prompt, input_image):
#         generated_image = self.pipe(prompt).input_image
#         saved_image = input_image + str(datetime.now())
#         generated_image.save("{}".format(saved_image))
#         im = Image.open(r'{}'.format(image_path))
#         im.show()
#         time.sleep(5)
#         im.close()

from services import BaseDiffusion

class DiffusionV2(BaseDiffusion):
  def __init__(self):
    self.model_id = "stabilityai/stable-diffusion-2"
    super().__init__(self.model_id)
    logger.info("Stable Diffusion V2 Loaded")
  
#   def initialize_model(self):
#     raise NotImplementedError

  # def generate_image(self, prompt, image_list):
  #   super().generate_image(prompt, image_list)