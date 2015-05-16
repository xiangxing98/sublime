# Ubuntu下Sublime Text 3 和搜狗拼音输入法安装全套解决方案

> 首先声明采用方法并非原创，参考了网上的帖子，经过自己的实践做了一些优化，参考帖子如下：

http://www.cnblogs.com/A-Song/archive/2013/04/01/2993194.html
http://songfantasy.iteye.com/blog/1536184
http://my.oschina.net/wugaoxing/blog/121281
http://my.oschina.net/Khiyuan/blog/98713
http://forum.suse.org.cn/viewtopic.php?f=16&t=333
http://www.sublimetext.com/forum/viewtopic.php?f=3&t=7006&start=10#p41343
## 1. 安装sougou for linux:

### （1）卸载原有的输入法，fcitx或ibus。如卸载fcitx
```
sudo apt-get remove fcitx*（如不需保留配置文件用purge）
sudo apt-get autoremove（自动卸载依赖软件）
sudo dpkg –get-selections | grep fcitx（查询fcitx相关的软件包是否卸载）
```

### （2）通过软件源安装（最好用的）
```
sudo add-apt-repository ppa:fcitx-team/nightly
sudo apt-get update
sudo apt-get install fcitx-sogoupinyin
```
然后下载皮肤安装：fcitx-sougou-skin 。在fcitx配置 -> 外观中选择sougou就行了。
fcitx-sougou-skin下载地址：
http://pan.baidu.com/share/link?shareid=3625366887&uk=2046922333

### （3）安装完毕，重新登录系统，即可使用搜狗输入法了。

## 2. 安装配置Sublime Text 3

### (1) 添加Sublime Text 3的安装源并执行更新（可忽略非该源产生的更新错误）。
```
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
```
### (2) 安装Sublime Text 3
```
sudo apt-get install sublime-text
```

### (3) 需要其他配置了，如设置为默认编辑器等等，请参考：
http://songfantasy.iteye.com/blog/1536184

### (4) 下面进入Sublime Text 3 下输入中文的配置。
保存以下代码到文件sublime_imfix.c
```
#include <gtk/gtkimcontext.h>
void gtk_im_context_set_client_window (GtkIMContext *context,
          GdkWindow    *window)
{
  GtkIMContextClass *klass;
  g_return_if_fail (GTK_IS_IM_CONTEXT (context));
  klass = GTK_IM_CONTEXT_GET_CLASS (context);
  if (klass->set_client_window)
    klass->set_client_window (context, window);
  g_object_set_data(G_OBJECT(context),"window",window);

  if(!GDK_IS_WINDOW (window))
    return;
  int width = gdk_window_get_width(window);
  int height = gdk_window_get_height(window);
  if(width != 0 && height !=0)
    gtk_im_context_focus_in(context);
}
```
### (5) 安装C/C++的编译环境和gtk libgtk2.0-dev
```
sudo apt-get install build-essential
sudo apt-get install libgtk2.0-dev
```
### (6) 编译成共享库
```
gcc -shared -o libsublime-imfix.so sublime_imfix.c  `pkg-config --libs --cflags gtk+-2.0` -fPIC
```
### (7) 测试运行
```
LD_PRELOAD=./libsublime-imfix.so sublime_text
```
注意：sublime_text 为sublime-text安装后的可执行命令，不同版本的名称可能不一样
如果测试可以运行，则进行第四步配置;如果不行，再试试
http://my.oschina.net/wugaoxing/blog/121281 这个帖子里的sublime_imfix.c文件

### (8) 拷贝文件到/opt/sublime_text目录下
```
sudo cp libsublime-imfix.so /opt/sublime_text/libsublime-imfix.so
```
注意：/opt/sublime_text/不同版本可能有所不同，请调整为自己安装版本的路径

### (9) 打开终端修改/usr/bin/subl
sudo vim /usr/bin/subl
修改/usr/bin/subl文件，在第一行加入：
export LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so
注意：/opt/sublime_text/不同版本可能有所不同，请调整为自己安装版本的路径

### (10) 修改sublime-text-2.desktop

注意：sublime_text.desktop不同版本有所不同，请调整为自己安装版本的路径 
```
sudo vim /usr/share/applications/sublime_text.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Sublime Text
GenericName=Text Editor
Comment=Sophisticated text editor for code, markup and prose
Exec=/usr/bin/subl %F        #这里修改执行路径为/usr/bin/subl,subl文件刚才已经修改过，大家应该记得
Terminal=false
MimeType=text/plain;        
Icon=sublime-text
Categories=TextEditor;Development;
StartupNotify=true
Actions=Window;Document;

[Desktop Action Window]
Name=New Window
Exec=/usr/bin/subl -n       #这里修改执行路径为/usr/bin/subl,subl文件刚才已经修改过，大家应该记得
OnlyShowIn=Unity;

[Desktop Action Document]
Name=New File
Exec=/usr/bin/subl new_file    #这里修改执行路径为/usr/bin/subl,
```
subl文件刚才已经修改过，大家应该记得
OnlyShowIn=Unity;

修改以上三处代码，保存。以上步骤主要完成了Sublime Text 3在三种情况下打开中文完全正常运行，搜狗输入法比小企鹅输入法好用的多。

### (11) 测试和方法的不足

Sublime Text 3 有5种打开方式，以下是我给的方法的支持程度：

1. 点击桌面图标或者锁定到任务栏的图标来打开Sublime Text 3        支持中文搜狗拼音

2. 在Sublime Text 3 中新建文件（快捷键Ctrl + N）中                 支持中文搜狗拼音

3. 选中文本文件用右键打开文件                                            支持中文搜狗拼音

4. 命令行执行subl                                                            支持中文搜狗拼音

5. 命令行执行sublime_text                                               不支持中文

相信以上五种方式的测试已经让你深深的爱上了我给的方法。在使用过程中其实还是有一些bug的，但一般都不是致命的bug如：

1. 执行sublime_text不能输入中文，这个相信大家用的并不多，真正用到命令行打开文件时可以用subl代替

2. sublime text 3 输入中文时输入框不跟随文字，这个暂时无解啊，不影响核心使用。

相信也会有其他的bug，已经使用上的如果有好的解决方案可以发出来大家共同探讨。

以上方法同样适用于sublime text 2 版本，不同的是在用路径的时候要修改为自己的路径。