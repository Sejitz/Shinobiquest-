<div align="center">⚔️ SHINOBI QUEST

A Shinobi's Journey Begins Here.

A terminal-based RPG inspired by the world of ninjas, built with Python and Rich.

Explore. Fight. Survive. Become Stronger.

""Python" (https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)" (https://www.python.org/)
""Interface" (https://img.shields.io/badge/Interface-Rich-8A2BE2?style=for-the-badge)" (https://github.com/Textualize/rich)
""Release" (https://img.shields.io/badge/Release-v1.0.0-2ea44f?style=for-the-badge)" (https://github.com/Sejitz/Shinobiquest-/releases)
""Platform" (https://img.shields.io/badge/Platform-Terminal-lightgrey?style=for-the-badge)" (#-getting-started)

"📦 Releases" (https://github.com/Sejitz/Shinobiquest-/releases) · "🐛 Report a Bug" (https://github.com/Sejitz/Shinobiquest-/issues) · "💻 Source Code" (https://github.com/Sejitz/Shinobiquest-)

</div>---

🥷 About the Game

Shinobi Quest (SQ) is a Python-based terminal RPG where you step into the life of a shinobi.

Choose your village, explore the game world, manage your resources, purchase supplies, and fight enemies in turn-based combat.

The game combines traditional Python programming with a dynamic terminal interface powered by Rich, featuring live layouts, status bars, and an updating battle log.

This project is built to be playable, expandable, and continuously improved.

✨ Features

⚔️ Strategic Combat

- Turn-based battles against randomly encountered enemies.
- Multiple enemy types with different combat behavior.
- Normal attacks, kunai throws, and escape attempts.
- Critical hits that deal increased damage.
- Enemy attacks, healing behavior, and combat responses.
- Live battle log that displays combat events.
- Experience and Ryo rewards after victory.

Choose your moves wisely. Randomly spamming attacks can get your shinobi defeated, especially against stronger enemies.

❤️ Character Status

- Live HP and Chakra indicators.
- Enemy health tracking during combat.
- Ryo balance displayed in the battle interface.
- Experience-based progression.
- Level-ups after reaching the required XP threshold.

🎒 Inventory System

- View your available items.
- Manage consumable supplies.
- Keep track of potions and kunai.
- Use your resources strategically during your journey.

🏪 Shop System

Purchase supplies using Ryo earned during gameplay.

Item| Price
🧪 Potion| 70 Ryo
🗡️ Kunai| 40 Ryo

🏯 Multiple Villages

Choose your starting village and begin your journey.

- 🍃 Leaf Village
- 🌧️ Rain Village
- 🏜️ Sand Village

💾 Save & Load

- Start a new game or load an existing game.
- Preserve your game progress.
- Continue your shinobi journey without starting over.

🎨 Rich Terminal Interface

The interface uses Python's Rich library to provide a more structured and interactive terminal experience.

- Organized layouts and panels.
- Live HP, Chakra, and enemy health bars.
- Dynamic battle information.
- Updating combat logs.
- Dedicated game menus and status displays.

---

🎮 Gameplay

Your journey follows a simple progression:

          ⚔️ SHINOBI QUEST
                 |
          ┌──────┴──────┐
          |             |
       New Game      Load Game
          |             |
          └──────┬──────┘
                 |
          Choose Village
                 |
           Begin Journey
                 |
          ┌──────┴──────┐
          |             |
        Explore       Inventory
          |             |
       Encounter       Shop
          |
      Battle Begins
          |
    ┌─────┼─────┐
    |     |     |
  Attack Kunai Run
    |     |     |
    └─────┼─────┘
          |
    Battle Results
          |
      Earn Rewards
          |
     Grow Stronger

⚡ Combat Mechanics

Action| Effect
Attack| Deals 10 base damage
Critical Hit| Deals 25 damage
Kunai| Deals 20 damage and consumes one kunai
Guard Response| Reduces the player's incoming damage to 5 in the corresponding combat response
Run| Attempts to escape the battle

Critical hits have a 5% chance of occurring during normal attacks.

Enemies can attack and heal, so understanding your opponent matters just as much as choosing your own attacks.

📈 Progression

- Earn XP and Ryo by defeating enemies.
- Level up after accumulating 500 XP.
- Find healing potions through a chance-based reward mechanic.
- Manage your HP and available supplies to survive tougher encounters.

---

🛠️ Built With

Technology| Purpose
Python| Core game logic
Rich| Terminal UI, layouts, panels, and live updates
JSON| Game save data
Git & GitHub| Version control and project distribution

---

📂 Project Structure

The project is organized into separate modules to keep different parts of the game manageable.

Shinobiquest-/
│
├── UI/          # Menus and interface components
├── systems/     # Game systems and mechanics
├── data/        # Game data
├── utils/       # Shared utilities
│
├── main.py      # Game entry point
├── save.json    # Save data, when present
└── README.md    # Project documentation

The tree above highlights the main components; additional files and subdirectories may exist.

---

🚀 Getting Started

Requirements

- Python 3.x
- A terminal that supports Python execution
- The Rich library

1. Clone the Repository

git clone https://github.com/Sejitz/Shinobiquest-.git

2. Enter the Project Directory

cd Shinobiquest-

3. Install Dependencies

pip install rich

4. Launch the Game

python main.py

Follow the in-game menus to start a new adventure or load your existing progress.

---

📱 Platform Compatibility

Shinobi Quest is a terminal-based Python game.

It can run in environments that support the required Python dependencies and terminal features, including suitable desktop terminals and Android terminal environments such as Termux.

Note: Terminal behavior may vary between environments.

---

🗺️ Development

Shinobi Quest is an evolving project focused on building a playable RPG while improving its combat systems, interface, and overall game experience.

Current development includes:

- Turn-based combat and enemy behavior.
- Character progression and resource management.
- Inventory and shop mechanics.
- A live Rich-based terminal interface.
- Save/load functionality.

Future improvements will depend on development priorities and testing.

---

📦 Releases

Check the Releases page for published versions, updates, and downloadable assets.

<div align="center">Current Release

"v1.0.0"

"⬇️ View All Releases" (https://github.com/Sejitz/Shinobiquest-/releases)

</div>---

🤝 Contributing

Found a bug or have an idea to improve the game?

1. Check the existing "Issues" (https://github.com/Sejitz/Shinobiquest-/issues).
2. Open an issue describing the bug or feature.
3. If you'd like to contribute code, fork the repository and submit a pull request.

Suggestions, bug reports, and constructive feedback are welcome.

---

👨‍💻 Developer

Sejitz — Creator and developer of Shinobi Quest.

Built with Python, experimentation, and a passion for creating games.

---

<div align="center">🌑 Every Shinobi Has a Story.

What's yours?

⭐ If you find the project interesting, consider starring the repository.

"GitHub Repository" (https://github.com/Sejitz/Shinobiquest-)

</div>
