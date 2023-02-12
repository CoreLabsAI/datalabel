# DataLabel - Data Editing Made Easy

[![Build Status](https://travis-ci.org/TitanLabsAI/datalabel.svg?branch=main)](https://travis-ci.org/<user>/<repo>)

DataLabel is a UI-based data editing tool that makes it easy to create labeled text data in a dataframe. With DataLabel, you can quickly and effortlessly edit your data without having to write any code. Its intuitive interface makes it ideal for both experienced data professionals and those new to data editing.

![](https://s3.gifyu.com/images/ezgif.com-resize5bbffcbc6fa9ab02.gif)
## Installation

DataLabel can be installed via pip:

```
pip install datalabel
```


### Usage
DataLabel is best used inside of a jupyter notebook or other Ipython envs.
Once DataLabel is installed, you can start using it right away. Simply import DataLabel in your script and use the edit function to open the UI-based editor.

```
import pandas as pd
import datalabel


texts = ['hi', 'hello', 'this is test data to label']
df_labeled = datalabel.label(texts)
```

The editor will open in a new window, allowing you to easily edit your data. You can add tags, write strings, and toggle true and false on rows, and DataLabel will handle the rest. When you're finished, simply click submit in the top right corner, close the window, and your labels will be saved to a dataframe.


## Features

- Easy-to-use UI-based data editing
- Intuitive interface
- No coding required


## Contributions

Contributions are welcome! If you'd like to contribute to DataLabel, please fork the repository and submit a pull request.

## License

DataLabel is released under the [MIT License](https://opensource.org/licenses/MIT).
