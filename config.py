"""
This is where the variables of the program are created. I put this outside of src/ so that anyone
can easily edit them without having to git clone from scratch. You can adjust these variables to
your liking and the program will still run as long as they keep the exact name they started with
and you don't add anything illegal like negative numbers or something

There's three categories of variables here, with each category being stricter and stricter in
terms of how much it affects the program when edited. Obviously you can still just edit whatever
but I'd advice being a bit more careful the deeper you go into this file
"""

# These variables are chill, you can edit them to tweak your personal Rodney to your preference.
# If you want Rodney to just shut up the whole time, you can set AUDIO_VOLUME to 0 or less and
# he will just stand there menacingly. He won't even say his lines on mute lip-sync style lmao

AUDIO_VOLUME = 1
IDLE_BASE_TIME = 15000
IDLE_VARIANCE = 0.25
MIN_START_TIME = 5000

RANDOM_BLINK_CHANCE = 333
BLINK_TIME = 0.16

# These variables can be adjusted too, but I'd be slightly more careful with them as the widget
# might start having visual bugs and stuff. If you're not satisfied with how Rodney's animations
# look, you can adjust them here, and maybe some other variables in the next category too

WIDGET_SIZE = 400
WIDGET_PADDING = 3

CURSOR_CHECK_TIMER = 16
WIDGET_DOWN = 280
WIDGET_EASING = 0.2

NECK_OX = 0.8
NECK_OY = 0.8
NECK_BOB = 2

HEAD_OX = 0.35
HEAD_OY = 0.7
HEAD_ANGLE_OFFSET = 1
HEAD_TILT_ANGLE = 20
HEAD_TILT_SPEED = 20

# These variables are a lot more volatile than everything else here and I don't recommend editing
# these unless you know what you're doing or you want to add custom sprites and need to adjust
# these numbers accordingly

FPS = 60

BODY_X = 144
BODY_Y = 272
BODY_WIDTH = 256
BODY_HEIGHT = 128

NECK_X = 230
NECK_Y = 260
NECK_WIDTH = 192
NECK_HEIGHT = 160

HEAD_X = 80
HEAD_Y = 30
HEAD_WIDTH = 320
HEAD_HEIGHT = 352
