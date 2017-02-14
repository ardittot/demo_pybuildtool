""" Run django tests.

Requirements:

    * django
      to install, run `pip install django`

"""

from pybuildtool.core.task import Task as BaseTask
from pybuildtool.misc.path import expand_resource

tool_name = __name__ # pylint:disable=invalid-name

class Task(BaseTask):
    """ Run django test.
    """

    name = tool_name
    workdir = None

    def prepare(self):
        """ Prepare settings.
        """
        cfg = self.conf

        # Change current directory, before running tests.
        work_dir = cfg.get('work_dir')
        if work_dir:
            self.workdir = expand_resource(self.group, work_dir)
            if self.workdir is None:
                self.bld.fatal(cfg['work_dir'] + ' not found.')


    def perform(self):
        """ Start process.
        """
        executable = self.env['PYTHON_BIN']
        return self.exec_command(
            '{exe} manage.py test'.format(
                exe=executable,
            ), cwd=self.workdir)


def configure(conf):
    """ Get python's path.
    """
    conf.env['PYTHON_BIN'] = conf.find_program('python')[0]
