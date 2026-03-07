from __future__ import annotations

import importlib.machinery
import sys
import types


def ensure_torchvision_stub() -> None:
    try:
        import torchvision  # type: ignore  # noqa: F401
        return
    except Exception:
        pass

    tv = types.ModuleType("torchvision")
    tv.__spec__ = importlib.machinery.ModuleSpec("torchvision", loader=None)

    transforms = types.ModuleType("torchvision.transforms")
    transforms.__spec__ = importlib.machinery.ModuleSpec("torchvision.transforms", loader=None)

    class InterpolationMode:
        NEAREST = "nearest"
        NEAREST_EXACT = "nearest_exact"
        BILINEAR = "bilinear"
        BICUBIC = "bicubic"
        BOX = "box"
        HAMMING = "hamming"
        LANCZOS = "lanczos"

    transforms.InterpolationMode = InterpolationMode
    tv.transforms = transforms

    for name in ("_meta_registrations", "datasets", "io", "models", "ops", "utils"):
        module = types.ModuleType(f"torchvision.{name}")
        module.__spec__ = importlib.machinery.ModuleSpec(f"torchvision.{name}", loader=None)
        setattr(tv, name, module)
        sys.modules.setdefault(f"torchvision.{name}", module)

    sys.modules["torchvision"] = tv
    sys.modules["torchvision.transforms"] = transforms
