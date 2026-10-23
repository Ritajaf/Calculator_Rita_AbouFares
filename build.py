from pybuilder.core import use_plugin, init


use_plugin("python.core")
use_plugin("python.unittest")


name = "calculator_Rita_AbouFares"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("name", "calculator_Rita_AbouFares")
    project.set_property("version", "0.1")
    project.set_property("default_task", "publish")
    project.set_property("unittest_module", "tests.unittest")
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Rita_AbouFares")
    project.set_property("unittest_module_glob", "test_*")
