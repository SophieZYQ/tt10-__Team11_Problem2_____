# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 50

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

module tt_um_priority_encoder(
  input  wire [15:0] input_signal,  
    output reg  [7:0] encoded_output 
);

   wire [7:0] priority_index;

    assign priority_index = (input_signal[15]) ? 8'd15 :
                            (input_signal[14]) ? 8'd14 :
                            (input_signal[13]) ? 8'd13 :
                            (input_signal[12]) ? 8'd12 :
                            (input_signal[11]) ? 8'd11 :
                            (input_signal[10]) ? 8'd10 :
                            (input_signal[9])  ? 8'd9  :
                            (input_signal[8])  ? 8'd8  :
                            (input_signal[7])  ? 8'd7  :
                            (input_signal[6])  ? 8'd6  :
                            (input_signal[5])  ? 8'd5  :
                            (input_signal[4])  ? 8'd4  :
                            (input_signal[3])  ? 8'd3  :
                            (input_signal[2])  ? 8'd2  :
                            (input_signal[1])  ? 8'd1  :
                            (input_signal[0])  ? 8'd0  : 8'b11110000; 
    assign encoded_output = priority_index;

endmodule

