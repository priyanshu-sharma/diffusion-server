from services.base_diffusion import BaseDiffusion
from services.stable_diffusion_v1_4 import DiffusionV14
from services.stable_diffusion_v1_5 import DiffusionV15
from services.stable_diffusion_v2_1 import DiffusionV21
from services.stable_diffusion_v2 import DiffusionV2

diffusionv14 = DiffusionV14()
diffusionv15 = DiffusionV15()
diffusionv21 = DiffusionV21()
diffusionv2 = DiffusionV2()

__all__ = (diffusionv14, diffusionv15, diffusionv21, diffusionv2)