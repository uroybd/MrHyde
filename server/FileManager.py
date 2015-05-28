from os import makedirs, listdir
from os.path import isfile, isdir, join
import logging
from sqlite3 import Error as SQLError

from bottle import template

import DbHandler


class FileManager:
    __logger = None
    __db = None

    def __init__(self):
        from main import cm
        self.__logger = logging.getLogger(__name__)
        self.__db = DbHandler.DbHandler(cm.get_db_file())

    def log(self):
        return self.__logger

    def database(self):
        return self.__db

    def create_diff_file(self, id, diff):
        try:
            file_name = ''.join(['/tmp/', id, '_patch.diff'])
            file_out = open(file_name, 'w')
        except IOError:
            self.log().error('Unable to create diff file.')
            raise
        else:
            file_out.write(diff)
            file_out.close()
            return file_name

    def file_download(self, id, file_name):
        repo_id = id.split('/')[0]
        if id.split('/')[1:]:
            file_path = id.split('/')[1:][0]
        else:
            file_path = []

        try:
            repo_path = self.database().list('repo', 'path', "id='%s'" % repo_id)[0]
            abs_path = '/'.join([repo_path, ''.join(file_path), file_name])
            if isfile(abs_path):
                return True
            else:
                return False
        except OSError as exception:
            self.log().error(exception.strerror)
            raise
        except SQLError as exception:
            self.log().error(exception.__str__())
            raise

    def deploy_error_page(self, deploy_path, error_type, error_msg):
        if not isdir(deploy_path):
            makedirs(deploy_path, 0o755, True)
        index_file_path = join(deploy_path, 'index.html')
        index_file = open(index_file_path, 'w')
        index_file.write(template('list_view', rows=[error_msg], header=error_type))
        index_file.close()

    def list_directory(self, path):
        from main import cm
        try:
            repo_path = ''.join([cm.get_base_dir(), '/', path])
            file_list = [f for f in listdir(repo_path)]
            return file_list
        except OSError as exception:
            self.log().error(exception.strerror)
            raise
        except SQLError as exception:
            self.log().error(exception.__str__())
            raise
