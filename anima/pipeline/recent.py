# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
import pickle
import os


class RecentFileManager(object):
    """Manages recent files list per environment

    A storage manager for recent file list per environment.

    To add a new file to the recent files list, the
    :meth:`.add(env_name, file)` can be used.

    And the recent files list can be retrieved through
    :meth:`.recent_files(env_name)` method.

    An environment is not always required, which will save the data under the
    "Generic" name.

    The data is held as a dictionary and the resultant RecentFileManager
    instance is stored in %HOME/.cache/anima/ folder.

    The RecentFileManager instance is restored from the cache folder when a new
    one is created. So it is kind of a Singleton.

    Also the 
    """

    def __new__(cls):
        """restore from locally saved one
        """
        return super(RecentFileManager, cls).__new__(cls)

    @classmethod
    def cache_file_full_path(cls):
        """:return str: the cache file full path
        """
        from anima import pipeline

        return os.path.normpath(
            os.path.expandvars(
                os.path.expanduser(
                    os.path.join(
                        pipeline.local_cache_folder,
                        pipeline.recent_file_name
                    )
                )
            )
        )

    def __init__(self):
        self.recent_files = dict()
        self.restore()

    def save(self):
        """save itself to local cache
        """
        dumped_data = pickle.dumps(self)
        self._write_data(dumped_data)

    def _write_data(self, data):
        """Writes the given data to the cache file

        :param data: the data to be written (generally serialized
          RecentFilesManager class itself).
        """
        file_full_path = self.cache_file_full_path()

        # create the path first
        file_path = os.path.dirname(file_full_path)
        try:
            os.makedirs(file_path)
        except OSError:
            # dir exists
            pass
        finally:
            with open(file_full_path, 'wb') as data_file:
                data_file.writelines(data)

    def restore(self):
        """restore from local cache folder
        """
        try:
            with open(RecentFileManager.cache_file_full_path(), 'rb') as s:
                unpickled_object = pickle.load(s)
                self.__dict__ = unpickled_object.__dict__
        except IOError:
            pass

    def add(self, env_name, file_path):
        """Saves the given file_path under the given environment name

        :param env_name: The name of the environment
        :param file_path: The file_path
        :return: None
        """
        if not self.recent_files.has_key(env_name):
            self.recent_files[env_name] = []

        if file_path in self.recent_files[env_name]:
            self.recent_files[env_name].remove(file_path)

        self.recent_files[env_name].insert(0, file_path)
        self.save()

    def remove(self, env_name, file_path):
        """Removes the given path from the recent files list
        """
        self[env_name].remove(file_path)

    def __getitem__(self, item):
        """
        :param str item: The name of the environment
        :return:
        """
        return self.recent_files[item]

    def __setitem__(self, key, value):
        """

        :param str key: The name of the environment
        :param list value: the value
        :return:
        """
        self.recent_files[key] = value

