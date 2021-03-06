#!/usr/bin/env python3
"""
Run a regression test on a single transistor column_mux.
"""

from testutils import header,openram_test,unittest
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug
from sram_factory import factory

class single_level_column_mux_test(openram_test):

    def runTest(self):
        globals.init_openram("config_20_{0}".format(OPTS.tech_name))
        import single_level_column_mux_array
        
        # check single level column mux array in single port
        debug.info(1, "Testing sample for 2-way column_mux_array")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux1", columns=16, word_size=8)
        self.local_check(a)

        debug.info(1, "Testing sample for 4-way column_mux_array")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux2", columns=16, word_size=4)
        self.local_check(a)

        debug.info(1, "Testing sample for 8-way column_mux_array")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux3", columns=32, word_size=4)
        self.local_check(a)
        
        # check single level column mux array in multi-port
        OPTS.bitcell = "pbitcell"
        OPTS.num_rw_ports = 1
        OPTS.num_r_ports = 1
        OPTS.num_w_ports = 1

        factory.reset()
        debug.info(1, "Testing sample for 2-way column_mux_array in multi-port")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux4", columns=16, word_size=8, bitcell_bl="bl0", bitcell_br="br0")
        self.local_check(a)

        debug.info(1, "Testing sample for 4-way column_mux_array  in multi-port")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux5", columns=16, word_size=4, bitcell_bl="bl0", bitcell_br="br0")
        self.local_check(a)

        debug.info(1, "Testing sample for 8-way column_mux_array  in multi-port (innermost connections)")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux6", columns=32, word_size=4, bitcell_bl="bl0", bitcell_br="br0")
        self.local_check(a)
        
        debug.info(1, "Testing sample for 8-way column_mux_array  in multi-port (outermost connections)")
        a = single_level_column_mux_array.single_level_column_mux_array(name="mux7", columns=32, word_size=4, bitcell_bl="bl2", bitcell_br="br2")
        self.local_check(a)

        globals.end_openram()
        

# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()
