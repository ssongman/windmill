import os.path
import logging.handlers
dllname = os.path.join("C:", "Python34", "Lib", "site-packages", "win32", "win32service.pyd")
handler = logging.handlers.NTEventLogHandler('Flask Instance', dllname=dllname, logtype='Application')