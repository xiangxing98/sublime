# Sublime Text 3 Markdown

## 1.首先需要安装Package Control：

- Go to [packagecontrol site](https://packagecontrol.io/)
> The simplest
 method of installation is through the Sublime Text console. The console is accessed via the ctrl+` shortcut or the View > Show Console menu. Once open, paste the appropriate Python code for your version of Sublime Text into the console.

- Copy and Paste: ctrl+` 到console，粘贴下面的语句，回车

```python
import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

```python
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```

## 2.安装Markdown Preview：

- ctrl + shift + p
- 输入：package，选择 install package
- 输入：markdown ，选择 markdown preview

## 3.重启sublime

## 4.编辑

- 按Ctrl + N 新建一个文档
- 按Ctrl + Shift + P
- 使用Markdown语法编辑文档
- 语法高亮，输入ssm 后回车(Set Syntax: Markdown)

## 5.在浏览器预览Markdown文档

- 按Ctrl + Shift + P
- 输入mp 后回车(Markdown Preview: current file in browser)
- 此时就可以在浏览器里看到刚才编辑的文档了

## 参考：

- [sublime_packages package_control installation: ](https://sublime.wbond.net/installation) 
- [使用Sublime Text 2 编辑Markdown](http://www.ituring.com.cn/article/6815)
- [markdown: ](http://www.ryanthaut.com/guides/sublime-text-3-markdown-and-live-reload/)

