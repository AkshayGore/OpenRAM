#!/usr/bin/env python3
"""
Run a regression test on a precharge cell
"""

import unittest
from testutils import header,openram_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug
from sram_factory import factory

class precharge_test(openram_test):

    def runTest(self):
        globals.init_openram("config_20_{0}".format(OPTS.tech_name))
        import precharge
        import tech
        
        # check precharge in single port
        debug.info(2, "Checking precharge for handmade bitcell")
        tx = precharge.precharge(name="precharge_driver", size=1)
        self.local_check(tx)
        
        # check precharge in multi-port
        OPTS.bitcell = "pbitcell"
        OPTS.num_rw_ports = 1
        OPTS.num_r_ports = 1
        OPTS.num_w_ports = 1

        factory.reset()
        debug.info(2, "Checking precharge for pbitcell (innermost connections)")
        tx = precharge.precharge(name="precharge_driver", size=1, bitcell_bl="bl0", bitcell_br="br0")
        self.local_check(tx)

        debug.info(2, "Checking precharge for pbitcell (innermost connections)")
        tx = precharge.precharge(name="precharge_driver", size=1, bitcell_bl="bl1", bitcell_br="br1")
        self.local_check(tx)
        
        debug.info(2, "Checking precharge for pbitcell (outermost connections)")
        tx = precharge.precharge(name="precharge_driver", size=1, bitcell_bl="bl2", bitcell_br="br2")
        self.local_check(tx)

        globals.end_openram()
        
# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()
