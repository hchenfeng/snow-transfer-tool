import importlib.machinery
import importlib.util
import os

loader = importlib.machinery.SourceFileLoader('snowTransfer', 'snowTransfer')
spec = importlib.util.spec_from_loader(loader.name, loader)
mod = importlib.util.module_from_spec(spec)
loader.exec_module(mod)

def test_convert_number_human_readable():
    assert "200.00 B" == mod.human_readable_size(200)

def test_logfile_generation():
    mod.log_dir = '/tmp'
    mod.create_logger()
    assert os.path.isfile(mod.log_dir + '/snowTransfer-full-%s.log' % mod.current_time)
