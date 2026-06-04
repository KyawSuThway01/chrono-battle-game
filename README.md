# ⚔️ Chrono Battle

> A fast-paced 2D action game built with Python & Pygame — developed as a Diploma student volunteer project.

---

## 🎥 Gameplay Demo

![Gameplay Demo](/background_image/demo.gif)

> 💡 *Replace `demo.gif` with a screen recording of your game exported as GIF*

---

## 📸 Gameplay Screenshots

### ⚔️ Main Battle Screen
![Gameplay](/background_image/gameplay.png)

### 💀 Game Over Screen
![Game Over](/background_image/gameover.png)

> 💡 *Take screenshots with `Snipping Tool` or `Print Screen` while playing*

---

## 👥 Our Team

### Group Photo
![Group Photo](/background_image/group_photo.jpg)

### 🎤 Presentation Day
![Presentation Photo](/background_image/presentation_photo.jpg)

---

## 🎮 About the Game

**Chrono Battle** is an action-packed side-scrolling game where you play as a brave warrior fighting against waves of powerful enemies. Survive, defeat enemies, and level up as the game gets faster and harder.

- 🗡️ Fight against 6 unique enemy types: Goblin, Mushroom, Skeleton, Necromancer, Evil Wizard, and Flying Eye
- 💣 Dodge enemy projectiles and attacks
- ⚡ Speed and difficulty increase as your score climbs
- 🏆 Score system to track your progress across levels

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `SPACE` | Jump |
| `W` | Attack 1 (Sword Slash) |
| `S` | Attack 2 (Power Strike) |
| `TAB` | Restart after Game Over |
| `ESC` | Return to Menu (in Settings/About) |

---

## 🔧 Technical Features

- **Object-Oriented Programming (OOP)** — Hero, Enemy, ScoreLevel as separate classes
- **Sprite Animation System** — Frame-by-frame GIF animation for all characters
- **Collision Detection** — Vector-based distance checking for hit/damage logic
- **Health & Damage System** — Dynamic health bar with damage states
- **Dynamic Difficulty Scaling** — Speed and enemy aggression increase every 100 points
- **Audio Management** — Background music + layered sound effects
- **Menu Navigation System** — Start, Settings, About screens
- **Score & Level Progression** — Auto-incrementing score with level-up milestones
- **Multi-Enemy AI** — 6 different enemies with unique attack patterns and animations

---

## 🌟 Features

- 🎨 Animated sprite-based characters with multiple states (idle, attack, hit, death)
- 🌍 Scrolling background that changes with level progression
- 🔊 Full audio — background music, sound effects for attacks, jumps, and explosions
- ⚙️ In-game settings with adjustable sound and brightness sliders
- 📖 About screen with game description
- 💀 Game Over screen with final score and restart option

---

## 🗂️ Project Structure

```
chrono-battle-game-main/
│
├── Audio/                          # Sound effects and background music
│   ├── Game Background Audio.wav
│   ├── Game Start Menu Audio.wav
│   ├── Game_Over Audio - (2).wav
│   ├── Player_Jumping.wav
│   ├── Player_Sword_Attack.wav
│   ├── Enemy_Sword_Attack.wav
│   ├── Bomb_Explode.wav
│   └── Bomb_ Throw from Enermy.wav
│
├── background_image/               # Background images for levels + menu GIF
│
├── Enemies/                        # Enemy sprite frames (Goblin, Mushroom, etc.)
│
├── hero/                           # Hero sprite frames
│   ├── Run/
│   ├── Jump/
│   ├── Fill/
│   ├── Death/
│   ├── hit/
│   ├── attack1/
│   └── attack2/
│
├── Libre_Baskerville,Monomakh/     # Custom fonts
│
├── Code/
│   ├── main_start.py               # 🚀 Entry point — run this file
│   ├── main.py                     # Core game loop
│   ├── hero.py                     # Hero class (movement, attacks, health)
│   ├── enemies.py                  # Enemy class (AI, animations, projectiles)
│   ├── score.py                    # Score & level system
│   ├── setting.py                  # Settings screen
│   └── For_Image_Cutting.py        # Utility: sprite sheet cutter
│
└── README.md
```

---

## ⚙️ How to Run

### 1. Install Dependencies
```bash
pip install pygame Pillow
```

### 2. Run the Game
```bash
cd Code
python main_start.py
```

> ⚠️ Make sure you run from inside the `Code/` folder, or the assets won't load correctly.

---

## 👥 Contributors

| Name | Role |
|------|------|
| Member 1 *(replace)* | Game Logic & Enemy AI |
| Member 2 *(replace)* | Hero Animations & Controls |
| Member 3 *(replace)* | UI, Menu & Audio |
| Member 4 *(replace)* | Art Assets & Sprite Cutting |

> 🎓 Volunteer Diploma Student Project

---

## 🚀 Future Improvements

- 👹 Boss Battles with unique mechanics
- 💾 Save & Load System
- ⚔️ More Weapons and Power-ups
- 🗺️ More Levels with new backgrounds
- 🧙 Character Selection Screen
- 🌐 Multiplayer Mode

---

## 🎓 Academic Project

**Chrono Battle** was built by Diploma students as a volunteer game development project. It demonstrates practical application of:

- Python Programming & OOP Design
- Game Development Concepts with Pygame
- Sprite Animation & Audio Integration
- UI/UX Design and Event Handling

---

## 👨‍💻 Built With

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)
![Pillow](https://img.shields.io/badge/Pillow-PIL-orange)

---

*Thanks for playing Chrono Battle! ⚔️*
