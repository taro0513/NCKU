module half_adder (
    input a,
    input b,
	 output carry,
    output sum
);

and(carry, a, b);
xor(sum, a, b);

endmodule
