module adder(a, b, sum, carry);

input a, b;
output sum, carry;

and(carry, a, b);
xor(sum, a, b);

endmodule