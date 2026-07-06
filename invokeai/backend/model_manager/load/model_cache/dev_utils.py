from contextlib import contextmanager

import torch

from invokeai.backend.util.logging import InvokeAILogger


@contextmanager
def log_operation_vram_usage(operation_name: str):
    """A helper function for tuning working memory requirements for memory-intensive ops.

    Sample usage:

    ```python
    with log_operation_vram_usage("some_operation"):
        some_operation()
    ```
    """
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        torch.cuda.reset_peak_memory_stats()
        max_allocated_before = torch.cuda.max_memory_allocated()
        max_reserved_before = torch.cuda.max_memory_reserved()
        use_xpu = False
    elif hasattr(torch, "xpu") and torch.xpu.is_available():
        torch.xpu.synchronize()
        torch.xpu.reset_peak_memory_stats()
        max_allocated_before = torch.xpu.max_memory_allocated()
        max_reserved_before = torch.xpu.max_memory_reserved()
        use_xpu = True
    else:
        max_allocated_before = 0
        max_reserved_before = 0
        use_xpu = None

    try:
        yield
    finally:
        if use_xpu is True:
            torch.xpu.synchronize()
            max_allocated_after = torch.xpu.max_memory_allocated()
            max_reserved_after = torch.xpu.max_memory_reserved()
        elif use_xpu is False:
            torch.cuda.synchronize()
            max_allocated_after = torch.cuda.max_memory_allocated()
            max_reserved_after = torch.cuda.max_memory_reserved()
        else:
            max_allocated_after = max_allocated_before
            max_reserved_after = max_reserved_before
        logger = InvokeAILogger.get_logger()
        logger.info(
            f">>>{operation_name} Peak VRAM allocated: {(max_allocated_after - max_allocated_before) / 2**20} MB, "
            f"Peak VRAM reserved: {(max_reserved_after - max_reserved_before) / 2**20} MB"
        )
