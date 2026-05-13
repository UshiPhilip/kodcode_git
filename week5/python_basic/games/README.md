# Word Guessing Game 🎯

A simple terminal-based word guessing game written in Python.  
The player chooses how many guesses they want, then tries to reveal the hidden word one letter at a time.

---

## 📌 Features

- Choose your own number of guesses.
- Random word selection from a built-in word list.
- Input validation for numbers and letters.
- Hidden word display using `#`.
- Win or lose message at the end.
- Option to quit anytime by typing `quit`.

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the script:

```
python main.py
```
Replace filename.py with the name of your Python file.

🎮 How to Play
Enter how many guesses you want.
A random hidden word will be selected.
Guess one letter at a time.
If the letter exists in the word, it will be revealed.
If not, one guess is removed.
Continue until:
You reveal the full word ✅
You run out of guesses ❌

You can type:
```
quit
```
at any time to exit the game.

## 📝 Example Gameplay

Enter a number guesses that you want to play: 5

---- HERE IS YOUR STATUS FOR NOW ----

You already used this letters [ ].

The hidden word is: #####.

Left you 5 times to try.

Please guess one letter (or quit to exit): a

## 📂 Word List

The game currently uses these words:

* bread
* light
* frame
* storm
* grape
* cloud
* point
* match
* brick
* voice

## ⚠️ Notes

Only English letters are allowed.
Only one letter can be entered each turn.
Invalid input will ask again.

## 🚀 Future Improvements

Possible upgrades:

Show already guessed letters more clearly
Add difficulty levels
Larger word database
Score system
Replay option
Better UI design

## 👨‍💻 Author

Made with Python for learning and practice.
