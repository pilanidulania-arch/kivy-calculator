[app]

# App basic info
title = CalculatorApp
package.name = calculator
package.domain = org.test

# Source files
source.dir = .
source.include_exts = py,kv,png,jpg,atlas

# Version
version = 1.0

# Requirements (IMPORTANT)
requirements = python3,kivy

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android API
android.api = 33
android.minapi = 21

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Log level
log_level = 2

# Allow backup
android.allow_backup = True

# Presplash (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# Icon (optional)
# icon.filename = %(source.dir)s/data/icon.png

# Build mode
buildozer.dir = .buildozer

# Debug mode
android.debug = True


[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 1