#
import logging
import types
import sys

logger = logging.getLogger(name='root')


class MyLogger(object):

    def __init__(self, level=logging.INFO):
        """
         Python log levels:
            CRITICAL 50
            ERROR   40
            WARNING 30
            INFO    20
            DEBUG   10
            NOTSET  0
        """
        self.__myLevel = level
        self.__currentLevel = logger.getEffectiveLevel()
        #
        #        logger.info("+MyLogger().__init__ with my level %d and current level %d" % (self.__myLevel, self.__currentLevel))
        # my level >= current level to write message

    def write(self, str):
        try:
            if self.__myLevel >= self.__currentLevel:
                f = sys._current_frames().values()[0]
                # fN = f.f_back.f_globals['__file__']
                tL = f.f_back.f_globals['__name__'].split('.')
                mN = "      " + tL[-1]
                if ((str is not None) and isinstance(str, types.StringTypes) and (str[-1] == '\n')):
                    logger.log(self.__myLevel, mN + " " + str[:-1])
                else:
                    logger.log(self.__myLevel, mN + " " + str)
        except:
            logger.exception(str)

    def flush(self):
        f = sys._current_frames().values()[0]
        # fN = f.f_back.f_globals['__file__']
        mN = f.f_back.f_globals['__name__']
        logger.log(self.__myLevel, mN + " " + "----")
