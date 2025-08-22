# 🧠 CNN Animations

Short, focused animations that explain core **Convolutional Neural Network** ops.

<p align="center">
  <img src="exports/gif/conv2d_valid.gif" width="520" alt="Convolution animation preview"/>
</p>

## What is a CNN?

A **CNN** processes grid-like data (e.g., images) using small sliding filters (kernels) with **shared weights** to detect local patterns.

## What is a Feature Map?

A **feature map** is the 2-D array after a convolution (and usually an activation). Large values indicate the filter’s pattern is present.

## 🎬 Episode 1 — Convolution

We slide a **3×3 kernel** over a **5×5 input** (valid padding, stride 1).  
At each position we **multiply & sum** the window × kernel and write the result to the output cell.

## 🗂 Layout
cnn-animations/
README.md
docs/intro.md
manim_scenes/
exports/gif/
exports/mp4/
scripts/
requirements.txt
.gitignore