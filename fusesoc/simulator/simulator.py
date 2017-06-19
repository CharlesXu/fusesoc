import argparse
import os
import logging

from fusesoc.edatool import EdaTool
from fusesoc.utils import run_scripts

logger = logging.getLogger(__name__)

class FileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, [os.path.abspath(values[0])])

class Simulator(EdaTool):

    TOOL_TYPE = 'sim'

    def configure(self, args, skip_params = False):
        if not skip_params:
            self.parse_args(args, 'sim', ['plusarg', 'vlogdefine', 'vlogparam', 'cmdlinearg'])
        super(Simulator, self).configure(args)

    def run(self, args):
        self.parse_args(args, 'sim', ['plusarg', 'vlogdefine', 'vlogparam', 'cmdlinearg'])
        if 'pre_run_scripts' in self.fusesoc_options:
            run_scripts(self.fusesoc_options['pre_run_scripts'],
                        self.work_root,
                        self.env)

    def done(self, args):
        if 'post_run_scripts' in self.fusesoc_options:
            run_scripts(self.fusesoc_options['post_run_scripts'],
                        self.work_root,
                        self.env)
