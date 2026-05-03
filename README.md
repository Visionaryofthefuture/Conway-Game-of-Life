# 🧬 Conway’s Game of Life (Pygame)

A simple implementation of Conway’s Game of Life built using Python and Pygame.  
Click to toggle cells, press space to run the simulation, and watch chaos unfold.

---

## 🚀 What this is

This project is a grid-based simulation of Conway’s Game of Life, a zero-player game where patterns evolve based on a few simple rules.

You don’t “play” it — you set it up and let it run.

---

## Features

- Interactive grid (click to toggle cells)
- Real-time simulation
- Clean visual rendering using Pygame
- Simple and readable logic

---

## 🧠 Rules of the Game

Each cell on the grid is either **alive** or **dead**, and evolves based on its neighbors:

1. Any live cell with fewer than 2 live neighbors → dies
2. Any live cell with 2 or 3 neighbors → survives
3. Any live cell with more than 3 neighbors → dies
4. Any dead cell with exactly 3 neighbors → becomes alive

---

## 🖥️ Controls

- 🖱️ **Mouse Click** → Toggle a cell (alive ↔ dead)
- ␣ **Spacebar** → Start / Pause simulation

---

## 📦 Installation

Make sure you have Python installed (3.x recommended).

Install dependencies:

```bash
pip install pygame
```
Run using the folowing command 
```bash
python main.py
