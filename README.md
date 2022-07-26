# Chapter Converter
Converts from YouTube's chapter format to Matroska's OGM format.

The chapter file can be muxed with popular tools like `MKVToolNix`.

## Usage
Both CLI and GUI will open a file explorer menu where you can select your file(s) to convert.

### CLI
```
python converter.pyw
```

### GUI
```
Double-click converter.pyw
```

-----------------------------------------------------------------------

## Youtube Format
Youtube uses `MM:SS` and `HH:MM:SS`format. When creating chapters, you cannot mix formats.
```
00:00 Chapter 1
00:30 Chapter 2
01:00 Chapter 3
```

## OGM Format
OGM uses `HH:MM:SS:mmm` format. This format has been modified for readability but still works.
```
CHAPTER01        =00:00:00.000
CHAPTER01NAME    =Chapter 1

CHAPTER02        =00:00:30.000
CHAPTER02NAME    =Chapter 2

CHAPTER03        =00:01:00.000
CHAPTER03NAME    =Chapter 3
```
