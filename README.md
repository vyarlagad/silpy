# The Simple Image Library `SilPy`
This is a simple library (as the name implies) that aims to implement several digital image processing algorithms.

## Minimal Intensity Graphic (.MIG)
For educational use, it is helpful to have a simple image file format that can be easily encoded to a file. I have decided to define a simple image file format that will only record intensity information about a particular image. Here is the file format:
```
[BYTE (Width)]
[BYTE (Height)]
[BYTE (Value for Row 1 Column 1)]
[BYTE (Value for Row 1 Column 2)]
...```
Here is an example in decimal:
```
8 8
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0
0 5 10 15 15 10 5 0```
Every byte is added to the file sequentially. There are no explicit new line characters in the file format, only byte values.
