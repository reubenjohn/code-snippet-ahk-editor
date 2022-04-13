# code-snippet-ahk-editor
Converts a code snippet to an Auto Hotkey Script for your favorite editor

# Prerequisites

This project is implemented in python, and assumes you have python 3 installed in order to execute.  
Additionally, since the program generates [AutoHotkey](https://www.autohotkey.com/) scripts, you would thus also need to have this software installed in order for the code snippet functionality to take effect.

# Quick Start

Once you have the prerequisite software installed, the below guide should get you up and running with code snippets at your fingertips.

Execute the below shell script in a terminal that supports running shell scripts:

    ./process_java_samples.sh

This generates AutoHotkey scripts for inserting code snippts for common Java algorithms such as binary search.
See `process_java_samples.sh` for more information.

Next, you can launch the index.ahk script with AutoHotkey to activate the code snippets.  
This will allow you to insert the code snippets configured in the index.ahk file.  

### Activating a code snippet

1. Press `Ctrl+Alt+Shift+I` to activate the prompt
2. Next, enter one of the short hands configured in the index.ahk file, for example `p` followed by `l` (println)
3. Now, you can insert one character at a time by pressing any of the function keys in any order. For example, `F1`, `F4`, etc.
4. Once the snippet reaches completion, the function keys will restore their original functionality in a few seconds.
5. You can abort at any time with `Ctrl+Shift+Esc`

You may customize this functionality by modifying the index.ahk file.
