# 🧠 CNN Animations


Animations that explain the building blocks of **Convolutional Neural Networks (CNNs)**, step by step.


<p align="center">
<img src="exports/gif/conv2d_valid.gif" width="520" alt="Convolution animation preview"/>
</p>


---


## 📌 Why CNNs?


A **Convolutional Neural Network (CNN)** is a deep learning model designed for grid‑like data such as images or audio spectrograms. CNNs:


- 🔎 Use **local receptive fields** (kernels look at small patches)
- ♻️ Apply **weight sharing** (the same kernel slides everywhere)
- 🏗 Build a **hierarchy of features** (edges → textures → shapes → objects)


---


## 🌊 What is a Feature Map?


After applying a kernel and an activation (e.g., ReLU), you get a **feature map**:


- Highlights where the kernel’s pattern appears
- Different kernels → different feature maps (edges, corners, textures)
- Stacking many maps builds rich image representations


---


## 🎬 Episode 1 — Convolution


We start with the most fundamental operation: **2D Convolution**.


- Input: **5×5 grid**
- Kernel: **3×3 filter**
- Padding: **valid**
- Stride: **1**


At each step:
1. Multiply input × kernel (elementwise)
2. Sum them up → one output cell
3. Slide to the next position


This produces a **3×3 feature map**, encoding the presence of the kernel’s pattern across the input.


---


## 📖 Want more details?


See the long‑form explanation here: **[docs/intro.md](docs/intro.md)**


---


## 🛣 Roadmap


- [x] Episode 1 — Convolution
- [ ] Episode 2 — Padding & Stride
- [ ] Episode 3 — Pooling (Max/Average)
- [ ] Episode 4 — Activations (ReLU, Sigmoid, …)
- [ ] Episode 5 — Loss & Backpropagation overview


---


## 📜 License


MIT — free to use and share.