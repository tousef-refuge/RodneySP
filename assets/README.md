Just like config.py, the assets/ directory can also be customized to your liking. However, there's
some strict rules you need to follow for the program to still run. For one, the assets/ directory
MUST look like this:

```commandline
assets
├───audio
│   └───idle
│   │   └───<As many .ogg files as you want as long as there is at least 1>
│   └───end.ogg
│   └───start.ogg
└───sprites
│   └───body.png
│   └───head_blink.png
│   └───head_idle.png
│   └───head_talk.png
│   └───neck.png
└───icon.ico
```

The files just need to exist and not corrupted, and the program should run just fine. Doesn't
matter what's in them. However, the one exception to this is `icon.ico` which also needs to be
16x16 so that PyQt doesn't freak out. Honestly, I recommend just keeping this file as it is,
it's kind of a headache making .ico files