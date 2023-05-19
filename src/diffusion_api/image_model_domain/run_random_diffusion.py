import logging
from image_model_domain.tasks import RandomDiffusion

# Add more prompts in prompt list to get the related output
# 

logger = logging.getLogger(__name__)
prompt_list = [ "cat dancing in rain"]
random_diffusion = RandomDiffusion(prompt_list)
logger.info("Random Diffusion Output - {}".format(random_diffusion))