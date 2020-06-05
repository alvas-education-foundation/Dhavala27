// Code your testbench here
// or browse Examples
module test;
  reg [15:0]A;
  wire [4:0] zeros;
  num_zero out (.A(A), .zeros(zeros));
  initial begin
    $dumpfile("dumo.vcd");
    $dumpvars(1,test);
    A=16'hFFFF; #100;
    A=16'hF56F; #100;
    A=16'h3FFF; #100;
    A=16'h0001; #100;
    A=16'hF10F; #100;
    A=16'hF822; #100;
    A=16'h7ABC; #100;
  end
