# 🧠 CNN Animations

Short, focused animations that explain core **Convolutional Neural Network** ops.

<p align="center">
  <img src="exports/gif/conv2d_valid.gif" width="520" alt="Convolution animation preview"/>
</p>

## What is a CNN?

A **CNN** is a neural network designed for grid-like data (images, audio spectrograms…).  
It uses small sliding filters (kernels) with shared weights to extract local patterns.

## What is a Feature Map?

A **feature map** is the 2D output after a convolution + activation.  
It highlights where the kernel’s pattern is found in the input.

---

## 🎬 Episode 1 — Convolution

We slide a **3×3 kernel** over a **5×5 input** (valid padding, stride 1).  
At each step we multiply and sum the window × kernel → one output cell.

---

## 🗂 Layout
cnn-animations/
README.md
docs/
intro.md
manim_scenes/
exports/gif/
exports/mp4/
scripts/
requirements.txt
.gitignore

Copy
Edit
