from pybuilder.core import use_plugin, init, task, depends
import os
from glob import glob
from subprocess import call

use_plugin("python.core")

@init
def initialize(project):
    project.build_depends_on("pyside6")  # 或者 "pyside2" 如果你用 PySide
    
    # 设置 UI 文件目录和输出目录
    project.set_property("dir_source_ui", "src/main/ui")  # UI 文件目录
    project.set_property("dir_source_main_python", "src/main/python")  # Python 代码目录
    
    # 设置 pyuic5 或 pyside2-uic 命令
    project.set_property("pyqt_ui_compiler", "pyside6-uic")  # 或者 "pyside2-uic"

@task
def compile_ui_files(project, logger):
    """将 .ui 文件编译为 .py 文件"""
    ui_dir = project.get_property("dir_source_ui")
    output_dir = os.path.join(project.get_property("dir_source_main_python"), "shit_recorder/ui")
    compiler = project.get_property("pyqt_ui_compiler")
    
    if not os.path.exists(ui_dir):
        logger.warn("UI 目录不存在: %s", ui_dir)
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ui_files = glob(os.path.join(ui_dir, "*.ui"))
    
    if not ui_files:
        logger.info("没有找到 .ui 文件")
        return
    
    for ui_file in ui_files:
        base_name = os.path.splitext(os.path.basename(ui_file))[0]
        output_file = os.path.join(output_dir, f"ui_{base_name}.py")
        
        logger.info("编译 %s -> %s", ui_file, output_file)
        
        with open(output_file, "w") as out:
            exit_code = call([compiler, ui_file], stdout=out)
            
            if exit_code != 0:
                logger.error("编译 %s 失败", ui_file)
                raise RuntimeError(f"无法编译 UI 文件: {ui_file}")

@task
@depends("compile_ui_files")
def build(project):
    pass  # 正常的构建过程