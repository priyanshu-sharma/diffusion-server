import logging
from image_model_domain.models import Images, DLModels
from server_config import BASE_DIR
from PIL import Image

logger = logging.getLogger(__name__)

class RandomDiffusion:
    def __init__(self):
        self.prefix = BASE_DIR.as_posix() + '/'
        logger.info("Initializing Random Diffusion")

    def process(self):
        images = Images.objects.all()
        dl_models = DLModels.objects.all()
        for image in images:
            try:
                image_path = image.path
                image_path = self.prefix + image_path
                im = Image.open(r'{}'.format(image_path))
                im.show()
            except Exception as e:
                print(image_path)
                print(image.id)

random_diffusion = RandomDiffusion()
random_diffusion.process()