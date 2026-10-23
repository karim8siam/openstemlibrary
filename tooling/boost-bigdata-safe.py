#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")

u5_safe = r"""
## 5.19 Practical Hyperparameter Selection in Production Deep Learning

When engineering large-scale statistical pipelines using stochastic optimizers like Adam, RMSprop, or SGD with momentum, tuning hyperparameters requires disciplined cross-validation protocols:
1. **Batch Size Selection**: Increasing batch size $B$ from 32 to 1024 improves GPU arithmetic intensity, but reduces the gradient noise that helps stochastic trajectories escape sharp local minima. When scaling batch size by a factor of $k$, apply the **Linear Learning Rate Scaling Rule** (Goyal et al. 2017): set the initial learning rate to $k \cdot \eta_0$ to preserve the effective variance of weight updates per epoch.
2. **Adam Epsilon Tuning**: The numerical stabilization constant $\epsilon$ in Adam is often defaulted to $10^{-8}$. However, in models with small gradient norms or half-precision (FP16/BF16) arithmetic, $10^{-8}$ can trigger numerical instability; increasing $\epsilon$ to $10^{-4}$ or $10^{-6}$ often dramatically stabilizes convergence.
3. **Weight Decay vs $L_2$ Regularization**: In adaptive optimizers (AdamW vs Adam), decoupling weight decay from the gradient update step preserves proper scale-invariant shrinkage, preventing weights from growing unbounded in directions with small historical gradients.
"""

u6_safe = r"""
## 6.18 Software Ecosystem and Distributed Linear Algebra Libraries

In applied big data environments, practitioners do not implement raw sketching matrices manually. They rely on optimized numerical linear algebra software libraries:
- **SciPy and LAPACK**: Provide optimized multithreaded OpenBLAS/MKL routines for exact matrix decompositions, ideal for matrices up to $10,000 \times 10,000$.
- **Facebook FAISS (Facebook AI Similarity Search)**: Industry-standard C++ library for high-performance vector similarity search using hierarchical k-means quantization (IVF-PQ) and GPU-accelerated inner product embeddings.
- **ScaLAPACK and Elemental**: Distributed-memory MPI libraries for high-performance computing clusters that distribute dense matrix blocks across 2D grid meshes.
- **CuPy and PyTorch Tensor**: GPU-native libraries executing parallel matrix sketching, batched QR factorizations, and singular value decompositions on Nvidia CUDA cores with teraflop throughput.
"""

append_to_unit(5, u5_safe)
append_to_unit(6, u6_safe)
print("Safe boost applied.")
