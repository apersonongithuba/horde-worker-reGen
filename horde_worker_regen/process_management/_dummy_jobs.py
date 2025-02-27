import random
import uuid

from horde_sdk.ai_horde_api.apimodels import (
    ImageGenerateJobPopPayload,
    ImageGenerateJobPopResponse,
    ImageGenerateJobPopSkippedStatus,
)
from horde_sdk.ai_horde_api.consts import KNOWN_SAMPLERS, KNOWN_SOURCE_PROCESSING
from horde_sdk.ai_horde_api.fields import JobID


def dummy_job_factory(model_name: str) -> ImageGenerateJobPopResponse:
    # sampler = random.choice(list(KNOWN_SAMPLERS.__members__.keys()))
    sampler = KNOWN_SAMPLERS.k_euler
    return ImageGenerateJobPopResponse(
        id=JobID(root=uuid.uuid4()),
        source_processing=KNOWN_SOURCE_PROCESSING.txt2img,
        skipped=ImageGenerateJobPopSkippedStatus(),
        model=model_name,
        payload=ImageGenerateJobPopPayload(
            sampler_name=sampler,
            cfg_scale=7.5,
            denoising_strength=1.0,
            seed="123456789",
            height=512 if model_name != "SDXL 1.0" else 1024,
            width=512 if model_name != "SDXL 1.0" else 1024,
            karras=True,
            tiling=False,
            hires_fix=False,
            clip_skip=1,
            control_type=None,
            image_is_control=False,
            return_control_map=False,
            prompt="a man walking in the snow",
            ddim_steps=30,
            n_iter=1,
        ),
    )


def get_n_dummy_jobs(n: int) -> list[ImageGenerateJobPopResponse]:
    # models_to_use = ["SDXL 1.0", "stable_diffusion", "Deliberate", "Deliberate 3.0", "Anything Diffusion"]
    models_to_use = [
        "stable_diffusion_2.1",
        "stable_diffusion",
        "waifu_diffusion",
        "Furry Epoch",
        "Yiffy",
        "Zack3D",
        "trinart",
        "Coloring Book",
        "Arcane Diffusion",
        # "Squishmallow Diffusion",
        "Spider-Verse Diffusion",
        "Archer Diffusion",
        "Elden Ring Diffusion",
        "Robo-Diffusion",
        "mo-di-diffusion",
        "Classic Animation Diffusion",
        # "Xynthii-Diffusion",
        "Comic-Diffusion",
        "Tron Legacy Diffusion",
        "Microworlds",
        "Zeipher Female Model",
        "Redshift Diffusion",
        "Borderlands",
        "Cyberpunk Anime Diffusion",
        "OpenJourney Diffusion",
        "Papercut Diffusion",
        "AIO Pixel Art",
        "JWST Deep Space Diffusion",
        "App Icon Diffusion",
        "Mega Merge Diffusion",
        "Voxel Art Diffusion",
        "Van Gogh Diffusion",
        "Anything Diffusion",
        "BubblyDubbly",
        "Dungeons and Diffusion",
        "Clazy",
        "Nitro Diffusion",
        "Samdoesarts Ultmerge",
        "Synthwave",
        "vectorartz",
        "Ranma Diffusion",
        "Ghibli Diffusion",
        "Hentai Diffusion",
        "Guohua Diffusion",
        "Inkpunk Diffusion",
        "Fantasy Card Diffusion",
        "Knollingcase",
        "Midjourney PaintArt",
        "RPG",
        "Poison",
        "Eimis Anime Diffusion",
        "Wavyfusion",
        "Papercutcraft",
        "kurzgesagt",
        "ChromaV5",
        "Dreamlike Diffusion",
        "Analog Diffusion",
        "Asim Simpsons",
        "Funko Diffusion",
        "Double Exposure Diffusion",
        "Microscopic",
        "Balloon Art",
        "Future Diffusion",
        "Seek.art MEGA",
        "Valorant Diffusion",
        "Hassanblend",
        "ACertainThing",
        "GTA5 Artwork Diffusion",
        "Trinart Characters",
        "Smoke Diffusion",
        "Supermarionation",
        "Dreamlike Photoreal",
        "PortraitPlus",
        "Vintedois Diffusion",
        "Darkest Diffusion",
        "Eternos",
        "Min Illust Background",
        "Dark Victorian Diffusion",
        "DnD Item",
        "ModernArt Diffusion",
        "HASDX",
        "Liberty",
        "ProtoGen",
        "3DKX",
        # "Moedel",
        "DreamLikeSamKuvshinov",
        "Sygil-Dev Diffusion",
        "MoistMix",
        "Healy's Anime Blend",
        "GuFeng",
        # "Elldreth's Lucid Mix",
        "Sci-Fi Diffusion",
        "Ultraskin",
        "Sonic Diffusion",
        "PPP",
        "Anygen",
        "Protogen Infinity",
        "DucHaiten",
        "Dreamshaper",
        "Zelda BOTW",
        "Marvel Diffusion",
        "T-Shirt Diffusion",
        "Lawlas's yiff mix",
        "DGSpitzer Art Diffusion",
        "Realistic Vision",
        "Dan Mumford Style",
        "PFG",
        "Epic Diffusion",
        "Deliberate",
        "Edge Of Realism",
        "Concept Sheet",
        "CharHelper",
        "Pokemon3D",
        # "pix2pix",
        "Vivid Watercolors",
        "Counterfeit",
        "Openniji",
        "Pastel Mix",
        "Pulp Vector Art",
        "Rainbowpatch",
        "Vector Art",
        "T-Shirt Print Designs",
        "GorynichMix",
        "Laolei New Berry Protogen Mix",
        "URPM",
        "Cheese Daddys Landscape Mix",
        "Rachel Walker Watercolors",
        "Project Unreal Engine 5",
        "Unstable Ink Dream",
        "PRMJ",
        # "Elldreths Retro Mix",
        "VinteProtogenMix",
        "Rodent Diffusion",
        "Anything v3",
        "Woop-Woop Photo",
        "Abyss OrangeMix",
        "CyriousMix",
        "Microcasing",
        "ChilloutMix",
        "Microchars",
        "Microcritters",
        "AbyssOrangeMix-AfterDark",
        "Grapefruit Hentai",
        "Experience",
        "Kenshi",
        "DucHaiten Classic Anime",
        "Rev Animated",
        "526Mix-Animated",
        "A to Zovya RPG",
        "Colorful",
        "Movie Diffusion",
        "GuoFeng",
        "Anime Pencil Diffusion",
        "BPModel",
        "UMI Olympus",
        "HRL",
        "Uhmami",
        "Neurogen",
        "NeverEnding Dream",
        "Protogen Anime",
        "SynthwavePunk",
        "Graphic-Art",
        "Illuminati Diffusion",
        "SD-Silicon",
        "FKing SciFi",
        "RealBiter",
        "FaeTastic",
        "OrbAI",
        "Realism Engine",
        "Jim Eidomode",
        "Dungeons n Waifus",
        "iCoMix",
        "TrexMix",
        "Pretty 2.5D",
        "ExpMix Line",
        "Disco Elysium",
        "Something",
        "RCNZ Dumb Monkey",
        "PIXHELL",
        "Korestyle",
        "PVC",
        "Aurora",
        "Char",
        "CamelliaMix 2.5D",
        "Perfect World",
        "JoMad Diffusion",
        "RCNZ Gorilla With A Brick",
        "Ether Real Mix",
        "Lyriel",
        "DnD Map Generator",
        "BRA",
        "MoonMix Fantasy",
        "ICBINP - I Can't Believe It's Not Photography",
        "BB95 Furry Mix",
        "MeinaMix",
        "Mistoon Amethyst",
        "Art Of Mtg",
        "Galena Redux",
        "Analog Madness",
        "Henmix Real",
        "Elysium Anime",
        "majicMIX realistic",
        "GhostMix",
        "Hassaku",
        "Dark Sushi Mix",
        "CyberRealistic",
        # "Realistic Vision Inpainting",
        # "Deliberate Inpainting",
        # "stable_diffusion_inpainting",
        "Disney Pixar Cartoon Type A",
        "Babes",
        # "DreamShaper Inpainting",
        # "A-Zovya RPG Inpainting",
        "BweshMix",
        "Cetus-Mix",
        "Real Dos Mix",
        "Realisian",
        # "Epic Diffusion Inpainting",
        # "Anything Diffusion Inpainting",
        "Fluffusion",
        "Anything v5",
        "ToonYou",
        "Reliberate",
        "SweetBoys 2D",
        # "iCoMix Inpainting",
        "Samaritan 3d Cartoon",
        "AnyLoRA",
        "Western Animation Diffusion",
        "Deliberate 3.0",
        "SDXL 1.0",
    ]

    # models_to_use = ["SDXL 1.0", "Deliberate", "Deliberate 3.0"]
    # models_to_use = ["Deliberate", "Deliberate 3.0", "Anything Diffusion"]
    # models_to_use = ["Deliberate"]
    # if 2, return one of each model
    if n == 2:
        return [dummy_job_factory(model_name) for model_name in models_to_use]

    # otherwise, return a random selection of models
    return [dummy_job_factory(random.choice(models_to_use)) for _ in range(n)]
