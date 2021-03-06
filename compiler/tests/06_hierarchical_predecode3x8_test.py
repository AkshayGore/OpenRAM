#!/usr/bin/env python3
"""
Run a regression test on a hierarchical_predecode3x8.
"""

import unittest
from testutils import header,openram_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

class hierarchical_predecode3x8_test(openram_test):

    def runTest(self):
        globals.init_openram("config_20_{0}".format(OPTS.tech_name))
        import hierarchical_predecode3x8 as pre
        import tech

        # checking hierarchical precode 3x8 for single port
        debug.info(1, "Testing sample for hierarchy_predecode3x8")
        a = pre.hierarchical_predecode3x8(name="pre1")
        self.local_check(a)
        
        # checking hierarchical precode 3x8 for multi-port
        OPTS.bitcell = "pbitcell"
        OPTS.num_rw_ports = 1
        OPTS.num_w_ports = 0
        OPTS.num_r_ports = 0
        
        debug.info(1, "Testing sample for hierarchy_predecode3x8 (multi-port case)")
        a = pre.hierarchical_predecode3x8(name="pre2")
        self.local_check(a)

        globals.end_openram()

# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()
