module up_down_counter(clock_50hz, reset, up_down, out_7);
	wire clock_div;
	wire [3:0] counter_out;
	input reset, up_down, clock_50hz;
	output [6:0] out_7;

	// module freq.


	frequency_divider (.clock_50hz(clock_50hz), .clock_div(clock_div), .reset(reset));

	// module counter


	counter (.clock_div(clock_div), .up_down(up_down), .out(counter_out), .reset(reset));

	// mosule diplay

	seven_display (.out_7(out_7), .count_sig(counter_out));

endmodule

module frequency_divider(clock_50hz, clock_div, reset);
	input clock_50hz, reset;
	output clock_div;

	reg [31:0] sum = 32'd0, clock_div = 1;

	always @(posedge clock_50hz or negedge reset)
	begin
		if(!reset) begin
			if(sum == 32'd49999999) begin
					sum <= 32'd0;
					clock_div <= ~clock_div;
			end else begin
				  sum <= sum + 1;
			end
		end else begin
//			sum <= 32'd49999999;
			clock_div <= ~clock_div;
		end
	end
endmodule

module seven_display(out_7, count_sig);
input [3:0] count_sig;
output [6:0] out_7;

reg [6:0] out_7;

always@(count_sig)
begin
	case(count_sig)
		4'd0 : out_7 = 7'b1000000;
		4'd1 : out_7 = 7'b1111001;
		4'd2 : out_7 = 7'b0100100;
		4'd3 : out_7 = 7'b0110000;
		4'd4 : out_7 = 7'b0011001;
		4'd5 : out_7 = 7'b0010010;
		4'd6 : out_7 = 7'b0000010;
		4'd7 : out_7 = 7'b1111000;
		4'd8 : out_7 = 7'b0000000;
		4'd9 : out_7 = 7'b0010000;
		4'd10 : out_7 = 7'b0001000;
		4'd11 : out_7 = 7'b0000011;
		4'd12 : out_7 = 7'b1000110;
		4'd13 : out_7 = 7'b0100001;
		4'd14 : out_7 = 7'b0000110;
		4'd15 : out_7 = 7'b0001110;
		default : out_7 = 7'b0000000;
	endcase;
end
endmodule	   


module counter(clock_div, up_down, out, reset);
input clock_div, up_down, reset;
output [3:0] out;

reg [3:0] out = 4'd0;

always @(posedge clock_div)
begin
	if(!reset) begin
		if(up_down) begin
			if (out == 4'd15) begin
				 out <= 4'd0;
			end else begin
				 out <= out + 1;
			end
		end else begin
			if (out == 4'd0) begin
				 out <= 4'd15;
			end else begin
				 out <= out - 1;
			end
		end
	end else begin
		out <= 4'd0;
	end
end
endmodule