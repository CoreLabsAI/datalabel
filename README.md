# datalabel - Data Editing Made Easy

[![Build Status](https://travis-ci.org/<user>/<repo>.svg?branch=master)](https://travis-ci.org/<user>/<repo>)

datalabel is a UI-based data editing tool that makes it easy to create labeled text data in a dataframe. With datalabel, you can quickly and effortlessly edit your data without having to write any code. Its intuitive interface makes it ideal for both experienced data professionals and those new to data editing.

## Installation

datalabel can be installed via pip:

```
pip install datalabel
```


### Usage
Once datalabel is installed, you can start using it right away. Simply import datalabel in your script and use the edit function to open the UI-based editor.

```
import datalabel

texts = <your list of strings>
datalabel.label(texts)
```

The editor will open in a new window, allowing you to easily edit your data. You can add tags, write strings, and toggle true and false on rows, and datalabel will handle the rest. When you're finished, simply click submit in the top right corner, close the window, and your labels will be saved to a dataframe.


## Features

- Easy-to-use UI-based data editing
- Intuitive interface
- No coding required


## Contributions

Contributions are welcome! If you'd like to contribute to Labeler, please fork the repository and submit a pull request.

## License

Labeler is released under the [MIT License](https://opensource.org/licenses/MIT).
