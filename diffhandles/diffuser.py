from typing import List

import torch

class Diffuser:
    
    def __init__(self):
        pass

    def to(self, device: torch.device = None, dtype: torch.dtype = None):
        raise NotImplementedError

    @staticmethod
    def get_depth_intrinsics(h: int, w: int):
        """
        Return intrinsics suitable for the input depth.
        """
        raise NotImplementedError

    @torch.no_grad()
    def initial_inference(self, latents: torch.Tensor, depth: torch.Tensor, uncond_embeddings: torch.Tensor, prompt: str, phrases: List[str]):
        raise NotImplementedError

    @torch.no_grad()
    def guided_inference(
            self, latents: torch.Tensor, depth: torch.Tensor, uncond_embeddings: torch.Tensor, prompt: str, phrases: List[str],
            attention_maps_orig: torch.Tensor, activations_orig: torch.Tensor, activations2_orig: torch.Tensor, activations3_orig: torch.Tensor):
        raise NotImplementedError
