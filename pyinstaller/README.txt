
○ インストール
  # pip install pyinstaller

○ Pythonファイルをexe化
  # pyinstaller <pyファイル> --noconsole --onefile

○ 参考
  - Pythonではじめるアプリ開発 ：exe化編
    http://pc-chem-basics.blog.jp/archives/24112647.html

  - Macでpyinstallerを使ってPythonコードから実行ファイルを生成した時の記録
    https://qiita.com/kanedaq/items/8bb33c135fd89991d548


○ 以下ログ ------------------------------
  ■ pip installログ
    yamanakukinoMBP:tkinter yamanakayasuyuki$ 
    yamanakukinoMBP:tkinter yamanakayasuyuki$ pip install pyinstaller
    Collecting pyinstaller
      Downloading pyinstaller-4.1.tar.gz (3.5 MB)
         |████████████████████████████████| 3.5 MB 124 kB/s 
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
        Preparing wheel metadata ... done
    Collecting pyinstaller-hooks-contrib>=2020.6
      Downloading pyinstaller_hooks_contrib-2020.11-py2.py3-none-any.whl (172 kB)
         |████████████████████████████████| 172 kB 148 kB/s 
    Collecting macholib>=1.8; sys_platform == "darwin"
      Downloading macholib-1.14-py2.py3-none-any.whl (37 kB)
    Requirement already satisfied: setuptools in /usr/local/lib/python3.8/site-packages (from pyinstaller) (50.3.2)
    Collecting altgraph
      Downloading altgraph-0.17-py2.py3-none-any.whl (21 kB)
    Building wheels for collected packages: pyinstaller
      Building wheel for pyinstaller (PEP 517) ... done
      Created wheel for pyinstaller: filename=pyinstaller-4.1-py3-none-any.whl size=2790249 sha256=f6ef8a5f04403a57e8d2335d81d7ffc90b464cc1b3c4cf2e4cedf35fd6422f07
      Stored in directory: /Users/yamanakayasuyuki/Library/Caches/pip/wheels/ae/7a/1e/e42202ec16f036e6c25592c6bc63d3c26e6a6addd6a25f053a
    Successfully built pyinstaller
    Installing collected packages: pyinstaller-hooks-contrib, altgraph, macholib, pyinstaller
    Successfully installed altgraph-0.17 macholib-1.14 pyinstaller-4.1 pyinstaller-hooks-contrib-2020.11
    WARNING: You are using pip version 20.2.4; however, version 20.3.3 is available.
    You should consider upgrading via the '/usr/local/opt/python@3.8/bin/python3.8 -m pip install --upgrade pip' command.
  
  
  ■ 実行
    yamanakukinoMBP:pyinstaller yamanakayasuyuki$ ll
    total 32
    -rwxrwxrwx  1 yamanakayasuyuki  staff  11036  1  4 01:06 tkinterTest.py
    yamanakukinoMBP:pyinstaller yamanakayasuyuki$ pyinstaller tkinterTest.py --noconsole --onefile
    108 INFO: PyInstaller: 4.1
    109 INFO: Python: 3.8.6
    160 INFO: Platform: macOS-10.15.7-x86_64-i386-64bit
    161 INFO: wrote /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/tkinterTest.spec
    167 INFO: UPX is not available.
    170 INFO: Extending PYTHONPATH with paths
    ['/Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller',
     '/Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller']
    185 INFO: checking Analysis
    186 INFO: Building Analysis because Analysis-00.toc is non existent
    186 INFO: Initializing module dependency graph...
    189 INFO: Caching module graph hooks...
    204 INFO: Analyzing base_library.zip ...
    4773 INFO: Processing pre-find module path hook distutils from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks/pre_find_module_path/hook-distutils.py'.
    4774 INFO: distutils: retargeting to non-venv dir '/usr/local/Cellar/python@3.8/3.8.6/Frameworks/Python.framework/Versions/3.8/lib/python3.8'
    9221 INFO: Caching module dependency graph...
    9432 INFO: running Analysis Analysis-00.toc
    9442 INFO: Analyzing /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/tkinterTest.py
    9515 INFO: Processing module hooks...
    9516 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9517 INFO: Loading module hook 'hook-lib2to3.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9581 INFO: Loading module hook 'hook-_tkinter.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9588 INFO: Not collecting Tcl/Tk data - either python is using macOS' system Tcl/Tk framework, or Tcl/Tk data directories could not be found.
    9588 INFO: Loading module hook 'hook-encodings.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9687 INFO: Loading module hook 'hook-distutils.util.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9690 INFO: Excluding import of lib2to3.refactor from module distutils.util
    9691 INFO: Loading module hook 'hook-pickle.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9694 INFO: Excluding import of argparse from module pickle
    9694 INFO: Loading module hook 'hook-heapq.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9696 INFO: Excluding import of doctest from module heapq
    9696 INFO: Loading module hook 'hook-difflib.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9698 INFO: Excluding import of doctest from module difflib
    9698 INFO: Loading module hook 'hook-multiprocessing.util.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9699 INFO: Excluding import of test from module multiprocessing.util
    9699 INFO: Excluding import of test.support from module multiprocessing.util
    9700 INFO: Loading module hook 'hook-sysconfig.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9739 INFO: Loading module hook 'hook-xml.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9836 INFO: Loading module hook 'hook-distutils.py' from '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks'...
    9871 INFO: Looking for ctypes DLLs
    9936 INFO: Analyzing run-time hooks ...
    9943 INFO: Including run-time hook '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks/rthooks/pyi_rth_multiprocessing.py'
    9947 INFO: Including run-time hook '/usr/local/lib/python3.8/site-packages/PyInstaller/hooks/rthooks/pyi_rth__tkinter.py'
    9961 INFO: Looking for dynamic libraries
    10124 INFO: Looking for eggs
    10125 INFO: Using Python library /usr/local/Cellar/python@3.8/3.8.6/Frameworks/Python.framework/Versions/3.8/Python
    10129 INFO: Warnings written to /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/build/tkinterTest/warn-tkinterTest.txt
    10191 INFO: Graph cross-reference written to /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/build/tkinterTest/xref-tkinterTest.html
    10220 INFO: checking PYZ
    10220 INFO: Building PYZ because PYZ-00.toc is non existent
    10221 INFO: Building PYZ (ZlibArchive) /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/build/tkinterTest/PYZ-00.pyz
    10917 INFO: Building PYZ (ZlibArchive) /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/build/tkinterTest/PYZ-00.pyz completed successfully.
    10935 INFO: checking PKG
    10935 INFO: Building PKG because PKG-00.toc is non existent
    10935 INFO: Building PKG (CArchive) PKG-00.pkg
    13835 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
    13840 INFO: Bootloader /usr/local/lib/python3.8/site-packages/PyInstaller/bootloader/Darwin-64bit/runw
    13840 INFO: checking EXE
    13840 INFO: Building EXE because EXE-00.toc is non existent
    13840 INFO: Building EXE from EXE-00.toc
    13840 INFO: Appending archive to EXE /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/dist/tkinterTest
    13860 INFO: Fixing EXE for code signing /Users/yamanakayasuyuki/local-work/Mac_tool/python/pyinstaller/dist/tkinterTest
    13865 INFO: Building EXE from EXE-00.toc completed successfully.
    13871 INFO: checking BUNDLE
    13871 INFO: Building BUNDLE because BUNDLE-00.toc is non existent
    13871 INFO: Building BUNDLE BUNDLE-00.toc
    13888 INFO: moving BUNDLE data files to Resource directory
    yamanakukinoMBP:pyinstaller yamanakayasuyuki$ ll
    total 40
    drwxr-xr-x  3 yamanakayasuyuki  staff     96  1  4 01:30 __pycache__
    drwxr-xr-x  3 yamanakayasuyuki  staff     96  1  4 01:30 build
    drwxr-xr-x  4 yamanakayasuyuki  staff    128  1  4 01:30 dist
    -rwxrwxrwx  1 yamanakayasuyuki  staff  11036  1  4 01:06 tkinterTest.py
    -rw-r--r--  1 yamanakayasuyuki  staff   1016  1  4 01:30 tkinterTest.spec
    ------------------------------------------------------------



