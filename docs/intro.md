# CNNs and Feature Maps — A Primer

## 1) What is a CNN?

A **Convolutional Neural Network** is a deep learning architecture built to handle grid‑like data such as images. CNNs are powerful because they combine three main principles:

* **Locality** — kernels (filters) look only at small neighborhoods of the input.
* **Weight sharing** — the same kernel slides across the whole input, greatly reducing parameters.
* **Hierarchy** — early layers learn edges and textures, later layers combine them into shapes, and deeper layers recognize objects.

### The Convolution Operation

For an input patch $X$ and a kernel $K$, the output cell at position $(i,j)$ is:

$$
Y[i,j] = \sum_{u,v} X[i+u, j+v] \cdot K[u,v]
$$

This sliding multiply‑sum is the essence of CNNs.

---

## 2) What is a Feature Map?

After convolving an input with a kernel and passing it through a nonlinearity (like ReLU), we obtain a **feature map**:

* Each number indicates how strongly the kernel’s pattern appears at that location.
* Different kernels detect different primitives (edges, corners, blobs).
* Stacking many feature maps creates a rich representation of the input.

Think of feature maps as layers of “pattern detectors” that build up from simple to complex.

---

## 3) Episode 1 in This Repo

This repository animates the most basic case:

* A **3×3 kernel** scanning a **5×5 input** (stride 1, valid padding).
* At each step, elementwise multiply and sum → write to the output cell.
* The result is a **3×3 feature map**, showing the kernel’s detection strength across the input.

Next steps will cover: padding & stride, pooling, activations, and finally loss/backpropagation to train CNNs.
