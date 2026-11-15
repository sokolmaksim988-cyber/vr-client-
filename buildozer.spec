[app]
# (str) Title of your application
title = VR Client

# (str) Package name
package.name = vrclient

# (str) Package domain (needed for android packaging)
package.domain = org.vr

# (str) Source files where the *.py files are located
source.dir = .

# (list) Source files to include (let it match default)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,sdl2,glew

# (str) Supported orientations
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# Android API and minimum API versions
android.api = 33
android.min_api = 21
