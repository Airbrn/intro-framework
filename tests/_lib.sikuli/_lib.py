from sikuli import *
from _uimap import *
from shortcuts import *

import os

class Browser(object):
    @classmethod
    def Start(self, url):
        Shortcuts.InvokeRunMenu()
        type("chrome " + url)
        type(Key.ENTER)
        wait(Browser_UI.button_Refresh, 5)

    @classmethod
    def Maximize(self):
        Shortcuts.InvokeContextMenu()
        type('x')

    @classmethod
    def OpenNewTab(self):
        type('t', Key.CTRL)

    @classmethod
    def OpenURL(self, url):
        Shortcuts.FocusAddressbar()
        paste(url)
        type(Key.ENTER)

class UIActions(object):
    @classmethod
    def GetClipboard():
        return Env.getClipboard()

    @classmethod
    def CopyAllClipboard(self):
        Shortcuts.SelectAll()
        sleep(1)
        Shortcuts.Copy()
        return Env.getClipboard()

    @classmethod
    def ClearClipboard():
        from java.awt.datatransfer import StringSelection
        from java.awt import Toolkit
        toolkit = Toolkit.getDefaultToolkit()
        clipboard = toolkit.getSystemClipboard()
        clipboard.setContents(StringSelection(""), None)

    @classmethod
    def MaximizeWindow(self):
        Shortcuts.InvokeContextMenu()
        sleep(0.5)
        type('x')

    @classmethod
    def PageDown(self):
        type(Key.PAGE_DOWN)
        sleep(1)

    @classmethod
    def ClickPage(self):
        click()

class Network(object):
    @classmethod
    def DownloadFile(self, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            urllib.urlretrieve(download_url, destination)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))