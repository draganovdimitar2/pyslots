

<div align="center">

## ⚠️ IMPORTANT DISCLAIMER ⚠️
This slot machine project is for **educational purposes only**. **Do not gamble — you will lose!**

</div>
  
## Demo Videos

### Gameplay

https://github.com/user-attachments/assets/bd7803c9-1152-4691-966a-afd2b45d3dce

### Jackpot

https://github.com/user-attachments/assets/9e561223-c989-4e3a-8419-3296e3022122

### Winning Lines

https://github.com/user-attachments/assets/1141b4b1-79da-45d2-99a4-60cae59f0306

> In the included *Winning Lines* video, the symbol set was intentionally reduced to increase the visibility of winning line patterns. This was done to better illustrate the paylines during testing and is **not reflective of standard game odds**. The full symbol set is used during normal gameplay.



## 🙏 Big Thanks

Special thanks to the following creators for their invaluable tutorials and insights:

- [**NotaSWE**](https://www.youtube.com/@NotaSWE) – for insightful explanations on **delta time** and **system design**, which greatly improved the structure and performance of this project.

- [**Clear Code**](https://www.youtube.com/@ClearCode) – for their incredible **Pygame tutorials**, which provided a solid foundation and inspiration throughout the development process.


> The idea for this project originated from a random [**NotaSWE**](https://www.youtube.com/@NotaSWE) video, where the concept of **delta time** was explained — this turned out to be crucial for creating smooth animations. I also adopted his **system design** approach when starting the project.


## 💡 My Contribution

> Building upon that foundation, the **winning lines** and **jackpot logic** are original ideas I developed for this project. The line definitions are fully modular, so you can easily add or remove lines to customize the gameplay.  

I implemented several unique features to make the slot machine feel more interactive, flexible, and visually engaging:

- 🎯 **Dynamic gameplay mechanics** — Change bet size and number of lines during gameplay using arrow keys. No need to modify the code to play differently.
- 🧠 **Custom line system** — Lines are implemented programmatically, with logic that checks for winning combinations across any defined set of lines.
- 💰 **Jackpot logic** — A random spin counter triggers a jackpot win to simulate rarity and add excitement.
- 📈 **Dynamic payout adjustment** — Win payouts scale according to the number of active lines, encouraging strategic play.
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
- Install Pygame via pip:

  ```bash
  pip install pygame
  ```
- To run:
  
  ```bash
  python main.py
  ```
