# 🐺 Wolfenstein-3D (Modern OpenGL Edition)

A simple 3D first-person shooter inspired by the classic **Wolfenstein 3D** — built with **Pygame** and **ModernGL**.

This project demonstrates:

* Ray casting–based shooting & visibility
* Grid-based pathfinding (BFS)
* Instanced rendering (doors, NPCs, HUD, items)
* Texture arrays & sprite sheets
* Basic enemy AI
* Level loading from Tiled `.tmx` maps
* Sound system with multiple channels

---

## 📸 Features

### 🎮 Core Gameplay

* First-person movement (WASD + mouse look)
* Weapon switching (Knife, Pistol, Rifle)
* Ammo & health system
* Key-based level progression
* Enemy AI with attack & chase logic
* Item pickups (ammo, medkits, weapons, keys)

### 🧠 Technical Highlights

* OpenGL 3.3 Core Profile
* Texture arrays for performance
* Instanced rendering for billboards & HUD
* Grid-based collision detection
* BFS Pathfinding for NPC navigation
* Ray casting for hit detection
* Modular engine architecture

---

## 🗂 Project Structure

```
.
├── main.py               # Entry point
├── engine.py             # Core engine logic
├── scene.py              # Scene update & rendering
├── player.py             # Player logic & camera control
├── camera.py             # View/projection camera system
├── level_map.py          # TMX level loader
├── path_finding.py       # BFS pathfinding
├── ray_casting.py        # Voxel ray traversal
├── shader_program.py     # Shader management
├── textures.py           # Texture array loading
├── texture_builder.py    # Builds texture arrays
├── sound.py              # Audio system
├── settings.py           # Game configuration
├── texture_id.py         # Texture enum IDs
└── assets/               # Textures, sounds, shaders
```

---

## 🛠 Requirements

* Python 3.9+
* Pygame
* ModernGL
* PyGLM
* pytmx

Install dependencies:

```bash
pip install pygame moderngl PyGLM pytmx
```

---

## ▶️ Running the Game

```bash
python main.py
```

Make sure the following directories exist:

```
assets/
resources/levels/
shaders/
```

---

## 🎮 Controls

| Action          | Key         |
| --------------- | ----------- |
| Move Forward    | W           |
| Move Backward   | S           |
| Strafe Left     | A           |
| Strafe Right    | D           |
| Interact (Door) | F           |
| Switch Weapon   | 1 / 2 / 3   |
| Shoot           | Left Mouse  |
| Change Weapon   | Mouse Wheel |
| Quit            | ESC         |

Mouse is captured automatically.

---

## 🧱 Levels

Levels are built using **Tiled Map Editor** and exported as `.tmx`.

Each level includes:

* `walls`
* `floors`
* `ceilings`
* `doors`
* `items`
* `npc`
* `player`

Levels are loaded dynamically:

```python
level_{num}.tmx
```

---

## 🧠 Architecture Overview

### 🔹 Engine

The `Engine` class connects:

* Player
* Scene
* Shader system
* Level map
* Pathfinding
* Ray casting
* Sound
* Textures

### 🔹 Rendering

Rendering is split into:

* Static level mesh
* Instanced doors
* Instanced billboards (NPCs, items)
* HUD layer
* Weapon mesh (first-person view)

### 🔹 Ray Casting

Used for:

* Player → NPC hit detection
* NPC → Player line-of-sight checks

Implements voxel stepping algorithm.

### 🔹 Pathfinding

* BFS on a grid
* Avoids walls and active NPC tiles
* Cached results using `lru_cache`

---

## 🔫 Weapons

| Weapon | Ammo Use | Damage | Range  |
| ------ | -------- | ------ | ------ |
| Knife  | 0        | 8      | Short  |
| Pistol | 1        | 20     | Medium |
| Rifle  | 2        | 41     | Long   |

Each weapon has:

* Animation frames
* Miss probability
* Sound effects
* Independent texture IDs

---

## 👾 Enemies

NPCs:

* Brown Soldier
* Blue Soldier
* Rat

Each enemy type has:

* Walk / attack / hurt / death animations
* Unique stats
* Attack distance
* Drop items
* Sound effects

---

## 🔊 Audio

Powered by Pygame mixer:

* Background music loop
* Weapon sounds
* NPC attack & death sounds
* Pickup effects
* Door sounds

Multi-channel playback supported.

---

## 🎨 Textures

* Built automatically into:

  * Texture array
  * Sprite sheet
* Located in:

```
assets/textures/
```

Texture IDs managed via `texture_id.py`.

---

## 📈 HUD

Displays:

* Health
* Ammo
* FPS counter
* Screen effects (damage flash)

Rendered using instanced quads.

---

## 🧪 Performance Notes

* Uses instanced rendering for scalability
* Texture arrays reduce draw calls
* Mipmaps + anisotropic filtering enabled
* Depth testing & blending configured

---

## 🚀 Future Improvements

* More enemy types
* More levels
* Saving system
* Advanced AI states
* Dynamic lighting
* Multiplayer support

---

## 📜 License

This project is for educational purposes and inspired by classic FPS design.

---

## 👤 Author

Built as a learning project combining:

* OpenGL rendering
* Game engine architecture
* AI basics
* Real-time input handling
