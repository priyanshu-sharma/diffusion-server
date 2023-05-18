import torch
import logging
from datetime import datetime
from diffusers import StableDiffusionImg2ImgPipeline, EulerDiscreteScheduler
from PIL import Image

logger = logging.getLogger(__name__)

class BaseDiffusion:
    def __init__(self, model_id):
        self.model_id = model_id
        self.initialize_model()
    
    def _check_for_cuda_device(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return device
    
    def _get_euler_discrete_scheduler(self):
        euler_discrete_scheduler = EulerDiscreteScheduler.from_pretrained(self.model_id, subfolder="scheduler")
        return euler_discrete_scheduler
    
    def _get_img2img_pipeline(self):
        pipe = StableDiffusionImg2ImgPipeline.from_pretrained(self.model_id, scheduler=self.scheduler, torch_dtype=torch.float16)
        return pipe

    def initialize_model(self):
        self.device = self._check_for_cuda_device()
        self.scheduler = self._get_euler_discrete_scheduler()    
        self.pipe = self._get_img2img_pipeline()
        self.pipe = self.pipe.to(self.device)

    def generate_image(self, prompt, image_name_list):
        try:
            image_list = []
            for i in range(0, len(image_name_list)):
                im = Image.open(image_name_list[i])
                image_list.append(im)
            generated_image_list = self.pipe(prompt=prompt, image=image_list).images
            save_image = "{}".format(str(datetime.now()))
            count = 1
            output_dict = {}
            logger.info("Generated Images List - {}".format(len(generated_image_list)))
            for i in range(0, len(generated_image_list)):
                image = generated_image_list[0]
                name = "{}-{}.png".format(save_image, i)
                image.save(name)
                input_image = image_name_list[i]
                output_dict[input_image] = name 
                i = i + 1
            return output_dict
        except Exception as e:
            logger.info(image_list)
        