🧠 CNN Animations

Animations that explain the building blocks of Convolutional Neural Networks (CNNs), step by step.

📌 Why CNNs?

A Convolutional Neural Network (CNN) is a special kind of deep learning model designed to work with grid-like data such as images or audio spectrograms.

CNNs use three key ideas:

🔎 Local receptive fields – small filters (kernels) look at small neighborhoods in the data

♻️ Weight sharing – the same kernel slides everywhere, reducing parameters

🏗 Hierarchy of features – shallow layers learn edges/textures, deeper layers learn shapes/objects

🌊 What is a Feature Map?

When you apply a kernel to an input and then pass the result through a nonlinearity (like ReLU), you get a feature map:

It highlights where the filter’s pattern (e.g., vertical edge) appears in the input

Different kernels produce different feature maps (edges, corners, blobs)

Stacking many maps across channels builds a rich representation of the input

Think of feature maps as the “eyes” of the CNN—each filter looking for its own pattern.

🎬 Episode 1 — Convolution

In this repo, we start with the most fundamental operation: 2D Convolution.

Input: 5×5 grid

Kernel: 3×3 filter

Padding: valid (no padding)

Stride: 1

At each position, the kernel slides across the input:

Multiply each overlapping pair (input × kernel)

Sum them all → one number

Place that number in the output grid

This produces a 3×3 feature map, which encodes how strongly the kernel’s pattern appears at each location.

📜 License

MIT — free to use and share