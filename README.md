# SomeBar

Simple taskbar indicator for Unity inspired by [AnyBar](https://github.com/tonsky/AnyBar) (basically it is a clone of AnyBar)

Tested on Ubuntu 18.04 with Unity and Ubuntu GNOME

<img src="screenshot_unity.png?raw=true" />

<img src="screenshot_ubuntugnome.png?raw=true" />

## Install

```sh
pip3 install somebar
```

## Usage

to run somebar just execute in console
```sh
somebar
```

somebar is controlled via UDP port (1738 by default). Send it a message and it will change a color:

```sh
echo -n "black" | nc -4u -w0 localhost 1738
```

Following commands change color:


<img src="somebar_icons/white@2x.png?raw=true" width=19 /> `white`
<img src="somebar_icons/red@2x.png?raw=true" width=19 /> `red`
<img src="somebar_icons/orange@2x.png?raw=true" width=19 /> `orange`
<img src="somebar_icons/yellow@2x.png?raw=true" width=19 /> `yellow`
<img src="somebar_icons/green@2x.png?raw=true" width=19 /> `green`
<img src="somebar_icons/cyan@2x.png?raw=true" width=19 /> `cyan`
<img src="somebar_icons/blue@2x.png?raw=true" width=19 /> `blue`
<img src="somebar_icons/purple@2x.png?raw=true" width=19 /> `purple`
<img src="somebar_icons/black@2x.png?raw=true" width=19 /> `black`
<img src="somebar_icons/question@2x.png?raw=true" width=19 /> `question`
<img src="somebar_icons/exclamation@2x.png?raw=true" width=19 /> `exclamation`

And one special command forces somebar to quit: `quit`

## Running multiple instances

You can run several instances of somebar as long as they listen on different ports. Use `-p` or `--port` command line argument to change port:

```sh
somebar -p 1738
somebar -p 1739
somebar -p 1740
```

## Custom images

somebar can use user-local images if you put them under `~/.somebar` or `~/.AnyBar`. E.g. if you have `~/.AnyBar/square@2x.png` present, send `square` to 1738 and it will be displayed.
