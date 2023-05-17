import logging
# from image_model_domain.models import Images , DLModels
from server_config import BASE_DIR
from PIL import Image

logger = logging.getLogger(__name__)

class RandomDiffusion:
    def __init__(self):
        self.prefix = BASE_DIR.as_posix() + '/'
        logger.info("Initializing Random Diffusion")

    def process(self):
        # images = Images.objects.all()
        # dl_models = DLModels.objects.all()
        images = ['dataset_domain/images/Default_A_side_view_of_a_samurai_cat_with_a_flat_design_Artwork_of_t_0_cc6b0aa7-de9c-4d6e-8d3a-3aebd827b1cd_1.jpg','dataset_domain/images/Default_Board_game_cafe_good_mood_with_happy_people_paper_art_style_1_0_74ea811b-feea-4a1a-abde-8587dc3f28fe_1.jpg','dataset_domain/images/Default_cute_isometric_china_town_cutaway_box_traditional_night_light_1_f48ad1f7-4067-4185-8c63-16a4290a1388_1.jpg','dataset_domain/images/Default_cute_isometric_cyberpunk_bedroom_cutaway_box_futuristic_highl_0_cf59779e-899f-4167-b106-a512f1a038e1_1.jpg','dataset_domain/images/Default_DD_cybernatic_character_rusty_metalic_hunter_armor_cyberpunk_2_6725d285-ee0e-4b16-b0fd-df73dd91e464_1.jpg','dataset_domain/images/Kre8_with_Watercolor_Magical_neon_watercolor_latte_art_intricate_design_steam_ri_1.jpg','dataset_domain/images/Leonardo_Diffusion_A_cute_Kawaii_tiny_hyper_realistic_baby_jaguar_wearing_hip_h_0 (2).jpg','dataset_domain/images/Leonardo_Diffusion_A_cute_Kawaii_tiny_hyper_realistic_baby_jaguar_wearing_hip_h_1.jpg','dataset_domain/images/Leonardo_Diffusion_back_facing_camera_soldier_holding_a_shiny_katana_in_his_han_0.jpg','dataset_domain/images/Leonardo_Diffusion_beautiful_northern_lights_vector_clipart_illustration_realis_3.jpg','dataset_domain/images/Leonardo_Diffusion_jrpg_complete_portrait_of_a_space_golden_retriever_puppie_we_0.jpg','dataset_domain/images/Leonardo_Diffusion_lightning_strikes_abstract_high_quality_UHD_Luminous_Studio_1.jpg','dataset_domain/images/Leonardo_Diffusion_Terrifying_Halloween_house_at_the_dead_of_night_bathed_in_a_1.jpg','dataset_domain/images/Leonardo_Diffusion_whimsical_detailed_close_up_portrait_victorian_brown_owl_flo_1.jpg','dataset_domain/images/Leonardo_Signature_A_image_banner_design_of_tshirt_for_a_website_1.jpg','dataset_domain/images/RPG_40_DD_cybernatic_character_rusty_metalic_hunter_armor_cyberpunk_0.jpg','dataset_domain/images/Leonardo_Diffusion_sticker_cartoon_cute_fox_white_background_Vermeer_style_12K_2.png']
        for image in images:
            try:
                # image_path = image.path
                image_path = self.prefix + image
                im = Image.open(r'{}'.format(image_path))
                im.show()
            except Exception as e:
                print(image_path)
                # print(image.id)

random_diffusion = RandomDiffusion()
random_diffusion.process()