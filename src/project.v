/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_priority_encoder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
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


  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
