# The different of theme and color-scheme in Sublime Text
# Sublime Text 的 theme和color-scheme

区别Sublime Text的theme和color-scheme,
theme是指主题，包括一些编辑器的元素，
而color-scheme是指语法高亮的颜色配置。

## PackageResourceViewer

Unless explicitly designated to not use it, most packages for Sublime Text 3 use the .sublime-package format (essentially a zip file). These packages are stored one directory up from the Packages folder, in Installed Packages. If you want to work with them, I highly recommend getting the PackageResourceViewer plugin by @skuroda. Install it via Package Control.

Once installed, open the command palette with Control + Shift + P and type prv to get the PackageResourceViewer options. Choose Extract Package, navigate down to Theme - Soda, hit Enter, and you're all set - the directory Packages/Theme - Soda should now exist with all the files from the Github repo in it. The .sublime-theme files will probably be the ones you're most interested in for now.

Have fun!

@WilsonF - Most theme's documentation includes instructions on how to activate it. For Soda, there are two sets of options - Dark and Light, and Sublime 2 and 3. So, for dark on ST3, the theme name is Soda Dark 3.sublime-theme. The same for ST2 would be Soda Dark.sublime-theme. In your user preferences, set "theme": "themename.sublime-theme" - for example, "theme": "Soda Dark 3.sublime-theme". Save your user prefs, restart Sublime, and the new theme will be activated. –  MattDMo Sep 15 '14 at 17:40



## 启用主题theme
在Preferences.sublime-settings 里边添加
"theme": "Nil.sublime-theme",
"theme": "Soda Light 3.sublime-theme",
"theme": "Glacier.sublime-theme",
"theme": "Predawn.sublime-theme",