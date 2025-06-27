

<div align="center">

## ⚠️ IMPORTANT DISCLAIMER ⚠️
This slot machine project is for **educational purposes only**. **Do not gamble — you will lose!**

</div>
  
## Demo Videos

### Gameplay

https://github.com/user-attachments/assets/07f95cd8-30dd-4851-b06d-33874c0aa03a


### Jackpot

https://github.com/user-attachments/assets/36837d2e-36da-4ebc-9807-b0468f2bbc20



### Winning Lines


https://github.com/user-attachments/assets/fc38df5f-3a1e-4369-bd3d-e6e708cfbefe



> In the included *Winning Lines* video, the symbol set was intentionally reduced to increase the visibility of winning line patterns. This was done to better illustrate the paylines during testing and is **not reflective of standard game odds**. The full symbol set is used during normal gameplay.



## 🙏 Big Thanks

Special thanks to the following creators for their invaluable tutorials and insights:

- [**NotaSWE**](https://www.youtube.com/@NotaSWE) – for insightful explanations on **delta time** and **system design**, which greatly improved the structure and performance of this project.

- [**Clear Code**](https://www.youtube.com/@ClearCode) – for their incredible **Pygame tutorials**, which provided a solid foundation and inspiration throughout the development process.


> The idea for this project originated from a random [**NotaSWE**](https://www.youtube.com/@NotaSWE) video, where the concept of **delta time** was explained — this turned out to be crucial for creating smooth animations. I also adopted his **system design** approach when starting the project.


## 💡 My Contribution  

Building upon that foundation, i implemented several unique features to make the slot machine feel more interactive, flexible, and visually engaging:

- 🎯 **Dynamic gameplay mechanics** — Change bet size and number of lines during gameplay using arrow keys. No need to modify the code to play differently.
- 🧠 **Custom line system** — Lines are implemented programmatically, with logic that checks for winning combinations across any defined set of lines.
- 💰 **Jackpot logic** — A random spin counter triggers a jackpot win to simulate rarity and add excitement.
- 📈 **Dynamic payout adjustment** — Win payouts scale according to the number of active lines, encouraging strategic play.
- 🏷️ **Symbol-based payout table** — Each symbol pays out a different multiplier of the player's bet per winning line.  
  The payout structure is defined by:
  ```python
  SYMBOL_PAYTABLE = {
      "cherry": 1.2,    # 120% of bet per winning line
      "seven": 10,      # 1000% of bet
      "bar": 5.0,       # 500% of bet
      "diamond": 2.5,   # 250% of bet
      "clover": 1.8     # 180% of bet
  }
  ```
  This allows for easy adjustment of game balance and introduces more excitement with rare, high-paying symbols.
- 🔀 **Customizable paylines** — You can define your own lines for the slot machine.  
    There are now **37** total paylines included by default, supporting a wide variety of patterns including straight, diagonal, zig-zag, and V-shapes.  
    Example:
  ```python
  PAYLINES = [
      ...
      [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],  # second_row
      [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],  # first_row
      [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],  # third row
      [(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)],  # V - shape
      [(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)],  # V - shape upside down
      ...
  ]
  ```
  You can add, remove, or modify these lines in the code to create your own unique slot machine experience.
- 🎞️ **Enhanced animations** — Added animations to improve visual feedback and player experience:
  - Animated **coin bursts** when a jackpot is hit
  - **Line highlighting animations** for multiple line wins
  - **Screen shake** and **flashing transparency effects** to emphasize big wins

These additions are designed to make the game not just a technical demo, but a playable and engaging slot machine experience.

## 🕹️ Controls

- **← Left Arrow** – Decrease bet  
- **→ Right Arrow** – Increase bet  
- **↑ Up Arrow** – Increase number of active lines  
- **↓ Down Arrow** – Decrease number of active lines

## 🎨 Image Customization
> 🖼️ You're free to replace or modify the symbol images however you like — just make sure they are in `.png` format **with a transparent background** so visual effects render properly. Pygame will automatically scale them to fit the defined dimensions:
>
> ```python
> SYMBOL_WIDTH = 240
> SYMBOL_HEIGHT = 200
> ```

## ⚙️ Requirements

- Python 3 is required.

Install dependencies (recommended):
```sh
pip install -r requirements.txt
```

Or install Pygame only:
```sh
pip install pygame
```

To run:
```sh
python main.py
```
