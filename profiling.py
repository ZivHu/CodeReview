# -*- coding: utf-8 -*-

import cProfile
import pstats

PROFILING = True  # 性能分析器开关


# 性能分析装饰器定义
def do_cprofile(filename):
    """
    Decorator for function profiling.
    """

    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            if PROFILING:
                profile = cProfile.Profile()
                profile.enable()
                print('    性能测试中..........')
                result = func(*args, **kwargs)
                profile.disable()
                print('    性能测试完毕........')
                # Sort stat by internal time.
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
                print('    文件已生成---『{}』'.format(filename))

                p = pstats.Stats(filename)
                print('################################分析情况####################################')
                p.strip_dirs().sort_stats('cumtime').print_stats(10, 1.0, '.*')
            else:
                result = func(*args, **kwargs)
            return result

        return profiled_func

    return wrapper
