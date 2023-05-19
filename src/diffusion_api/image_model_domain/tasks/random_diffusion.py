import logging
# from image_model_domain.models import Images , DLModels
from server_config import BASE_DIR
import numpy as np
import random
import time
import psutil
from PIL import Image
from services import diffusionv14, diffusionv15, diffusionv2, diffusionv21

logger = logging.getLogger(__name__)

class RandomDiffusion:
    def __init__(self, prompt_list=["generate image of cyberpunk battleship", "cat dancing in rain", "dogs sitting on sofa", "beautiful landscape with sea and mountains"]):
        self.prefix = BASE_DIR.as_posix() + '/'
        self.MODEL_TO_SERVICE_MAP = {
            'runwayml/stable-diffusion-v1-5': diffusionv15,
            'stabilityai/stable-diffusion-2': diffusionv2,
            'stabilityai/stable-diffusion-2-1': diffusionv21,
            'CompVis/stable-diffusion-v1-4': diffusionv14
        }
        self.prompt_list = prompt_list
        self.initiate_diffusion()

    def initiate_diffusion(self):
        start_time = time.time()
        logger.info("Initializing Random Diffusion")
        self.preprocess()
        logger.info("Pre-Processing Completed")
        diffusion_dict = self.perform_diffusion()
        logger.info("Diffusion Completed")
        memory_usage = psutil.Process().memory_info().rss / 1024 ** 2
        end_time = time.time()
        logger.info("Total Time Taken - {} seconds".format(end_time - start_time))
        logger.info("Memory Usage is around - {} MB".format(memory_usage))
        return diffusion_dict

    def preprocess(self):
        # images = Images.objects.all()
        # dl_models = DLModels.objects.all()
        self.dl_models = ['runwayml/stable-diffusion-v1-5','stabilityai/stable-diffusion-2','stabilityai/stable-diffusion-2-1','CompVis/stable-diffusion-v1-4']
        self.images = ['dataset_domain/images/Default_A_side_view_of_a_samurai_cat_with_a_flat_design_Artwork_of_t_0_cc6b0aa7-de9c-4d6e-8d3a-3aebd827b1cd_1.jpg','dataset_domain/images/Default_Board_game_cafe_good_mood_with_happy_people_paper_art_style_1_0_74ea811b-feea-4a1a-abde-8587dc3f28fe_1.jpg','dataset_domain/images/Default_cute_isometric_china_town_cutaway_box_traditional_night_light_1_f48ad1f7-4067-4185-8c63-16a4290a1388_1.jpg','dataset_domain/images/Default_cute_isometric_cyberpunk_bedroom_cutaway_box_futuristic_highl_0_cf59779e-899f-4167-b106-a512f1a038e1_1.jpg','dataset_domain/images/Default_DD_cybernatic_character_rusty_metalic_hunter_armor_cyberpunk_2_6725d285-ee0e-4b16-b0fd-df73dd91e464_1.jpg','dataset_domain/images/Kre8_with_Watercolor_Magical_neon_watercolor_latte_art_intricate_design_steam_ri_1.jpg','dataset_domain/images/Leonardo_Diffusion_A_cute_Kawaii_tiny_hyper_realistic_baby_jaguar_wearing_hip_h_0 (2).jpg','dataset_domain/images/Leonardo_Diffusion_A_cute_Kawaii_tiny_hyper_realistic_baby_jaguar_wearing_hip_h_1.jpg','dataset_domain/images/Leonardo_Diffusion_back_facing_camera_soldier_holding_a_shiny_katana_in_his_han_0.jpg','dataset_domain/images/Leonardo_Diffusion_beautiful_northern_lights_vector_clipart_illustration_realis_3.jpg','dataset_domain/images/Leonardo_Diffusion_jrpg_complete_portrait_of_a_space_golden_retriever_puppie_we_0.jpg','dataset_domain/images/Leonardo_Diffusion_lightning_strikes_abstract_high_quality_UHD_Luminous_Studio_1.jpg','dataset_domain/images/Leonardo_Diffusion_Terrifying_Halloween_house_at_the_dead_of_night_bathed_in_a_1.jpg','dataset_domain/images/Leonardo_Diffusion_whimsical_detailed_close_up_portrait_victorian_brown_owl_flo_1.jpg','dataset_domain/images/Leonardo_Signature_A_image_banner_design_of_tshirt_for_a_website_1.jpg','dataset_domain/images/RPG_40_DD_cybernatic_character_rusty_metalic_hunter_armor_cyberpunk_0.jpg','dataset_domain/images/Leonardo_Diffusion_sticker_cartoon_cute_fox_white_background_Vermeer_style_12K_2.png']
        self.image_list = []
        for image in self.images:
            try:
                # image_path = image.path
                image_path = self.prefix + image
                im = Image.open(r'{}'.format(image_path))
                # im.show()
                self.image_list.append(im)
            except Exception as e:
                print("Error log for image {} - {}".format(image_path, str(e)))
                # print(image.id)
        self.image_model_index_mapping = np.random.randint(len(self.dl_models), size=len(self.image_list))
        logger.info("Image Model Index Mapping - {}".format(self.image_model_index_mapping))
    
    def perform_diffusion(self):
        diffusion_dict = {}
        image_count = 0
        for image_index in self.image_model_index_mapping:
            dl_model_name = self.dl_models[image_index]
            logger.info("Dl Model Name - {}".format(dl_model_name))
            selected_images = self.images[image_count]
            # selected_images = Image.open(selected_images)
            # selected_images = selected_images.resize((512, 512))
            # logger.info("Generating Images for model - {}".format(dl_model_name))
            prompt_index = random.randint(0, len(self.prompt_list)-1)
            prompt = self.prompt_list[prompt_index]
            logger.info("Selected Images - {} using prompt - {}".format(selected_images, prompt))
            diffusion_image = self.MODEL_TO_SERVICE_MAP[dl_model_name].generate_image(prompt, selected_images)
            diffusion_dict[self.images[image_index]] = diffusion_image
            image_count = image_count + 1
        return diffusion_dict
        # for i in range(0, len(self.dl_models)):
        #     prompt = "generate image of cyberpunk battleship"
        #     dl_model_name = self.dl_models[i]
        #     logger.info("Dl Model Name - {}".format(dl_model_name))
        #     selected_images = np.where(self.image_model_index_mapping == i)[0]
        #     logger.info("Selected Images - {}".format(selected_images))
        #     image_name_list = []
        #     for selected_image in selected_images:
        #         image_name = self.images[selected_image]
        #         image_name_list.append(image_name)
        #     logger.info("Generating Images for model - {}".format(dl_model_name))
        #     self.MODEL_TO_SERVICE_MAP[dl_model_name].generate_image(prompt, image_name_list)

