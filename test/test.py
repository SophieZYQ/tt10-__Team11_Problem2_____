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

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_priority_encoder(dut):
    """Test Priority Encoder with multiple cases"""

    test_cases = [
        (0b00101010, 0b11110001, 13),  # First '1' at position 13
        (0b00000000, 0b00000001, 0),   # First '1' at position 0
        (0b00000000, 0b00000000, 240), # Special case: all zero
        (0b10000000, 0b00000000, 15),  # First '1' at position 15
        (0b00001111, 0b00000000, 7)    # First '1' at position 7
    ]

    for a, b, expected in test_cases:
        dut.ui_in.value = a
        dut.uio_in.value = b
        await Timer(10, units="ns")

        assert dut.uo_out.value == expected, f"Failed for input {a:08b} {b:08b}"
